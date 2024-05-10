from pydantic import BaseModel, Field


class SCopyExtensions(BaseModel):
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
