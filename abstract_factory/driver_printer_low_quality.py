from driver_printer import PrinterDriver
from dplq import DPLQ


class PrinterDriverLowQuality(PrinterDriver):
    @staticmethod
    def print() -> None:
        return DPLQ().print()
