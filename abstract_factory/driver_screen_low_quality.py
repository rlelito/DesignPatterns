from driver_screen import ScreenDriver
from dslq import DSLQ


class ScreenDriverLowQuality(ScreenDriver):
    @staticmethod
    def show() -> None:
        return DSLQ().show()
