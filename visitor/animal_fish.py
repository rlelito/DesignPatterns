from __future__ import annotations
from animal import Animal


class Fish(Animal):
    def __init__(self, health: bool, price: float) -> None:
        super().__init__("fish", health, price)

    def check(self, visitor: Visitor) -> None:
        return visitor.visit_others(self)
