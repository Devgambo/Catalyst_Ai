from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    QDRANT_API_KEY: str
    REDIS_URL: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    GEMINI_API_KEY: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()