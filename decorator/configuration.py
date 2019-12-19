from confirmation import Confirmation
from decorator_confirmation import ConfirmationDecorator
from decorator_head_1 import HeadDecorator1
from decorator_head_2 import HeadDecorator2
from decorator_footer_1 import FooterDecorator1
from decorator_footer_2 import FooterDecorator2


class Configuration(object):
    @staticmethod
    def get_confirmation(confirm_type: str) -> ConfirmationDecorator:
        switcher = {
            "scenario_1": HeadDecorator1(FooterDecorator1(FooterDecorator2(Confirmation()))),
            "scenario_2": HeadDecorator1(HeadDecorator2(FooterDecorator2(Confirmation())))
        }
        return switcher.get(confirm_type, switcher["scenario_1"])  # default call 1st value
