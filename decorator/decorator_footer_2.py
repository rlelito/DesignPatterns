from decorator_confirmation import ConfirmationDecorator


class FooterDecorator2(ConfirmationDecorator):
    def print(self) -> None:
        # here code printing 2nd footer
        super().print()
        self.print_footer()

    @staticmethod
    def print_footer() -> None:
        print("FOOTER 2")
