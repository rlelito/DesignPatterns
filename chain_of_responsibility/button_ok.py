from help_handler import HelpHandler


class OkButton(HelpHandler):
    def handle_help(self) -> None:
        print("anOkButton: received a request to provide help")
        if self.has_help():
            # provide specific help
            pass
        else:
            print("\tanOkButton: can't handle request, pass on request")
            super().handle_help()
