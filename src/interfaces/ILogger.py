from abc import ABC, abstractmethod
from src.level_enum import Level


class ILogger(ABC):

    @abstractmethod
    def log(self, message: str, level: Level) -> None:
        pass