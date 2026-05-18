from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, AboutCompany, News, FAQ, ContactInfo, Vacancy, Review, PromoCode, ClientProfile, Screening, Ticket, Employee
import requests
from .forms import ReviewForm, ExtendedUserCreationForm, MovieForm, ScreeningForm, TicketForm
import logging
from django.contrib.auth import login
from datetime import date
import calendar
from django.utils import timezone
import numpy as np
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
import matplotlib.pyplot as plt
import io
import urllib, base64
logger = logging.getLogger('django')

def log_this(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = "Аноним"
        logger.info(f"ПОЛЬЗОВАТЕЛЬ: {user} | ВЫЗВАЛ ФУНКЦИЮ: {func.__name__}")
        return func(request, *args, **kwargs)
    return wrapper

def is_staff_or_admin(user):
    if not user.is_authenticated:
        return False
    return user.is_superuser or Employee.objects.filter(user=user).exists()

@log_this
def movie_list(request):
    movies = Movie.objects.all()

    stats = None
    genre_data = None
    graph = None

    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort')

    if sort_by == 'rating':
        movies = movies.order_by('-rating')
    elif sort_by == 'new':
        movies = movies.order_by('-data')
    elif sort_by == 'old':
        movies = movies.order_by('data')

    if query:
        movies_list = [m for m in movies if query.lower() in m.title.lower()]
    else:
        movies_list = list(movies)

    if is_staff_or_admin(request.user):
        ratings = [float(m.rating) for m in movies_list]
        stats = {
            'total_count': len(movies_list),
            'average_rating': 0,
            'median_rating': 0,
            'mode_rating': 0,
        }

        if ratings:
            stats['average_rating'] = np.mean(ratings)
            stats['median_rating'] = np.median(ratings)

            vals, counts = np.unique(ratings, return_counts=True)
            index = np.argmax(counts)
            stats['mode_rating'] = vals[index]

        raw_genre_data = {}
        for m in movies_list:
            name = m.genre.name
            raw_genre_data[name] = raw_genre_data.get(name, 0) + 1

        # превращаем в список словарей, чтобы было удобно выводить
        genre_data = []
        for name, count in raw_genre_data.items():
            genre_data.append({
                'name': name,
                'count': count,
                'bar_height': count * 8 + 10
            })

        graph = get_graph()

    now = timezone.localtime(timezone.now())
    cal = calendar.HTMLCalendar(calendar.MONDAY).formatmonth(now.year, now.month)

    context = {
        'movies': movies_list,
        'is_staff': is_staff_or_admin(request.user),
        'stats': stats,
        'query': query,
        'genre_data': genre_data,
        'current_time_local': now,
        'current_time_utc': timezone.now(),
        'user_timezone': timezone.get_current_timezone_name(),
        'calendar': cal,
        'graph': graph,
    }

    return render(request, 'movies/index.html', context)


def get_graph():
    # создаем буфер для картинки
    buffer = io.BytesIO()
    # считаем жанры
    all_movies = Movie.objects.all()
    genres = [m.genre.name for m in all_movies]
    genre_counts = {g: genres.count(g) for g in set(genres)}

    # рисуем
    plt.figure(figsize=(7, 4))
    plt.bar(genre_counts.keys(), genre_counts.values(), color='orange')
    plt.title('Фильмы по жанрам')
    #  на 45 градусов
    # ha='right' выравнивает текст по правому краю
    plt.xticks(rotation=45, ha='right')
    # раздвинет границы графика, чтобы подписи влезли
    plt.tight_layout()

    # сохраняем в буфер
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # кодируем в строку
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def about(request):
    info = AboutCompany.objects.first()

    api_key = '504267ace31998cc175837536355a073'
    city = 'Minsk'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    weather_data = {}
    try:
        response = requests.get(weather_url)
        print(f"Статус погоды: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description'],
                'city': city
            }
    except:
        weather_data = None # если интернет пропал, страница не должна упасть

    return render(request, 'movies/about.html', {
        'info': info,
        'weather': weather_data
    })

def news_list(request):
    all_news = News.objects.all().order_by('-id')
    return render(request, 'movies/news.html', {'news': all_news})

def faq_list(request):
    faqs = FAQ.objects.all().order_by('-added_date')
    return render(request, 'movies/faq.html', {'faqs': faqs})

def contacts(request):
    staff = ContactInfo.objects.all()
    return render(request, 'movies/contacts.html', {'staff': staff})

def vacancies(request):
    items = Vacancy.objects.all()
    return render(request, 'movies/vacancies.html', {'vacancies': items})

def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() # cохраняем отзыв в бд
            return redirect('reviews') # перезагружаем страницу

    # если пользователь просто зашел на страницу (метод GET)
    else:
        form = ReviewForm()

    # забираем все отзывы из базы, чтобы показать их под формой
    items = Review.objects.all().order_by('-created_date')

    return render(request, 'movies/reviews.html', {
        'reviews': items,
        'form': form
    })


def promos(request):
    codes = PromoCode.objects.all().order_by('-is_active')
    return render(request, 'movies/promos.html', {'promos': codes})

def privacy(request):
    return render(request, 'movies/privacy.html')

@log_this
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data.get('birth_date')

            # 18+
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

            if age < 18:
                user.delete()
                return render(request, 'registration/register.html', {
                    'form': form,
                    'error': "Регистрация только для лиц старше 18 лет!"
                })

            ClientProfile.objects.create(user=user, birth_date=birth_date)

            login(request, user)
            return redirect('movie_list')
    else:
        form = ExtendedUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def check_admin(user):
    return user.is_superuser

# создание нового фильма
@user_passes_test(check_admin)
def movie_create(request):
    if not request.user.is_superuser: # если не админ - уходи
        return redirect('movie_list')

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES) # FILES нужен для загрузки постера
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Добавить новый фильм'})

