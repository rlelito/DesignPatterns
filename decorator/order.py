from configuration import Configuration


class Order(object):
    @staticmethod
    def print(confirm_type: str) -> None:
        selected_confirmation = Configuration().get_confirmation(confirm_type)
        selected_confirmation.print()
