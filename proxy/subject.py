from abc import ABC
from abc import abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self) -> str:
        pass
