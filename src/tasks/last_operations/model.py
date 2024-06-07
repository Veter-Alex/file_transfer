import enum
from database import BaseModel, created_at, intpk, str_50
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Operations_List(enum.Enum):
    copy = "copy"
    move = "move"
    backup = "backup"
    delete = "delete"

class Last_OperationsORM(BaseModel):
    __tablename__ = "last_operations"

    id: Mapped[intpk]
    tasks_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE")
    )
    operation: Mapped[Operations_List]
    timestamp: Mapped[created_at]
    status_ok: Mapped[bool]
