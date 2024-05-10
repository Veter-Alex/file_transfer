from dao.base import BaseDAO
from tasks.last_operations.model import Last_operations


class LastOperationsDAO(BaseDAO):
    model = Last_operations
