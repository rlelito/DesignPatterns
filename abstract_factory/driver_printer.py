from abc import ABC
from abc import abstractmethod


class PrinterDriver(ABC):
    @staticmethod
    @abstractmethod
    def print() -> None:
        pass
