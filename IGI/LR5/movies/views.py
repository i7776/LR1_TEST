from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all() # Берем все фильмы из базы
    return render(request, 'movies/index.html', {'movies': movies})
