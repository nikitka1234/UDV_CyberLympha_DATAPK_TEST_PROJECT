## Технологии
* Python
* aiohttp
* Redis
* CurrencyAPI

## Как запустить
1. Склонировать репозиторий
2. Создание и активация виртуального окружения
```commandline
python -m venv venv
GitBash: source venv/Scripts/activate
Windows: venv\Scripts\activate
Linux: source venv/bin/activate
```
3. Установка зависимостей
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки. API от сервиса прикрепил свой
```text
HOST=[HOST]
PORT=[PORT]
PASSWORD=[PASSWORD]

CURRENCY_API_TOKEN=Bvw9n2yCqnYQA6dGNRtiUDJU65dR2KpTIHu6J0G7
```
5. Запуск 
```commandline
python -m aiohttp.web -H localhost -P 8080 currency_api.main:init_func
```