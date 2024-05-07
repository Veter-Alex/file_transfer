from fastapi import APIRouter
from tasks.dao import (
    FileExtensiontoCopyDAO,
    FromDirDAO,
    LastOperationDAO,
    TaskDAO,
    ToDirDAO,
)
from tasks.schemas import (
    SFile_extension_to_copy,
    SFrom_Dir,
    SLast_Operation,
    STask,
    STo_Dir,
)

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
async def get_by_id(task_id : int) -> STask:
    """
    Получает задачу с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        STask: задача с заданным id
    """
    return await TaskDAO.get_one_or_none(id=task_id)


@router.get("/{task_id}/from_dirs")
async def get_task_from_dirs(task_id: int) -> list[SFrom_Dir]:
    """
    Получает список исходных директории для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SFrom_Dir]: список исходных директорий для задачи с заданным id
    """
    return await FromDirDAO.get_all(task_id=task_id)


@router.get("/{task_id}/to_dirs")
async def get_task_to_dirs(task_id: int) -> list[STo_Dir]:
    """
    Получает список директории назначения для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SFrom_Dir]: список директорий назначения для задачи с заданным id
    """
    return await ToDirDAO.get_all(task_id=task_id)


@router.get("/{from_dir_id}/file_extension_to_copy")
async def get_file_extension_to_copy(from_dir_id: int) -> list[SFile_extension_to_copy]:
    """
    Получает список расширений для задачи с исходной директории с заданным id

    Args:
        from_dir_id (int): id исходной директории

    Returns:
        list[SFile_extension_to_copy]: список расширений для задачи с исходной директории с заданным id
    """
    return await FileExtensiontoCopyDAO.get_all(from_dir_id=from_dir_id)


@router.get("/{task_id}/last_operation")
async def get_last_operations(task_id: int) -> list[SLast_Operation] | None:
    """
    Получает последнюю операцию для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SLast_Operation]: последнюю операцию для задачи с заданным id
    """
    return await LastOperationDAO.get_one_or_none(task_id=task_id)
