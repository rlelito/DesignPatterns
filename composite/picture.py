from graphic import Graphic


class Picture(Graphic):
    def __init__(self) -> None:
        self._graphics: list = []

    def draw(self) -> None:
        for g in self._graphics:
            g.draw()

    def add(self, item: Graphic) -> None:
        self._graphics.append(item)

    def remove(self, item: Graphic) -> None:
        self._graphics.remove(item)

    def get_child(self, index: int) -> None:
        return self._graphics[index]
