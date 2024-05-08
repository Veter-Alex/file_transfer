from dao.base import BaseDAO
from tasks.model import Tasks


class TaskDAO(BaseDAO):
    model = Tasks
