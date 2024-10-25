import pathlib
import threading
from datetime import datetime

from src.enums.level_enum import Level
from src.interfaces import ILogger


mutex_create = threading.Lock()
mutex_write = threading.Lock()


class Logger(ILogger):
    """
    Класс для управления логированием сообщений

    Атрибуты:
        _instance: Экземпляр логгера, который используется для записи сообщений.

    Методы:
        log(level, message): Записывает сообщение с заданным уровнем.
    """
    _instance = None

    def __new__(cls, dir_path: pathlib.Path = None):
        with mutex_create:
            if not cls._instance:
                time = datetime.now().strftime("%yyyy-%m-%d-%H-%M-%S")
                file_name = f"DP.P1.{time}.log"
                file_path = dir_path / file_name
                cls._instance = super().__new__(cls)
                cls._instance.file_path = file_path

            return cls._instance

    def log(self, message: str, level: Level) -> None:
        """Принимает сообщение с уровенем логгирования и запысывает в файл."""
        with mutex_write:
            time = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
            with open(self.file_path, 'a') as f:
                f.write(f"{time} [{level.value}] {message}\n")