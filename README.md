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

4. Задать права пользователя ai-readonly

docker exec -it demo-db psql -U demo -d demo


DO $$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'ai_readonly') THEN
      CREATE ROLE ai_readonly WITH LOGIN PASSWORD 'supersecret';
   END IF;
END
$$;

GRANT CONNECT ON DATABASE demo TO ai_readonly;

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN SELECT nspname FROM pg_namespace 
             WHERE nspname NOT IN ('pg_catalog','information_schema') LOOP
        EXECUTE format('GRANT USAGE ON SCHEMA %I TO ai_readonly;', r.nspname);
        EXECUTE format('GRANT SELECT ON ALL TABLES IN SCHEMA %I TO ai_readonly;', r.nspname);
        EXECUTE format('GRANT SELECT ON ALL SEQUENCES IN SCHEMA %I TO ai_readonly;', r.nspname);
        EXECUTE format('ALTER DEFAULT PRIVILEGES IN SCHEMA %I GRANT SELECT ON TABLES TO ai_readonly;', r.nspname);
    END LOOP;
END$$;


5. Включить VPN

Для корректной работы с OpenAI API требуется активное VPN-соединение.

6. Проверка API

После запуска сервис будет доступен по адресу:

http://localhost:8000