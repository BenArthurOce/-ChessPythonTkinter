class Command:
    def execute(self):
        pass


class ClearAllCommand(Command):
    def __init__(self, ui):
        self.ui = ui

    def execute(self):
        self.ui._btn_clear_all_on_single_click()

class FillGridCommand(Command):
    def __init__(self, ui):
        self.ui = ui

    def execute(self):
        self.ui._btn_fill_grid_on_single_click()

class DoubleClickCommand(Command):
    def __init__(self, ui):
        self.ui = ui

    def execute(self):
        self.ui._treeview_double_click()

class SingleClickCommand(Command):
    def __init__(self, ui):
        self.ui = ui

    def execute(self):
        self.ui._treeview_on_select()
