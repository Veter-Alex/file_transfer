import datetime
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="File Transfer",
    description="File Transfer API",
    version="0.1.0",
)


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


class Tasks(BaseModel):
    """
    A data model representing a task with an id, title, source directories,
        destination directories, task enable status, check interval, and optional notes.

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
        Tasks: An instance of the Tasks data model representing a task.
    """

    id: int
    title: str = Field(default="Task", min_length=1, max_length=15)
    from_dirs: list[From_dir]
    to_dirs: list[To_dir]
    task_enable: bool = Field(default=True)
    check_interval: int = Field(default=60, gt=0)
    last_operation: Last_operation | None = None
    notes: str | None = None


tasks = [
    {
        "id": 1,
        "title": "Task 1",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 2,
        "title": "Task 2",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 3,
        "title": "Task 3",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 4,
        "title": "Task 4",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
]


@app.get("/tasks", response_model=list[Tasks])
async def get_tasks(limit: int = 5, offset: int = 0) -> list[Tasks]:
    return tasks[offset:][:limit]


@app.get("/tasks/{task_id}", response_model=list[Tasks])
async def get_task(task_id: int) -> list[Tasks]:
    return [task for task in tasks if task.get("id") == task_id]


@app.post("/tasks")
async def add_tasks(new_tasks: list[Tasks]):
    tasks.extend(new_tasks)
    return {"status": "success", "tasks": tasks}


@app.post("/tasks/{task_id}")
async def update_task(
    task_id: int,
    title: str,
    from_dirs: str,
    to_dirs: str,
    task_enable: bool,
    check_interval: int,
):
    task = [task for task in tasks if task.get("id") == task_id][0]
    task.update(
        {
            "title": title,
            "from_dirs": from_dirs,
            "to_dirs": to_dirs,
            "task_enable": task_enable,
            "check_interval": check_interval,
        }
    )
    return {"status": "success", "task": task}
