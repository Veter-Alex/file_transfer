from dao.base import BaseDAO
from tasks.model import Tasks
from database import async_session_maker
from sqlalchemy import insert


class TasksDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def add_task(
        cls,
        title: str,
        task_enable: bool,
        check_interval: int,
        notes: str,
    ) -> Tasks.id:
        async with async_session_maker() as session:
            add_task = insert(cls.model).values(
                title=title,
                task_enable=task_enable,
                check_interval=check_interval,
                notes=notes,
            ).returning(Tasks.id)
            new_task = await session.execute(add_task)
            await session.commit()
            result = new_task.one_or_none()
            return result
