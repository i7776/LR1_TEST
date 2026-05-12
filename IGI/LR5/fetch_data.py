import os
import django
import requests
from datetime import datetime

# найти  настройки проекта cinema_project и включи все инструменты Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
django.setup()

from movies.models import Movie, Genre, Actor

def fetch_movies():
    api_key = '83e7f40222f4529dadf79c3cb637f592'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ru-RU&page=1'
    default_genre, _ = Genre.objects.get_or_create(name="Популярное")

    print("Запрашиваю данные из TMDB...")

    try:
        response = requests.get(url)
        movies_list = response.json().get('results', [])

        for item in movies_list[:12]:
            movie_id = item['id'] # нужен ID для запроса актеров

            # обработка даты
            raw_date = item.get('release_date')
            release_date = datetime.strptime(raw_date, '%Y-%m-%d').date() if raw_date else datetime.now().date()

            # создаем или находим фильм
            movie, created = Movie.objects.get_or_create(
                title=item['title'],
                defaults={
                    'description': item.get('overview', 'Описания нет'),
                    'data': release_date,
                    'duration': 120,
                    'budget': 50000000,
                    'country': "США",
                    'genre': default_genre,
                    'rating': item.get('vote_average', 0.0),
                }
            )

            print(f"Загружаю актеров для фильма: {movie.title}...")
            credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ru-RU'
            credits_resp = requests.get(credits_url).json()
            cast = credits_resp.get('cast', [])[:5] # Берем только ТОП-5 актеров

            for actor_data in cast:
                # Создаем актера в нашей базе
                actor_obj, _ = Actor.objects.get_or_create(name=actor_data['name'])
                # Привязываем его к фильму (это и есть работа ManyToManyField)
                movie.actors.add(actor_obj)

            if created:
                print(f" Добавлен: {movie.title}")
            else:
                print(f" Уже есть: {movie.title}")

        print("\nВсе готово! Теперь в базе есть настоящие фильмы.")

    except Exception as e:
        print(f" Произошла ошибка: {e}")

if __name__ == '__main__':
    fetch_movies()

