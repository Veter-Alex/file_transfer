from fastapi import APIRouter
from tasks.from_dirs.dao import FromDirsDAO
from tasks.from_dirs.schemas import SFrom_Dirs

router = APIRouter(
    prefix="/tasks",
    tags=["Входные директории"],
)


@router.get("/{task_id}/from_dirs")
async def get_task_from_dirs(task_id: int) -> list[SFrom_Dirs]:
    """
    Получает список исходных директории для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SFrom_Dir]: список исходных директорий для задачи с заданным id
    """
    return await FromDirsDAO.get_all(task_id=task_id)
