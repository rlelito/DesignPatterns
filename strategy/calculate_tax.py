from abc import ABC
from abc import abstractmethod


class CalculateTax(ABC):
    @abstractmethod
    def tax(self, net_price: float) -> float:
        pass
