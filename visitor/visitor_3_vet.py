from __future__ import annotations
from visitor import Visitor


class Visitor3(Visitor):
    def visit_birds(self, element: Bird) -> None:
        result = f"Visited animal: {type(element).__name__}"
        if element.health:
            result += "\n\tDiagnosis: healthy."
        else:
            result += "\n\tDiagnosis: illness."
            if element.price_black_market >= 2 * element.price:
                result += "\n\tTreatment: clinic - medical tests, expensive treatment."
            else:
                result += "\n\tTreatment: antibiotics, diet."
        print(result)

    def visit_others(self, element: Animal) -> None:
        result = f"Visited animal: {type(element).__name__}"
        if element.health:
            result += "\n\tDiagnosis: healthy."
        else:
            result += "\n\tDiagnosis: illness.\n\tTreatment: antibiotics."
        print(result)
