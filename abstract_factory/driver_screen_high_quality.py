from driver_screen import ScreenDriver
from dshq import DSHQ


class ScreenDriverHighQuality(ScreenDriver):
    @staticmethod
    def show() -> None:
        return DSHQ().show()
