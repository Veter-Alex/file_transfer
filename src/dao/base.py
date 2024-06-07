from typing import Any, Dict

from database import async_session_maker
from exceptions import (
    TaskAddException,
    TaskIdDeleteException,
    TaskIdNotFoundException,
    TaskNotFoundException,
)
from sqlalchemy import delete, insert, select, update


class BaseDAO:
    model = None

    @classmethod
    async def get_one_or_none(cls, **filter_by: Dict[str, Any]) -> list[Any]:
        async with async_session_maker() as session:
            return await session.get(cls.model, filter_by)

    @classmethod
    async def get_all(cls, **filter_by: Dict[str, Any]) -> list[Any]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add_one(cls, **data: Dict[str, Any]) -> int:
        async with async_session_maker() as session:
            new_item = cls.model(**data)
            session.add(new_item)
            await session.commit()
            return new_item.id

    # TODO разобраться с методом update
    @classmethod
    async def update_one(cls, id: int, **update_by: Dict[str, Any]) -> int:
        async with async_session_maker() as session:
            stmt = (
                update(cls.model).where(cls.model.id == id).values(**update_by)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount

    @classmethod
    async def del_one(cls, **filter_by: Dict[str, Any]) -> int:
        async with async_session_maker() as session:
            if not cls.model:
                raise ValueError("Model is not set")
            stmt = (
                delete(cls.model)
                .where(cls.model.id == filter_by["id"])
                .returning(cls.model.id)
            )
            try:
                result = await session.execute(stmt)
                await session.commit()
                deleted_id = result.scalar_one()
            except (AttributeError, NoResultFound) as e:
                raise TaskIdNotFoundException(
                    f"No row found for model {cls.model.__name__} with filter_by {filter_by}"
                ) from e
            return deleted_id
