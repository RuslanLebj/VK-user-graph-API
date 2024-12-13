from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# Загрузка переменных окружения (при локальном запуске)
load_dotenv()


class Settings(BaseSettings):
    """
    Класс для управления подключением к базе данных Neo4j.

    Этот класс обеспечивает создание единственного экземпляра подключения к Neo4j
    с использованием библиотеки py2neo. При первом вызове создается подключение,
    которое используется повторно при последующих вызовах.
    """
    AUTH_TOKEN: str

    NEO4J_BOLT_URL: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str

    class Config:
        env_file = "./docker/app/.env"


# Инициализация настроек
settings = Settings()