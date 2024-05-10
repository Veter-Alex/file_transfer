# TODO написать докстринг к модулю
from fastapi import HTTPException, status


class FileTransferException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TaskNotFoundException(FileTransferException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Задачи не найдены"


class TaskNameAlreadyExistsException(FileTransferException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такое имя задачи уже существует"


class PathNotExistsException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Заданная директория отсутствует или не доступна"
