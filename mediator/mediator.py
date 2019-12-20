from abc import ABC
from abc import abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass
