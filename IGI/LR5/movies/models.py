from django.db import models
from django.contrib.auth.models import User
import re
from django.core.exceptions import ValidationError
from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя актера")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назавание фильма")
    description = models.TextField(verbose_name="Описание")
    data = models.DateField(verbose_name="Год выпуска")
    duration = models.IntegerField(verbose_name="Длительность")
    budget =  models.PositiveBigIntegerField(default=0, verbose_name="Бюджет")
    country = models.CharField(max_length=100, verbose_name="Страна")
    #Многие к одному
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер", null=True, blank=True)
    #Многие ко многим
    actors = models.ManyToManyField(Actor, verbose_name="Актеры")

    def __str__(self):
        return self.title

class Hall(models.Model):
    number = models.IntegerField(default=1, verbose_name="Номер")
    capacity = models.IntegerField(verbose_name="Мест")

    def __str__(self):
        return f"Зал №{self.number}"

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="Время сеанса")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.movie.title} | {self.time}"

class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE, verbose_name="Сеанс")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    seat_number = models.IntegerField(verbose_name="Номер места")
    buy_date = models.DateTimeField(auto_now_add=True)
    paid_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена оплаты", default=0)

    def __str__(self):
        return f"Билет на {self.screening.movie.title} (Место: {self.seat_number})"

def validate_phone_number(value):
    pattern = r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$'
    if not re.match(pattern, value):
        raise ValidationError("Номер телефона должен быть в формате +375 (29) XXX-XX-XX")


def validate_employee_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("Сотрудник должен быть старше 18 лет!")


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, verbose_name="Должность")

    # Подключаем наши функции к полям
    birth_date = models.DateField(validators=[validate_employee_age], verbose_name="Дата рождения", null=True)
    phone = models.CharField(max_length=20, validators=[validate_phone_number], verbose_name="Телефон", null=True)

    def __str__(self):
        return f"{self.user.username} ({self.position})"

class AboutCompany(models.Model):
    title = models.CharField(max_length=200, default="О нашей компании")
    logo = models.ImageField(upload_to='logo/', verbose_name="Логотип")
    content = models.TextField(verbose_name="О компании")
    history = models.TextField(verbose_name="История компании")
    requisites = models.TextField(verbose_name="Реквизиты")

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name="Полный текст статьи")
    short_description = models.CharField(max_length=300, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=300, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    added_date = models.DateField(auto_now_add=True)

class ContactInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='staff/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.employee.user.get_full_name()} - {self.employee.position}"

class PrivacyPolicy(models.Model):
    text = models.TextField(verbose_name="Текст политики")
    updated_at = models.DateTimeField(auto_now=True)

class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание вакансии")
    salary = models.CharField(max_length=100, verbose_name="Зарплата", blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Оценка")
    text = models.TextField(verbose_name="Текст отзыва")
    created_date = models.DateTimeField(auto_now_add=True)

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Промокод")
    discount = models.IntegerField(verbose_name="Скидка")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.code

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"Профиль: {self.user.username}"
