from factory_controller import FactoryController
from driver_screen import ScreenDriver
from driver_printer import PrinterDriver
from driver_screen_low_quality import ScreenDriverLowQuality
from driver_printer_low_quality import PrinterDriverLowQuality


class FactoryLowQuality(FactoryController):
    @staticmethod
    def get_screen_driver() -> ScreenDriver:
        return ScreenDriverLowQuality()

    @staticmethod
    def get_printer_driver() -> PrinterDriver:
        return PrinterDriverLowQuality()
