from factory_controller import FactoryController
from factory_low_quality import FactoryLowQuality
from factory_high_quality import FactoryHighQuality


class Configuration(object):
    @staticmethod
    def choose_factory(factory: str) -> FactoryController:
        if factory == "low":
            return FactoryLowQuality()
        elif factory == "high":
            return FactoryHighQuality()
