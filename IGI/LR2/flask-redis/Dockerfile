# Используем легковесный образ Python
FROM python:3.14-alpine

# Назначаем рабочую директорию
WORKDIR /code

# Устанавливаем переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Копируем зависимости и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Копируем весь оставшийся код в контейнер
COPY . .

# Команда для запуска приложения
CMD ["flask", "run"]
