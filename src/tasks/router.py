from fastapi import APIRouter
from tasks.dao import TaskDAO
from tasks.schemas import STask

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.get("")
async def get_all() -> list[STask]:
    """
    Получает список задач
    Args:
        task_id (int): id задачи

    Returns:
        list[STask]: список задач
    """
    return await TaskDAO.get_all()


@router.get("/{task_id}")
async def get_by_id(task_id: int) -> STask:
    """
    Получает задачу с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        STask: задача с заданным id
    """
    return await TaskDAO.get_one_or_none(id=task_id)


@router.post("")
async def add_task(
    title: str,
    task_enable: bool,
    check_interval: int,
    notes: str | None = None,
) -> STask:
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
    return await TaskDAO.add(
        title=title,
        task_enable=task_enable,
        check_interval=check_interval,
        notes=notes,
    )
