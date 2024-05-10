from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Tasks(Base):
    """Класс Tasks представляет собой модель SQLAlchemy,
    которая представляет таблицу в базе данных. У нее есть следующие поля:

    Атрибуты:
        id: (int), идентификатор задачи.
        title: (str), название задачи.
        task_enable: (bool), ключ - статус активации задачи.
        check_interval: (int), интервал выполнения задачи в секундах.
        notes: (str), строка с дополнительными заметками по задаче.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    task_enable = Column(Boolean, nullable=True)
    check_interval = Column(Integer, default=60)
    notes = Column(String, nullable=True)
