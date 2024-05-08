from pydantic import BaseModel, Field


class STask(BaseModel):
    """
    A data model representing a task with an id, title, source directories,
        destination directories, task enable status, check interval,
        and optional notes.

    Args:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        from_dirs (list[From_dir]): The list of source directories
            for the task.
        to_dirs (list[Path]): The list of destination directories
            for the task.
        task_enable (bool): Flag indicating if the task is enabled.
        check_interval (int): The interval in seconds at which the task
            should be checked.
        notes (str | None): Additional notes for the task, if any.

    Returns:
        Task: An instance of the Task data model representing a task.
    """

    id: int
    title: str = Field(default="Task", min_length=1, max_length=15)
    task_enable: bool = Field(default=True)
    check_interval: int = Field(default=60, gt=0)
    notes: str | None = None

    class Config:
        orm_mode = True
