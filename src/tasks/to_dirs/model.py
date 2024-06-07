from database import BaseModel, intpk, str_256
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column


class To_DirsORM(BaseModel):
    __tablename__ = "to_dirs"

    id: Mapped[intpk]
    from_dirs_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("from_dirs.id", ondelete="CASCADE"), nullable=False
    )
    path_to_dir: Mapped[str_256]
    is_backup_dir_not_copy_files: Mapped[bool] = mapped_column(default=False)
    create_dir_day: Mapped[bool] = mapped_column(default=False)
    create_dir_hour: Mapped[bool] = mapped_column(default=False)
    create_dir_extension: Mapped[bool] = mapped_column(default=False)
