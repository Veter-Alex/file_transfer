import datetime
from pathlib import Path

from pydantic import BaseModel, Field


class SLast_Operation(BaseModel):
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


class SFile_extension_to_copy(BaseModel):
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
    min_size_file: int = Field(default=10, ge=0)  # default 10 bits
    max_size_file: int = Field(default=104857600, gt=0)  # default 100 MB


class SFrom_Dir(BaseModel):
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
    del_after_copy: bool = Field(default=False)


class STo_Dir(BaseModel):
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
