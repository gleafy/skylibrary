FROM python:3.10-slim

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Собираем статику
RUN python manage.py collectstatic --noinput

# Команда запуска (миграции + сервер)
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 config.wsgi:application