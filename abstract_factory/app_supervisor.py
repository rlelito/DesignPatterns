from configuration import Configuration


class AppSupervisor(object):
    def __init__(self, screen: str, printer: str) -> None:
        self._screen_driver = Configuration().choose_factory(screen).get_screen_driver()
        self._printer_driver = Configuration().choose_factory(printer).get_printer_driver()

    def show(self) -> None:
        return self._screen_driver.show()

    def print(self) -> None:
        return self._printer_driver.print()
