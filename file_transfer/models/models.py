from datetime import datetime, timezone

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(15), nullable=False),
    Column("task_enable", Integer),
    Column("check_interval", Integer),
    Column("last_operation_id", ForeignKey("last_operation.id")),
    Column("notes", String(255)),
)

from_dirs = Table(
    "from_dirs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task_id", ForeignKey("tasks.id")),
    Column("path_from_dir", String(255)),
    Column("file_extensions", String(255)),
    Column("del_after_copy", Integer),
)

to_dirs = Table(
    "to_dirs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task_id", ForeignKey("tasks.id")),
    Column("path_to_dir", String(255)),
    Column("create_dir_day", Integer, default=0),
    Column("create_dir_hour", Integer, default=0),
    Column("create_dir_extension", Integer, default=0),
)

file_extensions = Table(
    "file_extensions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("from_dir_id", ForeignKey("from_dirs.id")),
    Column("extension", String(255)),
    Column("min_size_file", Integer),
    Column("max_size_file", Integer),
)

last_operation = Table(
    "last_operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("operation", String(255)),
    Column("timestamp", TIMESTAMP, default=datetime.now(timezone.utc)),
    Column("status_ok", Integer),
)
