from figure import Figure
from xx_square import XxCircle


class Circle(Figure):
    _xx_circle: XxCircle = XxCircle()

    def get_position(self) -> None:
        self._xx_circle.get_position()

    def set_position(self) -> None:
        self._xx_circle.set_position()

    def show(self) -> None:
        self._xx_circle.show_circle()

    def fill(self) -> None:
        self._xx_circle.fill_circle()

    def set_color(self) -> None:
        self._xx_circle.give_color()

    def remove(self) -> None:
        self._xx_circle.remove_circle()
