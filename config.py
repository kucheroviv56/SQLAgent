import os

DB_USER = os.getenv("DB_USER", "ai_readonly")
DB_PASSWORD = os.getenv("DB_PASSWORD", "supersecret")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "demo")

DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
# OPENAI_API_KEY = ""
LOG_FILE = os.getenv("AGENT_LOG_FILE", "agent.log")
