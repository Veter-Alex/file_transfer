from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class From_dir(Base):
    """Класс From_dir представляет собой модель SQLAlchemy,
        которая представляет таблицу в базе данных. У нее есть следующие поля:

    Арgs:
        task_id (int): идентификатор задачи, к которой привязан источник.
            ForeignKey на таблицу tasks.
        path_from_dir (str): путь к директории, из которой будут
            забираться файлы.
        del_after_copy (bool): удалять ли файлы после копирования
            (по умолчанию - не удалять).
        del_not_copy_files (bool): удалять ли файлы,
            которые не будут скопированы (по умолчанию - не удалять).
        backup_not_copy_files (bool): делать ли резервную копию файлов,
            которые не будут скопированы (по умолчанию - не делать).
        backup_dir_not_copy_files (str): директория для резервной копии файлов,
            которые не будут скопированы (по умолчанию - не задана).
            (например: /home/user/backup).
        create_dir_day_not_copy_files (bool): создавать ли поддиректорию
            в директории резервной копии файлов,
            которые не будут скопированы по дню (по умолчанию - не создавать).
            (например: /home/user/backup/2022/01/22).
        create_dir_hour_not_copy_files (bool): создавать ли поддиректорию
            в директории резервной копии файлов,
            которые не будут скопированы по часу (по умолчанию - не создавать).
            (например: /home/user/backup/2022/01/22/13).
        create_dir_extension_not_copy_files (bool): создавать ли поддиректорию
            в директории резервной копии файлов,
            которые не будут скопированы по расширению (по умолчанию - не создавать).
            (например: /home/user/backup/2022/01/22/13/txt).
    """

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
