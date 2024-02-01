import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

from config import settings

# engine.connect() - делает подключение к БД () не делает COMMIT при выходе
#                  - commit надоделать явно: conn.commit()
# engine.begin() - делает подключение к БД () всегда делает COMMIT при выходе

# Созддаём синхронное подключение
sync_engine = create_engine(
    # f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    url=settings.DATABASE_URL_psycopg,
    # Выводит запросы в консоль
    echo=True,
    # Макс кол-во подключений
    # pool_size=5,
    # Макс кол-вл доп подключений
    # max_overflow=10,
)

# Созддаём aсинхронное подключение
async_engine = create_async_engine(
    # Просто используем асинхронную настройку
    url=settings.DATABASE_URL_asyncpg,
)

# Создаем синхронную и асинхронную сессии и передает туда движок
session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


# Base.metadata - это вместо MetaData()
class Base(DeclarativeBase):
    pass
