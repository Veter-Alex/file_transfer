from dao.base import BaseDAO
from tasks.to_dirs.model import To_DirsORM


class ToDirsDAO(BaseDAO):
    model = To_DirsORM
