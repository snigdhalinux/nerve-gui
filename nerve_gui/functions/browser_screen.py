from gi.repository import Gtk, Adw
from nerve_gui.classes.nerve_screen import NerveScreen

class BrowserScreen(NerveScreen, Adw.Bin):
    __gtype_name__ = "BrowserScreen"
    list_browsers = Gtk.Template.Child()
    chosen_browser = ""
    move_to_summary = False

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.list_browsers.connect("row-selected", self.selected_browser)

        def selected_browser(self, widget, row):
            if row is not None:
                print(row.get_title())
                self.chosen_browser = row.get_title()
                row.select_button.set_active(True)
                self.set_valid(True)
            else:
                print("none")