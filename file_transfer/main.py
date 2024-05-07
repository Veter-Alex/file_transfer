import datetime
from pathlib import Path
from typing import Any, Optional

import uvicorn
from database import tasks
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field
from tasks.router import router as tasks_router

app = FastAPI(
    title="File Transfer",
    description="File Transfer API",
    version="0.1.0",
)

app.include_router(tasks_router)


class Last_operation(BaseModel):
    """
    A data model representing the last operation performed on a task.

    Args:
        operation (str): The name of the last operation performed.
        timestamp (datetime.datetime): The timestamp of the last operation.

    Returns:
        Last_operation: An instance of the Last_operation data model
            representing the last operation performed on a task.
    """

    operation: str = Field(default="")
    timestamp: datetime.datetime
    status_ok: bool = Field(default=True)


class File_extension(BaseModel):
    """
    A data model representing a file extension with default values
        for extension type, minimum file size, and maximum file size.

    Args:
        extension (str): The file extension type.
        min_size_file (int): The minimum size in bytes
            for files with this extension.
        max_size_file (int): The maximum size in bytes
            for files with this extension.

    Returns:
        File_extension: An instance of the File_extension data model
            representing a file extension.
    """

    extension: str = Field(default="*", min_length=1, max_length=5)
    min_size_file: int = Field(default=10, gt=0)  # default 10 bits
    max_size_file: int = Field(default=104857600, gt=0)  # default 100 MB


class From_dir(BaseModel):
    """
    A data model representing a source directory with its path,
        supported file extensions, and an option to delete files after copying.

    Args:
        path_from_dir (Path): The path to the source directory.
        file_extensions (list[File_extension]): The list of supported
            file extensions in the directory.
        del_after_copy (bool): Flag indicating whether files should
            be deleted after copying.

    Returns:
        From_dir: An instance of the From_dir data model representing
            a source directory.
    """

    path_from_dir: Path
    file_extensions: list[File_extension]
    del_after_copy: bool = Field(default=False)


class To_dir(BaseModel):
    """
    A data model representing a destination directory with its path.

    Args:
        path_to_dir (Path): The path to the destination directory.

    Returns:
        To_dir: An instance of the To_dir data model representing
            a destination directory.
    """

    path_to_dir: Path
    create_dir_day: bool = Field(default=False)
    create_dir_hour: bool = Field(default=False)
    create_dir_extension: bool = Field(default=False)


class Task(BaseModel):
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
    from_dirs: list[From_dir]
    to_dirs: list[To_dir]
    task_enable: bool = Field(default=True)
    check_interval: int = Field(default=60, gt=0)
    last_operation: Last_operation | None = None
    notes: str | None = None


class Get_Tasks:
    def __init__(
        self,
        limit: int = Query(10, ge=0),
        offset: int = Query(0, ge=0),
        task_enable: Optional[bool] = False,
    ):
        self.limit = limit
        self.offset = offset
        self.task_enable = task_enable


@app.get("/tasks")
async def get_tasks(get_tasks: Get_Tasks = Depends()) -> list[Task]:
    if get_tasks.task_enable is False:
        return tasks[get_tasks.offset : get_tasks.offset + get_tasks.limit]
    else:
        return [
            task
            for index, task in enumerate(tasks)
            if task["task_enable"] == get_tasks.task_enable
            and index >= get_tasks.offset
            and index < get_tasks.offset + get_tasks.limit
        ]


@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> Task:
    return next((task for task in tasks if task["id"] == task_id), None)


@app.post("/tasks")
async def add_task(new_task: Task) -> dict[str, str | Task]:
    tasks.append(dict(new_task))
    return {"status": "success", "task": new_task}


@app.patch("/tasks")
async def task_update(task_update: Task) -> dict[str, str | Task]:
    for task in tasks:
        if task["id"] == task_update.id:
            task["title"] = task_update.title or task["title"]
            task["from_dirs"] = task_update.from_dirs or task["from_dirs"]
            task["to_dirs"] = task_update.to_dirs or task["to_dirs"]
            task["task_enable"] = (
                bool(task_update.task_enable)
                if task_update.task_enable
                else task["task_enable"]
            )
            task["check_interval"] = (
                task_update.check_interval or task["check_interval"]
            )
            task["last_operation"] = (
                task_update.last_operation or task["last_operation"]
            )
            task["notes"] = task_update.notes or task["notes"]
            break
    return {"status": "success", "task": task_update}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
