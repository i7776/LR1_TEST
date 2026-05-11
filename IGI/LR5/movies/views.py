from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Movie, AboutCompany, News, FAQ, ContactInfo, Vacancy, Review, PromoCode
import requests
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import datetime
import calendar
from django.utils import timezone

def movie_list(request):
    movies = Movie.objects.all()

    # ПОИСК: если в адресе есть параметр 'q'
    query = request.GET.get('q')
    if query:
        # icontains — поиск по части слова (без учета регистра)
        movies = movies.filter(title__icontains=query)

    sort_by = request.GET.get('sort')
    if sort_by == 'rating':
        movies = movies.order_by('-rating') # минус означает от большего к меньшему
    elif sort_by == 'new':
        movies = movies.order_by('-data')
    elif sort_by == 'old':
        movies = movies.order_by('data')

    now = datetime.datetime.now()
    # Текстовый календарь на текущий месяц
    cal = calendar.HTMLCalendar(calendar.MONDAY).formatmonth(now.year, now.month)

    # статистика
    stats = {
        'total_count': movies.count(),
        'average_rating': movies.aggregate(Avg('rating'))['rating__avg'], # агр считает итоговое число и возвращает словарь
    }

    return render(request, 'movies/index.html', {
        'movies': movies,
        'stats': stats, # передаем статистику
        'current_time_local': now,
        'current_time_utc': datetime.datetime.utcnow(),
        'user_timezone': timezone.get_current_timezone_name(),
        'calendar': cal,
        'query': query
    })

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # создаем пользователя в бд
            login(request, user) # входим на сайт под этим именем
            return redirect('movie_list') # уходим на главную
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})