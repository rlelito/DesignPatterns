from library import Library
from gl1 import GL1


class LibraryV1(Library):
    @staticmethod
    def draw_line(x1: float, x2: float, y1: float, y2: float) -> None:
        GL1.draw_line(x1, x2, y1, y2)

    @staticmethod
    def draw_circle(x: float, y: float, r: float) -> None:
        GL1.draw_circle(x, y, r)
