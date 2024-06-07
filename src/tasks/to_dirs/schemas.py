from pathlib import Path

from pydantic import BaseModel, Field


class STo_Dirs(BaseModel):
    """
    A data model representing a destination directory with its path.

    Args:
        path_to_dir (Path): The path to the destination directory.

    Returns:
        To_dir: An instance of the To_dir data model representing
            a destination directory.
    """

    id: int
    from_dirs_id: int
    path_to_dir: str
    is_backup_dir_not_copy_files: bool
    create_dir_day: bool
    create_dir_hour: bool
    create_dir_extension: bool

    class Config:
        orm_mode = True
