from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class To_dirs(Base):
    __tablename__ = "to_dirs"

    id = Column(Integer, primary_key=True)
    from_dirs_id = Column(Integer, ForeignKey("from_dirs.id"), nullable=False)
    path_to_dir = Column(String, nullable=False)
    is_backup_dir_not_copy_files = Column(Boolean, default=False)
    create_dir_day = Column(Boolean, default=False)
    create_dir_hour = Column(Boolean, default=False)
    create_dir_extension = Column(Boolean, default=False)
