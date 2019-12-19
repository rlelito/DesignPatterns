from figure import Figure
from library import Library


class Circle(Figure):
    def __init__(self, gl: Library, x: float, y: float, r: float) -> None:
        super().__init__(gl)
        self._x = x
        self._y = y
        self._r = r

    def draw(self) -> None:
        super().draw_circle(self._x, self._y, self._r)
