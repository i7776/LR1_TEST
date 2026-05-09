import os
import django
import requests
from datetime import datetime
from movies.models import Movie, Genre

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
django.setup()

def fetch_movies():
    api_key = '83e7f40222f4529dadf79c3cb637f592'
    

