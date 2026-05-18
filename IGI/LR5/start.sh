#!/bin/bash

# 1. Применяем миграции (обновляем структуру базы)
python manage.py migrate

# 2. Выполняем очистку данных (удаляем старые/пустые записи)
python data_cleaner.py

# 3. Собираем статические файлы (картинки, CSS)
python manage.py collectstatic --noinput

# 4. Запускаем сервер через Gunicorn
gunicorn cinema_project.wsgi:application --bind 0.0.0.0:8000