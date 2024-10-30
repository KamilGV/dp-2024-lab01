from datetime import datetime
import pathlib
import threading

from src.enums.level_enum import Level
from src.interfaces import ILogger


class Logger(ILogger):
    """
    Класс для управления логированием сообщений

    Атрибуты:
        _instance: Экземпляр логгера, который используется для записи сообщений.

    Методы:
        log(level, message): Записывает сообщение с заданным уровнем.
    """

    _instance = None
    _file_path = None
    _mutex_create = threading.Lock()
    _mutex_write = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._mutex_create:
            if not cls._instance:
                cls._instance = super().__new__(cls)

            return cls._instance

    def __init__(self, dir_path: pathlib.Path = None):
        if dir_path is None:
            raise Exception("Не задан путь к директории.")
        with self._mutex_create:
            if not self._file_path:
                self._create_file(dir_path=dir_path)

    def _create_file(self, dir_path: str):
        """
        Метод для формирования пути до файла для записи логов.

        :param dir_path: Путь к директории.
        :return: None.
        """
        time = datetime.now().strftime("%yyyy-%m-%d-%H-%M-%S")
        file_name = f"DP.P1.{time}.log"
        file_path = dir_path / file_name
        self._file_path = file_path

    def log(self, message: str, level: Level) -> None:
        """
        Метод для записи лога.

        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: None.
        """
        with self._mutex_write:
            row = self._genetare_log(message=message, level=level)
            with open(self._file_path, "a") as f:
                f.write(f"{row}\n")

    def _genetare_log(self, message: str, level: Level):
        """
        Метод для формирования строки лога.

        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: Строка лога.
        """
        time = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        return f"{time} [{level.value}] {message}"
