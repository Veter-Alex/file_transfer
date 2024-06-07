from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class STask_edit(BaseModel):
    """Cхема Pydantic для валидации данных
    при редактировании задачи.

    Attributes:
        title (str): Название задачи,
            не может превышать 50 символов
        is_run (bool): Активация задачи
        check_interval (int): Интервал проверки задачи,
            должен быть больше 0
        notes (str, optional): Примечание к задаче

    Args:
        BaseModel (_type_): специальный класс Pydantic
    """

    title: str | None = Field(
        None, min_length=1, max_length=50, description="Название задачи"
    )
    is_run: bool | None = Field(None, description="Активация задачи")
    check_interval: int | None = Field(
        None, gt=0, description="Интервал проверки задачи"
    )
    notes: str | None = Field(None, description="Примечание к задаче")


class STask_add(BaseModel):
    """Cхема Pydantic для валидации данных
    при добавлении новой задачи.

    Attributes:
        title (str): Название задачи,
            не может быть пустым,
            не может превышать 50 символов
        is_run (bool): Активация задачи,
            по умолчанию задача неактивна
        check_interval (int): Интервал проверки задачи,
            должен быть больше 0
        notes (str, optional): Примечания к задаче

    Args:
        BaseModel (_type_): специальный класс Pydantic
    """

    title: str = Field(
        min_length=1, max_length=50, description="Название задачи"
    )
    is_run: bool = Field(default=False, description="Активация задачи")
    check_interval: int = Field(gt=0, description="Интервал проверки задачи")
    notes: str | None = Field(None, description="Примечания к задаче")

    class Config:
        """
        Настройки для работы с ORM
        """

        orm_mode = True


class STaskId(BaseModel):
    """
    Cхема Pydantic для валидации данных,
    которая будет отображать возвращаемый ответ функции
    add_task.

    Attributes:
        id (int): Идентификатор задачи в БД

    Args:
        BaseModel (_type_): специальный класс Pydantic
    """

    id: int

    class Config:
        """
        Настройки для работы с ORM
        """

        orm_mode = True


class STask(STask_add):
    """Cхема Pydantic для валидации данных
    при запросе данных о задачи из БД.

    Attributes:
        id (int): Идентификатор задачи в БД

    Extends:
        STask_add: наследуемся от класса STasks_add и добавляем id
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """
        Настройки для работы с ORM
        """

        orm_mode = True
