from decorator_confirmation import ConfirmationDecorator


class FooterDecorator1(ConfirmationDecorator):
    def print(self) -> None:
        # here code printing 1st footer
        super().print()
        self.print_footer()

    @staticmethod
    def print_footer() -> None:
        print("FOOTER 1")
