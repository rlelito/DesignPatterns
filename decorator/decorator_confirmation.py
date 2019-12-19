from component import Component


class ConfirmationDecorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    def print(self) -> None:
        if self._component is not None:
            self._component.print()
