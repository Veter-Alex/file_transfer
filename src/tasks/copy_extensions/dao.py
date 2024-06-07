from dao.base import BaseDAO
from tasks.copy_extensions.model import Copy_ExtensionsORM


class CopyExtensionsDAO(BaseDAO):
    model = Copy_ExtensionsORM
