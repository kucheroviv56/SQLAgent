-- Создаём read-only пользователя
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'ai_readonly') THEN
        CREATE ROLE ai_readonly WITH LOGIN PASSWORD 'supersecret';
    END IF;
END$$;

-- Разрешаем подключение к базе и схеме
GRANT CONNECT ON DATABASE demo TO ai_readonly;
GRANT USAGE ON SCHEMA public TO ai_readonly;

-- Разрешаем SELECT на все существующие таблицы
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ai_readonly;

-- Разрешаем SELECT на все будущие таблицы
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO ai_readonly;
