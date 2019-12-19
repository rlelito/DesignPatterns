from application import Application
from dialog_print import PrintDialog
from dialog_save import SaveDialog
from button_print import PrintButton
from button_ok import OkButton

if __name__ == "__main__":
    # Initializing objects
    application = Application()
    save_dialog = SaveDialog()
    print_dialog = PrintDialog()
    print_button = PrintButton()
    ok_button = OkButton()

    # Setting successors (next handler)
    save_dialog.next_handler = application
    print_dialog.next_handler = application
    print_button.next_handler = print_dialog
    ok_button.next_handler = print_dialog

    print_button.handle_help()
    print()
    ok_button.handle_help()
    print()
    save_dialog.handle_help()
