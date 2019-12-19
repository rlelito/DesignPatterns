from figure import Figure
from library import Library


class Rectangle(Figure):
    def __init__(self, gl: Library, x1: float, x2: float, y1: float, y2: float) -> None:
        super().__init__(gl)
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def draw(self) -> None:
        for i in range(0, 4):
            super().draw_line(self._x1, self._x2, self._y1, self._y2)
