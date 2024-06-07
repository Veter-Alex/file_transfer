from dao.base import BaseDAO
from tasks.from_dirs.model import From_DirsORM


class FromDirsDAO(BaseDAO):
    model = From_DirsORM
