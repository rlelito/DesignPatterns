from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, species: str, health: bool, price: float) -> None:
        self._species: str = species
        self._health: bool = health
        self._price: float = price

    @abstractmethod
    def check(self, visitor: Visitor) -> None:
        pass

    @property
    def health(self) -> bool:
        return self._health

    @property
    def price(self) -> float:
        return self._price
