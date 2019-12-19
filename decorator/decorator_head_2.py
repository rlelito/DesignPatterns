from decorator_confirmation import ConfirmationDecorator


class HeadDecorator2(ConfirmationDecorator):
    def print(self) -> None:
        # here code printing 2nd heading
        self.print_head()
        super().print()

    @staticmethod
    def print_head() -> None:
        print("HEADING 2")
