from database import BaseModel, intpk, str_50
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Copy_ExtensionsORM(BaseModel):
    __tablename__ = "copy_extensions"

    id: Mapped[intpk]
    from_dirs_id: Mapped[int] = mapped_column(
        ForeignKey("from_dirs.id", ondelete="CASCADE")
    )
    extension: Mapped[str_50]
    min_size_file: Mapped[int] = mapped_column(default=1)
    max_size_file: Mapped[int] = mapped_column(default=104857600)
