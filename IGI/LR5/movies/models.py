from django.db import models
from django.contrib.auth.models import User

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

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, verbose_name="Должность (Кассир)")


