from pathlib import Path

from pydantic import BaseModel, Field


class STo_Dir(BaseModel):
    """
    A data model representing a destination directory with its path.

    Args:
        path_to_dir (Path): The path to the destination directory.

    Returns:
        To_dir: An instance of the To_dir data model representing
            a destination directory.
    """

    id: int
    path_to_dir: Path
    create_dir_day: bool = Field(default=False)
    create_dir_hour: bool = Field(default=False)
    create_dir_extension: bool = Field(default=False)

    class Config:
        orm_mode = True
