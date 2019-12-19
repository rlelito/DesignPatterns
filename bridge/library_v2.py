from library import Library
from gl2 import GL2


class LibraryV2(Library):
    @staticmethod
    def draw_line(x1: float, x2: float, y1: float, y2: float) -> None:
        GL2.drawing_line(x1, x2, y1, y2)

    @staticmethod
    def draw_circle(x: float, y: float, r: float) -> None:
        GL2.drawing_circle(x, y, r)
