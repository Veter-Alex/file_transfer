from typing import Any

from exceptions import (
    TaskAddException,
    TaskEditException,
    TaskIdDeleteException,
    TaskIdNotFoundException,
    TaskNotFoundException,
)
from fastapi import APIRouter, Depends
from tasks.dao import TasksDAO
from tasks.schemas import STask, STask_add, STask_edit, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("/")
async def get_all() -> list[STask]:
    """
    Верни список задач.

    Returns:
        list[STask]: список задач

    Raises:
        TaskNotFoundException: прерывание если в базе данных нет ни одной задачи
    """
    result = await TasksDAO.get_all()
    if result == []:
        raise TaskNotFoundException(detail="Задачи в базе данных не найдены")
    return result


@router.get("/{task_id}")
async def get_task_by_id(task_id: int) -> STask:
    """
    Верни задачу с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        STask: задача с заданным id

    Raises:
        TaskIdNotFoundException: прерывание если задача с заданным id не найдена
    """
    result = await TasksDAO.get_one_or_none(id=task_id)
    if result is None:
        raise TaskIdNotFoundException(detail="Задача с заданным id не найдены")
    return result


@router.post("/")
async def add_task(task: STask_add = Depends()) -> STaskId:
    """
    Добавь задачу и верни id задачи в виде {"id": id}

    Args:
        task (STask): задача для добавления

    Returns:
        STaskId: {"id": id задачи}
    """
    result = await TasksDAO.add_one(
        title=task.title,
        is_run=task.is_run,
        check_interval=task.check_interval,
        notes=task.notes,
    )
    if result is None:
        raise TaskAddException(detail="Ошибка при добавлении задачи")
    return {"id": result}


@router.put("/")
async def update_task(
    task_id: int, task_edit: STask_edit = Depends()
) -> STaskId:
    """
    Измени задачу и верни id задачи в виде {"id": id}

    Args:
        task_id (int): id задачи
        task_edit (STask_edit): поля для редактирования

    Returns:
        STaskId: id задачи
    """
    update_data = task_edit.model_dump(exclude_unset=True, exclude_none=True)
    result = await TasksDAO.update_one(id=task_id, **update_data)
    if result is None:
        raise TaskEditException(detail="Ошибка при редактировании задачи")
    return {"id": result}


@router.delete("/{task_id}")
async def del_task(task_id: int) -> STaskId:
    """
    Удали задачу с заданным id и верни статус выполнения

    Args:
        task_id (int): id задачи

    Returns:
        str: сообщение об успешном удалении

    Raises:
        TaskIdNotFoundException: Если возникла ошибка при удалении задачи
    """
    result = await TasksDAO.del_one(id=task_id)
    if result is None:
        raise TaskIdDeleteException(detail="Ошибка при удалении задачи")
    return {"id": result}
