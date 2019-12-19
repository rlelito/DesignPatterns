from driver_printer import PrinterDriver
from dphq import DPHQ


class PrinterDriverHighQuality(PrinterDriver):
    @staticmethod
    def print() -> None:
        return DPHQ().print()
