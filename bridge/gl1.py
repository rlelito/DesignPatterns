class GL1(object):
    @staticmethod
    def draw_line(x1: float, x2: float, y1: float, y2: float) -> None:
        print(f"Drawing line using graphic library GL1."
              f"\t(x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2})")

    @staticmethod
    def draw_circle(x: float, y: float, r: float) -> None:
        print(f"Drawing circle using graphic library GL1."
              f"\t(x: {x}, y: {y}, r: {r})")
