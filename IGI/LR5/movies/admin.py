from django.contrib import admin
from .models import Genre, Actor, Movie, Hall, Screening, Employee

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Screening)
admin.site.register(Employee)
