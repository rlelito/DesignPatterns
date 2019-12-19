from abc import ABC
from abc import abstractmethod


class DataBase(ABC):
    @staticmethod
    @abstractmethod
    def execute_select(spec_query: str) -> None:
        pass
