# ide_screen.py

from gi.repository import Gtk, Adw
from nerve_gui.classes.nerve_screen import NerveScreen

@Gtk.Template(resource_path="/org/snigdhaos/nerve_gui/pages/ide_screen.ui")
class IdeScreen(NerveScreen, Adw.Bin):
    __gtype_name__ = "IdeScreen"

    list_ide = Gtk.Template.Child()

    chosen_ide = ""
    move_to_summary = False

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window

        self.list_ide.connect("row-selected", self.selected_ide)
    
    def selected_ide(self, widget, row):
        if row is not None:
            print(row.get_title())
            self.chosen_ide = row.get_title()
            row.select_button.set_active(True)

            self.set_valid(True)
        else:
            print("row is none!!")