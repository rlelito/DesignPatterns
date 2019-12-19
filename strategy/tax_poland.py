from calculate_tax import CalculateTax


class TaxPoland(CalculateTax):
    def tax(self, net_price: float) -> float:
        return net_price * 0.23
