from abc import ABC
from abc import abstractmethod


class Library(ABC):
    @staticmethod
    @abstractmethod
    def draw_line(x1: float, x2: float, y1: float, y2: float) -> None:
        pass

    @staticmethod
    @abstractmethod
    def draw_circle(x: float, y: float, r: float) -> None:
        pass
