#!/bin/bash
set -e # Остановить скрипт при любой ошибке

echo "--- Начинаю миграции ---"
python manage.py migrate --noinput

echo "--- Собираю статику ---"
python manage.py collectstatic --noinput

echo "--- Пытаюсь загрузить данные из JSON ---"
if [ -f "initial_data.json" ]; then
    python manage.py loaddata initial_data.json || echo "Предупреждение: данные не загружены, но продолжаем..."
fi

echo "--- Запускаю Gunicorn ---"
exec gunicorn cinema_project.wsgi:application --bind 0.0.0.0:8000