"""
Модуль с исключениями.
"""

from fastapi import HTTPException, status


class FileTransferException(HTTPException):
    status_code = 500
    detail = "Ошибка сервера (значение по умолчанию)"

    def __init__(self, **kwargs: dict) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)


class TaskNotFoundException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Задачи в базе данных не найдены"


class TaskIdNotFoundException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Задача с заданным id в базе данных не найдена"


class TaskAddException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ошибка при добавлении задачи"


class TaskEditException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ошибка при редактировании задачи"


class TaskIdDeleteException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ошибка при удалении задачи"


class TaskNameAlreadyExistsException(FileTransferException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такое имя задачи уже существует"


class PathNotExistsException(FileTransferException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Заданная директория отсутствует или не доступна"
