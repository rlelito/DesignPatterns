from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass
