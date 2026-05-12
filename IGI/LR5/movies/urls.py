from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.movie_list, name='movie_list'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^news/$', views.news_list, name='news'),
    re_path(r'^faq/$', views.faq_list, name='faq'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
    re_path(r'^vacancies/$', views.vacancies, name='vacancies'),
    re_path(r'^reviews/$', views.reviews, name='reviews'),
    re_path(r'^promos/$', views.promos, name='promos'),
    re_path(r'^privacy/$', views.privacy, name='privacy'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^movie/add/$', views.movie_create, name='movie_create'),
    re_path(r'^movie/(?P<pk>\d+)/edit/$', views.movie_update, name='movie_update'),
    re_path(r'^movie/(?P<pk>\d+)/delete/$', views.movie_delete, name='movie_delete'),
]