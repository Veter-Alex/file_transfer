from dao.base import BaseDAO
from tasks.last_operations.model import Last_operation


class LastOperationDAO(BaseDAO):
    model = Last_operation
