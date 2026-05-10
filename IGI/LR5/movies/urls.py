from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('about/', views.about, name='about'),
    path('news/', views.news_list, name='news'),
    path('faq/', views.faq_list, name='faq'),
    path('contacts/', views.contacts, name='contacts'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.reviews, name='reviews'),
    path('promos/', views.promos, name='promos'),
    path('privacy/', views.privacy, name='privacy'),
]