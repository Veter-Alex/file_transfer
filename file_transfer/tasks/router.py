from fastapi import APIRouter

router = APIRouter(
    prefix="/taskss",
    tags=["Задачи"],
)


@router.get("")
def get_tasks() -> None:
    pass


@router.get("/{task_id}")
def get_task_id(task_id: int) -> None:
    pass
