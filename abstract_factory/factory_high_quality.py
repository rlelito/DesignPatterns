from factory_controller import FactoryController
from driver_screen import ScreenDriver
from driver_printer import PrinterDriver
from driver_screen_high_quality import ScreenDriverHighQuality
from driver_printer_high_quality import PrinterDriverHighQuality


class FactoryHighQuality(FactoryController):
    @staticmethod
    def get_screen_driver() -> ScreenDriver:
        return ScreenDriverHighQuality()

    @staticmethod
    def get_printer_driver() -> PrinterDriver:
        return PrinterDriverHighQuality()
