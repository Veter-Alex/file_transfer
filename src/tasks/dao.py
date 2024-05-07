from dao.base import BaseDAO
from tasks.model import (
    File_extension_to_copy,
    From_dir,
    Last_operation,
    Tasks,
    To_dir,
)


class TaskDAO(BaseDAO):
    model = Tasks


class FileExtensiontoCopyDAO(BaseDAO):
    model = File_extension_to_copy


class FromDirDAO(BaseDAO):
    model = From_dir


class ToDirDAO(BaseDAO):
    model = To_dir


class LastOperationDAO(BaseDAO):
    model = Last_operation
