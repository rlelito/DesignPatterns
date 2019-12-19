from help_handler import HelpHandler


class SaveDialog(HelpHandler):
    def handle_help(self):
        print("aSaveDialog: received a request to provide help")
        if self.has_help():
            # provide specific help
            pass
        else:
            print("\taSaveDialog: can't handle request, pass on request")
            super().handle_help()
