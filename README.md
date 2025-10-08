Требования

Docker + Docker Compose

OpenAI API Key

Дамп БД 

VPN (для доступа к OpenAI API)

Шаги запуска
1. Установить переменные окружения

Задайте ключ OpenAI через переменные окружения системы:

OPENAI_API_KEY=ваш_ключ

2. Поднять контейнеры

docker-compose build
docker-compose up -d

Это поднимет:

demo-db — контейнер с Postgres

api — API на FastAPI

3. Загрузить дамп в базу

Если у вас есть дамп dump.sql:

docker exec -i demo-db psql -U demo -d demo < dump.sql

4. Включить VPN

Для корректной работы с OpenAI API требуется активное VPN-соединение.

5. Проверка API

После запуска сервис будет доступен по адресу:

http://localhost:8000