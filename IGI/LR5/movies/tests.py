from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth.models import User

class CinemaLabTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser('admin_test', 'a@t.com', 'pass123')
        self.user = User.objects.create_user('user_test', 'u@t.com', 'pass123')

        self.genre = Genre.objects.create(name="Драма")
        self.actor = Actor.objects.create(name="Тестовый Актер") # Создаем актера для тестов
        self.hall = Hall.objects.create(number=1, capacity=50)
        self.movie = Movie.objects.create(
            title="Тестовый фильм",
            data=date.today(),
            duration=120,
            budget=1000,
            country="США",
            genre=self.genre,
            rating=8.0
        )
        self.screening = Screening.objects.create(
            movie=self.movie,
            hall=self.hall,
            time=timezone.now() + timedelta(days=1),
            price=15.0
        )
        AboutCompany.objects.create(title="О нас", content="Инфо", history="История", requisites="Реквизиты")
        News.objects.create(title="Новость", short_description="Кратко", content="Текст")
        FAQ.objects.create(question="Вопрос", answer="Ответ")
        Vacancy.objects.create(title="Вариант", description="Описание")
        PromoCode.objects.create(code="SALE", discount=10)

    # проверка доступности
    def test_pages_available(self):
        pages = ['movie_list', 'about', 'news', 'faq', 'contacts', 'vacancies', 'reviews', 'promos', 'privacy']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200)

    # тест поиска
    def test_search(self):
        response = self.client.get(reverse('movie_list'), {'q': 'Тестовый'})
        self.assertContains(response, "Тестовый фильм")

    # тест создания отзыва
    def test_review(self):
        response = self.client.post(reverse('reviews'), {
            'name': 'Иван',
            'rating': 5,
            'text': 'Крутой кинотеатр!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

    # 18+
    def test_age_limit(self):
        young_date = date.today() - timedelta(days=365*10)
        response = self.client.post(reverse('register'), {
            'username': 'kid_user',
            'password1': 'CinemaLab_2026!',
            'password2': 'CinemaLab_2026!',
            'first_name': 'Ребенок',
            'last_name': 'Тестовый',
            'birth_date': young_date.strftime('%Y-%m-%d')
        })
        self.assertContains(response, "Регистрация только для лиц старше 18 лет!")

    # create
    def test_admin_create_movie_post(self):
        self.client.login(username='admin_test', password='pass123')
        response = self.client.post(reverse('movie_create'), {
            'title': 'Новый фильм через тест',
            'description': 'Описание',
            'data': '2026-05-15',
            'duration': 150,
            'budget': 5000,
            'country': 'Италия',
            'genre': self.genre.id,
            'rating': 7.5,
            'actors': [self.actor.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Movie.objects.filter(title='Новый фильм через тест').exists())

    # create - бронирование
    def test_book_ticket_post(self):
        self.client.login(username='user_test', password='pass123')
        response = self.client.post(reverse('book_ticket', args=[self.screening.id]), {
            'seat_numbers': '10, 11'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ticket.objects.count(), 2)

    # delete - отмена
    def test_cancel_ticket(self):
        ticket = Ticket.objects.create(screening=self.screening, user=self.user, seat_number=20)
        self.client.login(username='user_test', password='pass123')
        response = self.client.post(reverse('cancel_ticket', args=[ticket.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Ticket.objects.filter(id=ticket.id).exists())

    # безопасность
    def test_user_cannot_delete_movie(self):
        self.client.login(username='user_test', password='pass123')
        response = self.client.get(reverse('movie_delete', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)