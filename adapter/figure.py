from abc import ABC, abstractmethod


class Figure(ABC):
    def get_position(self) -> None:
        pass

    def set_position(self) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def fill(self) -> None:
        pass

    def set_color(self) -> None:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass
