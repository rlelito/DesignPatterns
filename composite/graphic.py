from abc import ABC
from abc import abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass

    def add(self, item) -> None:
        pass

    def remove(self, item) -> None:
        pass

    def get_child(self, index: int) -> None:
        pass
