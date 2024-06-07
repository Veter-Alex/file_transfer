from dao.base import BaseDAO
from database import async_session_maker
from sqlalchemy import insert
from tasks.model import TasksORM


class TasksDAO(BaseDAO):
    model = TasksORM
