from order import Order

if __name__ == "__main__":
    cart = [
        {'name': 'Product 1', 'price': 2.79, 'amount': 1},
        {'name': 'Product 2', 'price': 1, 'amount': 3},
        {'name': 'Product 3', 'price': 3.49, 'amount': 1},
        {'name': 'Product 4', 'price': 1.37, 'amount': 1},
        {'name': 'Product 5', 'price': 3, 'amount': 2}
    ]

    print("1st strategy")
    o1 = Order('Polska', cart)
    o1.calculate_tax()

    print("\n2nd strategy")
    o1 = Order('Drugi', cart)
    o1.calculate_tax()
