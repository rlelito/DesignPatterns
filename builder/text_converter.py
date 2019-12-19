from abc import ABC
from abc import abstractmethod
from typing import Tuple


class TextConverter(ABC):
    @staticmethod
    @abstractmethod
    def convert_character(character: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def convert_tag(tag: Tuple[str, str]) -> str:
        pass

    def __str__(self):
        return self.__class__.__name__
