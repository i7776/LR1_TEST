#!/bin/bash

# 1. Миграции
python manage.py migrate --noinput

# 2. ЗАГРУЗКА ДАННЫХ
if [ -f "initial_data.json" ]; then
    python manage.py loaddata initial_data.json
fi

# 4. Сборка статики
python manage.py collectstatic --noinput

# 5. Запуск
gunicorn cinema_project.wsgi:application --bind 0.0.0.0:8000