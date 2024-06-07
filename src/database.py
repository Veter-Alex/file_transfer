"""
Модуль для настройки базы данных.

"""

import datetime
from typing import Annotated

from config import settings
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.pool import AsyncAdaptedQueuePool

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    poolclass=AsyncAdaptedQueuePool,
    future=True,
)
""" Асинхронное подключение,
которое будет отвечать за отправку запросов в базу данных engine.
"""

async_session_maker = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    future=True,
)
"""Фабрика сессий
"""

str_256 = Annotated[str, 256]
"""Аннотация строки в 256 символов
для использования в моделях SQLAlchemy ( Annotated[str, 256] )
"""
str_50 = Annotated[str, 50]
"""Аннотация строки в 256 символов
для использования в моделях SQLAlchemy
( Annotated[str, 50] )
"""
intpk = Annotated[int, mapped_column(primary_key=True)]
"""Аннотация поля id (PrimaryKey)
для использования в моделях SQLAlchemy
( Annotated[int, mapped_column(primary_key=True)] )
"""
created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
"""Аннотация поля создание записи (created_at)
и автоматическом назначении текущей даты и времени
для использования в моделях SQLAlchemy
( Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
  ]  )
"""

updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=text("TIMEZONE('utc', now())"),
        # onupdate=datetime.datetime.now(datetime.timezone.utc),
    ),
]
"""Аннотация поля обновления записи (updated_at)
и автоматическом назначении текущей даты и времени
для использования в моделях SQLAlchemy
( updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
    ),
] )
"""


class BaseModel(DeclarativeBase):
    """Базовый класс для наследования в моделях.
    Соответствует одной таблице в базе данных.

    Args:
        DeclarativeBase (_type_): класс Pydantic
    """

    pass
