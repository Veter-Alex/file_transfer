from pathlib import Path

from pydantic import BaseModel, Field


class SFrom_Dirs(BaseModel):
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

    id: int
    tasks_id: int
    path_from_dir: str
    del_after_copy: bool
    del_not_copy_files: bool
    backup_not_copy_files: bool
    path_backup_dir_not_copy_files: str | None

    class Config:
        orm_mode = True
