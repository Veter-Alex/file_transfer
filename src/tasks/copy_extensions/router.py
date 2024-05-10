from fastapi import APIRouter
from tasks.copy_extensions.dao import CopyExtensionsDAO
from tasks.copy_extensions.schemas import SCopyExtensions

router = APIRouter(
    prefix="/tasks",
    tags=["Расширение для копирования"],
)


@router.get("/{from_dir_id}/file_extension_to_copy")
async def get_file_extension_to_copy(
    from_dir_id: int,
) -> list[SCopyExtensions]:
    """
    Получает список расширений для задачи с исходной директории с заданным id

    Args:
        from_dir_id (int): id исходной директории

    Returns:
        list[SFile_extension_to_copy]: список расширений для задачи
            с исходной директории с заданным id
    """
    return await CopyExtensionsDAO.get_all(from_dir_id=from_dir_id)
