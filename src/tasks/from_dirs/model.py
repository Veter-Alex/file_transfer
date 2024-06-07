from typing import Optional

from database import BaseModel, intpk, str_256
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class From_DirsORM(BaseModel):
    __tablename__ = "from_dirs"

    id: Mapped[intpk]
    tasks_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE")
    )
    path_from_dir: Mapped[str_256]
    del_after_copy: Mapped[bool] = mapped_column(default=False)
    del_not_copy_files: Mapped[bool] = mapped_column(default=False)
    backup_not_copy_files: Mapped[bool] = mapped_column(default=False)
    path_backup_dir_not_copy_files: Mapped[Optional[str_256]]
