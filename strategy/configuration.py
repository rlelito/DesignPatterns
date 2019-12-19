from calculate_tax import CalculateTax
from tax_poland import TaxPoland
from tax_other import TaxOther


class Configuration(object):
    @staticmethod
    def choose_method(country: str) -> CalculateTax:
        switcher = {
            "Poland": TaxPoland(),
            "Other": TaxOther()
        }
        return switcher.get(country, TaxPoland())  # default value TaxPoland()
