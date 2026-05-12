from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, AboutCompany, News, FAQ, ContactInfo, Vacancy, Review, PromoCode, ClientProfile
import requests
from .forms import ReviewForm, ExtendedUserCreationForm, MovieForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from datetime import date
import datetime
import calendar
from django.utils import timezone
import numpy as np

def movie_list(request):
    movies = Movie.objects.all()

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

    now = datetime.datetime.now()
    cal = calendar.HTMLCalendar(calendar.MONDAY).formatmonth(now.year, now.month)

    context = {
        'movies': movies_list,
        'stats': stats,
        'query': query,
        'genre_data': genre_data,
        'current_time_local': now,
        'current_time_utc': datetime.datetime.utcnow(),
        'user_timezone': timezone.get_current_timezone_name(),
        'calendar': cal,
    }

    return render(request, 'movies/index.html', context)

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
        weather_data = None # Если интернет пропал, страница не должна упасть

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

# 1. Создание нового фильма
def movie_create(request):
    if not request.user.is_superuser: # Если не админ - уходи
        return redirect('movie_list')

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES) # FILES нужен для загрузки постера
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Добавить новый фильм'})

# 2. Редактирование существующего фильма
def movie_update(request, pk):
    if not request.user.is_superuser:
        return redirect('movie_list')

    movie = get_object_or_404(Movie, pk=pk) # Ищем фильм по ID или выдаем ошибку 404
    if request.method == "POST":
        # instance=movie говорит Django: "не создавай новый, а обнови этот"
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Редактировать фильм'})

# 3. Удаление фильма
def movie_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('movie_list')

    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST": # Если нажали кнопку подтверждения
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})