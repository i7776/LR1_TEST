from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Movie, AboutCompany, News, FAQ, ContactInfo, Vacancy, Review, PromoCode
import requests
from .forms import ReviewForm

def movie_list(request):
    movies = Movie.objects.all()

    # статистика
    stats = {
        'total_count': movies.count(),
        'average_rating': movies.aggregate(Avg('rating'))['rating__avg'], # агр считает итоговое число и возвращает словарь
    }

    return render(request, 'movies/index.html', {
        'movies': movies,
        'stats': stats # передаем статистику
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