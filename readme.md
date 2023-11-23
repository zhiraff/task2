## Инструкция по запуску

### 1. Склонировать и перейти в директорию

`$ git clone https://github.com/zhiraff/task2.git`
`$ cd task2/`

### 2. Создать и активировать виртуальное окружение (необязательно)

`$ python3 -m venv .venv`
`$ source ./.venv/bin/activate`

### 3. Установить зависимости

`$ pip install -r requirements.txt`

### 4. Скачать client_secrets.json и положить в корень проекта

Подробнее о том, где и как взять client_secrets.json описано не здесь

### 5. Применить миграци (при необходимости)

`$ python3 manage.py migrate`

### 6. Создать суперпользователя (при необходимости)

`$ python3 manage.py createsuperuser`

### 7. Запуск приложения

`$ python3 manage.py runserver

### 8. Пройти аутентификацию в google и ввести код подтверждения в консоль

### Готово!
