from abc import ABC
from abc import abstractmethod


class ScreenDriver(ABC):
    @staticmethod
    @abstractmethod
    def show() -> None:
        pass
