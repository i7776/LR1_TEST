FROM python:3.14-alpine

# назначаем рабочую директорию
WORKDIR /code

# устанавливаем переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# копируем зависимости и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# открываем порт 5000
EXPOSE 5000

# копируем весь оставшийся код в контейнер
COPY . .

# запускаум приложения
CMD ["flask", "run"]
