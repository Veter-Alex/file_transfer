import datetime
from typing import Literal

from pydantic import BaseModel, Field


class SLast_Operations(BaseModel):
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
    tasks_id: int
    operation: Literal["backup", "copy", "move", "delete"]
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)
    status_ok: bool

    class Config:
        orm_mode = True
