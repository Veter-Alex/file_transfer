from typing import Optional

from database import BaseModel, created_at, intpk, str_50, str_256, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TasksORM(BaseModel):
    """Класс Tasks представляет собой модель SQLAlchemy,
    которая представляет таблицу в базе данных. У нее есть следующие поля:

    Атрибуты:
        id: (int), идентификатор задачи.
        title: (str), название задачи.
        is_run: (bool), ключ - статус активности задачи.
        check_interval: (int), интервал выполнения задачи в секундах.
        notes: (str), строка с дополнительными заметками по задаче.
    """

    __tablename__ = "tasks"

    id: Mapped[intpk]
    title: Mapped[str_50] = mapped_column(unique=True)
    is_run: Mapped[bool] = mapped_column(default=False)
    check_interval: Mapped[int] = mapped_column(default=60)
    notes: Mapped[Optional[str_256]]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
