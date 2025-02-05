# Task Management API

RESTful API для управления задачами пользователей с аутентификацией JWT и PostgreSQL.

## Особенности

- 🔐 Аутентификация через JWT (OAuth2)
- 📝 CRUD операции для задач и пользователей
- 🔍 Фильтрация задач по названию и времени создания
- 🐘 Использование PostgreSQL в качестве БД
- 🚀 FastAPI с асинхронной поддержкой
- 🛠 Валидация данных через Pydantic
- 📦 Структура проекта по модулям

## Требования

- Python 3.9+
- Docker

## Быстрый старт

1. Склонируйте репозиторий:
   ```cmd
   git clone https://github.com/RailSafiullin/smartsoft_test_case

2. Перейдите в папку проекта:
   ```cmd
   cd smartsoft_test_case\task_manager

3. Запустите докер контейнер
   ```cmd
   docker-compose up --build

4. Перейдите к документации API - Swagger UI: http://localhost:8000/docs
