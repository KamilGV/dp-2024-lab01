from abc import ABC, abstractmethod

from src.enums.level_enum import Level


class ILogger(ABC):
    """
    Интерфейс для управления логированием сообщений

        Методы:
        log(level, message): Записывает сообщение с заданным уровнем.
    """
    @abstractmethod
    def log(self, message: str, level: Level) -> None:
        """Метод, который принимает сообщение с уровенем логгирования и запысывает данные."""
        pass
