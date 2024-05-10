from fastapi import APIRouter
from tasks.to_dirs.dao import ToDirsDAO
from tasks.to_dirs.schemas import STo_Dirs

router = APIRouter(
    prefix="/tasks",
    tags=["Выходные директории"],
)


@router.get("/{task_id}/to_dirs")
async def get_task_to_dirs(task_id: int) -> list[STo_Dirs]:
    """
    Получает список директории назначения для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SFrom_Dir]: список директорий назначения для задачи с заданным id
    """
    return await ToDirsDAO.get_all(task_id=task_id)
