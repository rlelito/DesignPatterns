from decorator_confirmation import ConfirmationDecorator


class HeadDecorator1(ConfirmationDecorator):
    def print(self) -> None:
        # here code printing 1st heading
        self.print_head()
        super().print()

    @staticmethod
    def print_head():
        print("HEADING 1")
