from abc import ABC
from abc import abstractmethod
from library import Library


class Figure(ABC):
    def __init__(self, gl: Library) -> None:
        self._gl = gl

    @abstractmethod
    def draw(self) -> None:
        pass

    def draw_line(self, x1: float, x2: float, y1: float, y2: float) -> None:
        self._gl.draw_line(x1, x2, y1, y2)

    def draw_circle(self, x: float, y: float, r: float) -> None:
        self._gl.draw_circle(x, y, r)
