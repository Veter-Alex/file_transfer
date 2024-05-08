import datetime

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

    id: int
    operation: str = Field(default="")
    timestamp: datetime.datetime
    status_ok: bool = Field(default=True)

    class Config:
        orm_mode = True
