from fastapi import APIRouter
from tasks.dao import TasksDAO
from tasks.schemas import STasks

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("")
async def get_all() -> list[STasks]:
    """
    Получает список задач
    Args:
        task_id (int): id задачи

    Returns:
        list[STask]: список задач
    """
    result = await TasksDAO.get_all()
    if result == []:
        pass
    else:
        return result


@router.get("/{task_id}")
async def get_by_id(task_id: int) -> STasks:
    """
    Получает задачу с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        STask: задача с заданным id
    """
    return await TasksDAO.get_one_or_none(id=task_id)


@router.post("")
async def add_task(
    title: str,
    task_enable: bool,
    check_interval: int,
    notes: str | None = None,
):
    """
    Создает задачу

    Args:
        title (str): название задачи
        task_enable (bool): состояние задачи
        check_interval (int): интервал проверки задачи
        notes (str | None): заметки

    Returns:
        STask: созданная задача
    """
    result = await TasksDAO.add_task(
        title=title,
        task_enable=task_enable,
        check_interval=check_interval,
        notes=notes,
    )
    return result
