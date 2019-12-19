from configuration import Configuration


class Order(object):
    def __init__(self, country: str, products: list) -> None:
        self._c_tax = Configuration.choose_method(country)
        self._products: list = products

    def calculate_tax(self) -> None:
        for item in self._products:
            print(f"{item['name']}: {item['amount']} x {item['price']:.2f} => "
                  f"{item['amount'] * (item['price'] + self._c_tax.tax(item['price'])):.2f}")
