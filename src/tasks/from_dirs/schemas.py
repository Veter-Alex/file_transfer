from pathlib import Path

from pydantic import BaseModel, Field


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

    id: int
    path_from_dir: Path
    del_after_copy: bool = Field(default=False)

    class Config:
        orm_mode = True


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

    id: int
    extension: str = Field(default="*", min_length=1, max_length=5)
    min_size_file: int = Field(default=10, ge=0)  # default 10 bits
    max_size_file: int = Field(default=104857600, gt=0)  # default 100 MB

    class Config:
        orm_mode = True
