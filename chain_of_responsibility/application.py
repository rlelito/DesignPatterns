from help_handler import HelpHandler


class Application(HelpHandler):
    def show_help(self):
        print("\tanApplication: can handle request, display help")

    def handle_help(self):
        print("anApplication: received a request to provide help")
        if self.has_help():
            self.show_help()
        else:
            print("\tanApplication: can't handle request, pass on request")
            super().handle_help()
