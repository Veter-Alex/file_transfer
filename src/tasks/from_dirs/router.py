from fastapi import APIRouter
from tasks.from_dirs.dao import FileExtensiontoCopyDAO, FromDirDAO
from tasks.from_dirs.schemas import SFile_extension_to_copy, SFrom_Dir

router = APIRouter(
    prefix="/tasks",
    tags=["Входные директории"],
)


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


@router.get("/{from_dir_id}/file_extension_to_copy")
async def get_file_extension_to_copy(
    from_dir_id: int,
) -> list[SFile_extension_to_copy]:
    """
    Получает список расширений для задачи с исходной директории с заданным id

    Args:
        from_dir_id (int): id исходной директории

    Returns:
        list[SFile_extension_to_copy]: список расширений для задачи с исходной директории с заданным id
    """
    return await FileExtensiontoCopyDAO.get_all(from_dir_id=from_dir_id)
