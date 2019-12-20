from base_component import BaseComponent


class CheckboxComponent(BaseComponent):
    def __init__(self, action: str, text: str) -> None:
        super().__init__()
        self.action: str = action
        self.text: str = text
        self.checked: bool = False

    def check(self) -> None:
        self.mediator.notify(self, self.action)

    def __str__(self):
        return f"[{'X' if self.checked else ' '}] {self.action}) {self.text}"
