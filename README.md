# Library Management API

Дипломный проект: REST API сервис для управления библиотекой.

## Технологический стек
* **Python 3.10** & **Django 4.2**
* **Django REST Framework (DRF)** - построение API
* **PostgreSQL** - база данных
* **Docker & Docker Compose** - контейнеризация
* **JWT** - авторизация
* **Swagger/OpenAPI** - автодокументация

## Запуск проекта

1. Убедитесь, что установлен Docker и Docker Compose.
2. Запустите проект командой:
    ```bash
    docker-compose up -d --build
    ```
3.  Создайте суперпользователя (администратора):
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Документация API

После запуска документация доступна по адресу:

  * Swagger UI: `http://localhost:8000/`
  * ReDoc: `http://localhost:8000/redoc/`

## Права доступа (Permissions)

  * **Анонимные пользователи**: Могут просматривать список книг (GET).
  * **Администраторы**: Могут добавлять, изменять и удалять книги.
