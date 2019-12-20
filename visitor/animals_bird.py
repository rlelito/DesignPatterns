from __future__ import annotations
from animal import Animal


class Bird(Animal):
    def __init__(self, health: bool, price: float, black_market_price: float) -> None:
        super().__init__("bird", health, price)
        self._price_black_market = black_market_price

    @property
    def price_black_market(self) -> float:
        return self._price_black_market

    def check(self, visitor: Visitor) -> None:
        return visitor.visit_birds(self)
