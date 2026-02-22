# используем образ Python
FROM python:3.9-slim

# yстанавливаем рабочую папку внутри контейнера
WORKDIR /app

# копируем .py файлы в контейнер
COPY . .

# запускаем скрипт
CMD ["python", "main.py"]
