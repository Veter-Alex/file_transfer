from typing import Any, Dict

from database import async_session_maker
from sqlalchemy import insert, select


class BaseDAO:
    model = None

    @classmethod
    async def get_one_or_none(cls, **filter_by: Dict[str, Any]) -> list[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by: Dict[str, Any]) -> list[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    # @classmethod
    # async def add(cls, **data):
    #     async with async_session_maker() as session:
    #         query = insert(cls.model).values(**data)
    #         await session.execute(query)
    #         await session.commit()

    # @classmethod
    # async def del_one(cls, **filter_by: Dict[str, Any]) -> (str, int):
    #     async with async_session_maker() as session:
    #         query = select(cls.model).filter_by(**filter_by)
    #         result = await session.execute(query)
    #         return ("Ok")
