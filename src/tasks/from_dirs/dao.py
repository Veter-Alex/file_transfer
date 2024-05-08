from dao.base import BaseDAO
from tasks.from_dirs.model import File_extension_to_copy, From_dir


class FromDirDAO(BaseDAO):
    model = From_dir


class FileExtensiontoCopyDAO(BaseDAO):
    model = File_extension_to_copy
