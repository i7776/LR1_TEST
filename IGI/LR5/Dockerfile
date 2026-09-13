FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py migrate --noinput && python manage.py loaddata initial_data.json && python manage.py collectstatic --noinput && gunicorn cinema_project.wsgi:application --bind 0.0.0.0:8000