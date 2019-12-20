from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_birds(self, element: Birds) -> None:
        pass

    @abstractmethod
    def visit_others(self, element: Animal) -> None:
        pass
