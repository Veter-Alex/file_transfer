from dao.base import BaseDAO
from tasks.last_operations.model import Last_OperationsORM


class LastOperationsDAO(BaseDAO):
    model = Last_OperationsORM
