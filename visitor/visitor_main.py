from __future__ import annotations
from typing import List

from animal_mammal import Mammal
from animals_bird import Bird
from animal_reptile import Reptile
from animal_fish import Fish

from visitor_1 import Visitor1
from visitor_2 import Visitor2
from visitor_3_vet import Visitor3


def code_price(components: List[Animal], visitor: Visitor) -> float:
    result = 0
    for comp in components:
        result += comp.check(visitor)
    return result


def code_health(components: List[Animal], visitor: Visitor) -> Animal:
    for comp in components:
        comp.check(visitor)


if __name__ == "__main__":
    m1 = Mammal(True, 50)
    m2 = Mammal(False, 25)
    b1 = Bird(True, 40, 60)
    b2 = Bird(False, 20, 80)
    b3 = Bird(False, 70, 40)
    r1 = Reptile(False, 70)
    f1 = Fish(True, 10)

    pet_store = [m1, m2, b1, b2, r1, f1]
    country_x = [b1, b2, b3, r1, f1]

    print("____ Visitor1 ____")
    print("All official prices:", code_price(pet_store, Visitor1()))
    print("\n____ Visitor2 ____")
    print("All prices (black market prices, if not included official price):", code_price(country_x, Visitor2()))
    print("\n____ Visitor3 ____")
    code_health(country_x, Visitor3())
