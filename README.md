# Лабораторна робота: Налаштування середовища для розробки REST API

## Мета роботи
Налаштувати середовище для подальшого виконання лабораторних робіт з дисципліни та розробити базове REST API.

## Завдання
1. Налаштування середовища, типового для розробки бекенду на Python.
2. Розробка healthcheck ендпоінта веб застосунку.
3. Налаштування деплою застосунку.
4. Тестування REST API за допомогою Insomnia.

## Практичне завдання
Практичне завдання полягає в налаштуванні шаблону проекту для веб застосунку. Потрібно створити базовий проект з ендпоінтом, який буде вітати користувача. Налаштувати для нього Docker-контейнер, а також конфігурацію для Docker Compose. Після цього задеплоїти цей маленький проект за допомогою [Render.com](https://render.com).

## Вимоги до виконання
- Виконане завдання повинно знаходитись у вигляді репозиторію в системі контролю версій (рекомендовано GitHub).
- Повинні бути структуровані коміти.
- В `README.md` повинні міститись повні інструкції для запуску проекту.
- Проект повинен бути задеплоєний та мати GET ендпоінт `/healthcheck`, який повинен віддавати код відповіді 200 і в тілі відповіді містити JSON з поточною датою та статусом сервісу.

## Методичні рекомендації
1. Створити проект в Git та клонувати його.
2. Перейти в папку проекту.
3. Встановити Python в системі (опціонально, можете одразу розробляти в Docker).
4. Створити віртуальне середовище:
   ```bash
   python3 -m venv env
5. Активувати віртуальне середовище:
    source ./env/bin/activate
6. Встановити Flask:
    pip install flask
7. Записати всі залежності в requirements.txt:
   pip freeze > requirements.txt
8. Створити папку для модуля проекту та файли __init__.py та views.py.
9. У файлі __init__.py створити змінну app та імпортувати файли:
    from flask import Flask

    app = Flask(__name__)

    import <your_app_module_name>.views
10. Реалізувати ендпоінт healthcheck у views.py.
11. Запустити застосунок:

## Налаштування Docker
1. Встановити Docker з офіційного сайту.
2. Створити Dockerfile:
   FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

CMD flask --app <your_app_name> run -h 0.0.0.0 -p $PORT

3. Збілдити образ:
  docker build . -t <image_name>:latest
4. Запустити контейнер:
  docker run -it --rm --network=host -e PORT=<your_port> <image_name>:latest

## Налаштування Docker Compose
1. Створити docker-compose.yaml:
services:
  <app_name>:
    restart: always
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      PORT: "<your_port>"
    ports:
      - "<your_port>:8080"
2. Запустити:
  docker-compose build
  docker-compose up

## Деплой
1. Зареєструватися на Render.com.
2. Створити новий сервіс типу Web Service.
3. Підключити свій репозиторій.
4. Запустити процес деплою.

## Посилання
https://backend-lab-1-30ng.onrender.com/

## Автор
Рабійчук Дар'я, група ІМ-21

P.S. Не забудьте замінити `<your_app_module_name>`, `<your_port>`, `<image_name>` та `<app_name>` на відповідні значення.
