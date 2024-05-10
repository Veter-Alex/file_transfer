from dao.base import BaseDAO
from tasks.to_dirs.model import To_dirs


class ToDirsDAO(BaseDAO):
    model = To_dirs
