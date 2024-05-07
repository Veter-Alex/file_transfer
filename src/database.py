from config import settings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import AsyncAdaptedQueuePool

async_engine = create_async_engine(
    settings.DATABASE_URL, poolclass=AsyncAdaptedQueuePool, future=True
)

async_session_maker = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False, future=True
)


class Base(DeclarativeBase):
    pass
