from django.shortcuts import render
from django.db.models import Avg
from .models import Movie

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