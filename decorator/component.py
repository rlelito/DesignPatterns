from abc import ABC
from abc import abstractmethod


class Component(ABC):
    @abstractmethod
    def print(self) -> None:
        pass
