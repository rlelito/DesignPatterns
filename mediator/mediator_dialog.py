from mediator import Mediator
from component_checkbox import CheckboxComponent


class DialogMediator(Mediator):
    def __init__(self, ch1: CheckboxComponent, ch2: CheckboxComponent, ch3: CheckboxComponent) -> None:
        self._checkbox_1 = ch1
        self._checkbox_1.mediator = self
        self._checkbox_2 = ch2
        self._checkbox_2.mediator = self
        self._checkbox_3 = ch3
        self._checkbox_3.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "1":
            if not self._checkbox_1.checked:
                self._checkbox_1.checked = True
            else:
                self._checkbox_1.checked = False
                self._checkbox_2.checked = False
                self._checkbox_3.checked = False
        elif event == "2":
            if not self._checkbox_2.checked:
                self._checkbox_1.checked = True
                self._checkbox_2.checked = True
            else:
                self._checkbox_2.checked = False
                self._checkbox_3.checked = False
        elif event == "3":
            if not self._checkbox_3.checked:
                self._checkbox_1.checked = True
                self._checkbox_2.checked = True
                self._checkbox_3.checked = True
            else:
                self._checkbox_3.checked = False
