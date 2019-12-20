from math import sqrt
from subject import Subject


class RealSubject(Subject):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def request(self) -> str:
        return self.quadratic_equation(self.a, self.b, self.c)

    def get_input(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def quadratic_equation(a: float, b: float, c: float) -> str:
        if a == 0:
            if b == 0:
                if c == 0:
                    return "Identity Equation."
                else:
                    return "Contradiction Equation."
            else:
                return f"One solution: x = {-c / b}."
        else:
            delta = b * b - 4 * a * c
            if delta < 0:
                return "No solutions."
            else:
                if delta == 0:
                    return f"One double solution: x = {-b / (2 * a)}."
                else:
                    x1 = (-b + sqrt(delta)) / (2 * a)
                    x2 = (-b - sqrt(delta)) / (2 * a)
                    return f"Solution: x1 = {x1}, x2 = {x2}."
