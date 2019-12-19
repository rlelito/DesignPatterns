from help_handler import HelpHandler


class PrintDialog(HelpHandler):
    def handle_help(self):
        print("aPrintDialog: received a request to provide help")
        if self.has_help():
            # provide specific help
            pass
        else:
            print("\taPrintDialog: can't handle request, pass on request")
            super().handle_help()
