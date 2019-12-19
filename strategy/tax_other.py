from calculate_tax import CalculateTax


class TaxOther(CalculateTax):
    def tax(self, net_price: float) -> float:
        return net_price + 1
