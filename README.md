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
2. Клонируйте репозиторий;
    ```bash
    git clone https://github.com/gleafy/skylibrary
    cd skylibrary
    ```
3. Создайте .env файл на основе существующего примера .env.example
4. Запустите проект командой:
    ```bash
    docker-compose up -d --build
    ```
5.  Создайте суперпользователя (администратора):
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Документация API

После запуска документация доступна по адресу:

  * Swagger UI: `http://localhost/`
  * ReDoc: `http://localhost/redoc/`

## Права доступа (Permissions)

  * **Анонимные пользователи**: Могут просматривать список книг (GET).
  * **Администраторы**: Могут добавлять, изменять и удалять книги.