# редактирование существующего фильма
@user_passes_test(check_admin)
def movie_update(request, pk):
    if not request.user.is_superuser:
        return redirect('movie_list')

    movie = get_object_or_404(Movie, pk=pk) # Ищем фильм по ID или выдаем ошибку 404
    if request.method == "POST":
        # instance=movie не создавай новый, а обнови этот
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Редактировать фильм'})

# удаление фильма
@user_passes_test(check_admin)
def movie_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('movie_list')

    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST": # усли нажали кнопку подтверждения
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})

# создание сеанса
def screening_create(request):
    if not request.user.is_superuser: return redirect('movie_list')

    # Пытаемся поймать ID фильма из ссылки
    movie_id = request.GET.get('movie_id')
    initial_data = {}
    if movie_id:
        initial_data['movie'] = movie_id # предзаполняем поле movie

    if request.method == "POST":
        form = ScreeningForm(request.POST)
        if form.is_valid():
            Screening.objects.create(
                movie=form.cleaned_data['movie'],
                hall=form.cleaned_data['hall'],
                time=form.cleaned_data['time'],
                price=form.cleaned_data['price']
            )
            return redirect('movie_list')
    else:
        form = ScreeningForm(initial=initial_data)

    return render(request, 'movies/screening_form.html', {'form': form, 'title': 'Добавить сеанс'})

# Редактирование сеанса
def screening_update(request, pk):
    if not request.user.is_superuser: return redirect('movie_list')

    try:
        sc = Screening.objects.get(id=pk)
    except Screening.DoesNotExist:
        raise Http404("Сеанс не найден")

    if request.method == "POST":
        form = ScreeningForm(request.POST)
        if form.is_valid():
            sc.movie = form.cleaned_data['movie']
            sc.hall = form.cleaned_data['hall']
            sc.time = form.cleaned_data['time']
            sc.price = form.cleaned_data['price']
            sc.save()
            return redirect('movie_list')
    else:
        initial = {'movie': sc.movie, 'hall': sc.hall, 'time': sc.time, 'price': sc.price}
        form = ScreeningForm(initial=initial)

    return render(request, 'movies/screening_form.html', {'form': form, 'title': 'Изменить сеанс'})

# удаление сеанса
def screening_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('movie_list')
    try:
        sc = Screening.objects.get(id=pk)
        sc.delete()
    except Screening.DoesNotExist:
        pass
    return redirect('movie_list')

# покупка билета
@log_this
@login_required
def book_ticket(request, screening_id):
    screening = get_object_or_404(Screening, id=screening_id)

    # список занятых мест
    taken_tickets = Ticket.objects.filter(screening=screening).values_list('seat_number', flat=True)
    taken_seats = list(taken_tickets)

    total_capacity = screening.hall.capacity
    free_seats = [i for i in range(1, total_capacity + 1) if i not in taken_seats]

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            seats_input = form.cleaned_data['seat_numbers']
            code_text = form.cleaned_data.get('promo_code') # Получаем промокод из формы

            # парсим номера мест
            try:
                requested_seats = [int(s.strip()) for s in seats_input.split(',')]
            except ValueError:
                messages.error(request, "Ошибка формата! Вводите только числа через запятую.")
                return redirect('book_ticket', screening_id=screening.id)

            # проверяем места на валидность
            errors = []
            valid_seats = []
            for seat in requested_seats:
                if seat > total_capacity or seat < 1:
                    errors.append(f"Места №{seat} нет в зале.")
                elif seat in taken_seats:
                    errors.append(f"Место №{seat} уже занято.")
                else:
                    valid_seats.append(seat)

            if errors:
                for error in errors:
                    messages.error(request, error)
            elif not valid_seats:
                messages.error(request, "Вы не выбрали ни одного места.")
            else:
                base_price = len(valid_seats) * screening.price
                final_price = float(base_price)

                # применяем промокод
                if code_text:
                    promo = PromoCode.objects.filter(code=code_text, is_active=True).first()
                    if promo:
                        discount = promo.discount
                        final_price = float(base_price) * (1 - discount / 100)
                        messages.success(request, f"Применен промокод на {discount}%!")
                    else:
                        messages.error(request, "Промокод не найден или не активен.")
                price_per_ticket = final_price / len(valid_seats)

                # билеты в базе
                for seat in valid_seats:
                    Ticket.objects.create(
                        screening=screening,
                        user=request.user,
                        seat_number=seat,
                        paid_price=price_per_ticket
                    )

                messages.success(request, f"Успешно забронировано мест: {len(valid_seats)}. Итого к оплате: {final_price:.2f} BYN.")
                return redirect('my_tickets')
    else:
        form = TicketForm()

    return render(request, 'movies/book_ticket.html', {
        'screening': screening,
        'form': form,
        'free_seats': free_seats,
        'taken_seats': taken_seats
    })

# личный кабинет пользователя (список билетов)
@log_this
@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    total_sum = sum(t.paid_price for t in tickets)
    return render(request, 'movies/my_tickets.html', {
        'tickets': tickets,
        'total_sum': total_sum # Передаем сумму в шаблон
    })

# отмена брони (удаление билета)
@log_this
@login_required
def cancel_ticket(request, ticket_id):
    # билет существует и принадлежит этому юзеру
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('my_tickets')
    return render(request, 'movies/ticket_confirm_delete.html', {'ticket': ticket})
