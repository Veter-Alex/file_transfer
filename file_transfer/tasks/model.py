from file_transfer.database import Base
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    task_enable = Column(Boolean, nullable=True)
    check_interval = Column(Integer, default=60)
    notes = Column(String)


class Last_operation(Base):
    __tablename__ = "last_operation"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    operation = Column(String)
    timestamp = Column(DateTime)
    status_ok = Column(Boolean)


class To_dir(Base):
    __tablename__ = "to_dir"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    path_to_dir = Column(String, nullable=False)
    create_dir_day = Column(Boolean, default=False)
    create_dir_hour = Column(Boolean, default=False)
    create_dir_extension = Column(Boolean, default=False)


class From_dir(Base):
    __tablename__ = "from_dir"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    path_from_dir = Column(String, nullable=False)
    del_after_copy = Column(Boolean, default=False)
    del_not_copy_files = Column(Boolean, default=False)
    backup_not_copy_files = Column(Boolean, default=False)
    backup_dir_not_copy_files = Column(String, nullable=True)
    create_dir_day_not_copy_files = Column(Boolean, default=False)
    create_dir_hour_not_copy_files = Column(Boolean, default=False)
    create_dir_extension_not_copy_files = Column(Boolean, default=False)


class File_extension_to_copy(Base):
    __tablename__ = "file_extension"

    id = Column(Integer, primary_key=True)
    from_dir_id = Column(Integer, ForeignKey("from_dir.id"), nullable=False)
    extension = Column(String, nullable=False)
    min_size_file = Column(Integer, nullable=False)
    max_size_file = Column(Integer, nullable=False)
