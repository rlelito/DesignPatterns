from help_handler import HelpHandler


class PrintButton(HelpHandler):
    def handle_help(self):
        print("aPrintButton: received a request to provide help")
        if self.has_help():
            # provide specific help
            pass
        else:
            print("\taPrintButton: can't handle request, pass on request")
            super().handle_help()
