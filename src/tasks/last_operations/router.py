from fastapi import APIRouter
from tasks.last_operations.dao import LastOperationsDAO
from tasks.last_operations.schemas import SLast_Operations

router = APIRouter(
    prefix="/tasks",
    tags=["Последняя операция"],
)


@router.get("/{task_id}/last_operation")
async def get_last_operations(task_id: int) -> list[SLast_Operations] | None:
    """
    Получает последнюю операцию для задачи с заданным id

    Args:
        task_id (int): id задачи

    Returns:
        list[SLast_Operation]: последнюю операцию для задачи с заданным id
    """
    return await LastOperationsDAO.get_one_or_none(task_id=task_id)
