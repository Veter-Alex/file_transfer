from pathlib import Path

from config import settings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import AsyncAdaptedQueuePool

async_engine = create_async_engine(
    settings.DATABASE_URL, poolclass=AsyncAdaptedQueuePool, future=True
)

async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False, future=True
)


class Base(DeclarativeBase):
    pass


tasks = [
    {
        "id": 1,
        "title": "Task 1",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 2,
        "title": "Task 2",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": False,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 3,
        "title": "Task 3",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": True,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
    {
        "id": 4,
        "title": "Task 4",
        "from_dirs": [
            {
                "path_from_dir": Path("/data"),
                "file_extensions": [
                    {
                        "extension": "txt",
                        "min_size_file": 10,
                        "max_size_file": 104857600,
                    }
                ],
                "del_after_copy": False,
            }
        ],
        "to_dirs": [
            {
                "path_to_dir": Path("/data"),
                "create_dir_day": False,
                "create_dir_hour": False,
                "create_dir_extension": False,
            }
        ],
        "task_enable": False,
        "check_interval": 60,
        "last_operation": None,
        "notes": None,
    },
]
