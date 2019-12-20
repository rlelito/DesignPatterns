from __future__ import annotations
from visitor import Visitor


class Visitor1(Visitor):
    def visit_birds(self, element: Bird) -> float:
        return element.price

    def visit_others(self, element: Animal) -> float:
        return element.price
