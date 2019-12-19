from abc import ABC
from abc import abstractmethod
from driver_screen import ScreenDriver
from driver_printer import PrinterDriver


class FactoryController(ABC):
    @staticmethod
    @abstractmethod
    def get_screen_driver() -> ScreenDriver:
        pass

    @staticmethod
    @abstractmethod
    def get_printer_driver() -> PrinterDriver:
        pass
