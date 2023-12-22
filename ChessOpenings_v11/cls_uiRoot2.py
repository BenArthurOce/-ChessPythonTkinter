import tkinter as tk
from tkinter import ttk


from ChessWidgets.cls_uiTile import uiTile
from ChessWidgets.cls_uiScrollableTileContainer import uiScrollableTileContainer
from ChessWidgets.cls_uiTreeviewFrame import TreeviewFrame

from cls_OpeningsDict import OpeningsDict
from cls_ChessGameLogic import ChessGameLogic

# from cls_event import EventHandler
from cls_command_pattern import *


class UIRoot(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess")
        self.root.geometry('1200x650+0+0')

        # Openings() object
        self.AllOpenings = OpeningsDict()

        # Events
        # self.event_handler = EventHandler()
        # self.command = None
        self.double_click_command = None
        self.single_click_command = None

        # CURRENT SELECT ITEMS
        # ==========================================
        self.current_selection_Listbox = ""
        self.current_selection_Treeview = ""

        # TOP LEVEL FRAMES
        # ==========================================
        # Main Frame
        self.TopLevelFrameALL = ttk.Frame(self.root)
        self.TopLevelFrameALL.pack(fill=tk.BOTH, expand=True)

        # Left Half - Interactive UI
        self.TopLevelFrameLEFT = tk.Frame(self.TopLevelFrameALL, bg="black")
        self.TopLevelFrameLEFT.pack(side=tk.LEFT, fill=tk.BOTH)

        # Right Half - Chessboard Grid
        self.TopLevelFrameRIGHT = tk.Frame(self.TopLevelFrameALL, bg="black")
        self.TopLevelFrameRIGHT.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # LEFT PANEL FRAMES
        # ==========================================
        # Listbox and Scrollbar (sample two move openings)
        self.twoMoveContainer = tk.Frame(self.TopLevelFrameLEFT)
        self.twoMoveContainer.grid(row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, sticky="nsew")
        self._create_opening_move_list_widget()

        # Frame that holds input buttons and textbox
        self.inputContainer = tk.Frame(self.TopLevelFrameLEFT)
        self.inputContainer.grid(row=1, column=0, rowspan=1, columnspan=1, padx=10, pady=10)     # Goes under the twoMoveList_widget
        self._create_button_widgets()

        # Single Chessboard display
        self.MainChessboardTile = uiTile(parent=self.TopLevelFrameLEFT, ref_num=0, main_or_sub="Main", colour="pink", frame_width=250, frame_height=250)
        self.MainChessboardTile.grid(row=0, column=1, rowspan=2, columnspan=1, padx=10, pady=10)

        # List/Table of openings
        self.treeviewContainer = TreeviewFrame(self.TopLevelFrameLEFT)
        self.treeviewContainer.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Bind the function to the TreeviewSelect event
        self.treeviewContainer.treeview.bind("<<TreeviewSelect>>", self._treeview_on_select)

        # Bind the function to the Treeview double-click event
        self.treeviewContainer.treeview.bind("<Double-1>", self._treeview_double_click)


        # RIGHT PANEL FRAMES
        # ==========================================
        self.ChessBoardContainer = uiScrollableTileContainer (self.TopLevelFrameRIGHT, "purple")
        self.ChessBoardContainer.pack(fill=tk.BOTH, expand=True)

        # RUN PROGRAM
        # ==========================================
        # self.run_program()

    # CREATE WIDGETS - LIST OF TWO MOVES
    # ==========================================
    def _create_opening_move_list_widget(self):
        # Heading
        lblMoveCombinations = tk.Label(master=self.twoMoveContainer, text="Move Combinations:")
        lblMoveCombinations.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create three Button tabs for move combinations selection
        button1 = ttk.Button(master=self.twoMoveContainer, width=5, text="1", command=lambda: self.on_button_selected(1))
        button2 = ttk.Button(master=self.twoMoveContainer, width=5, text="2", command=lambda: self.on_button_selected(2))
        button3 = ttk.Button(master=self.twoMoveContainer, width=5, text="3", command=lambda: self.on_button_selected(3))
        button4 = ttk.Button(master=self.twoMoveContainer, width=5, text="Fav", command=lambda: self.on_button_selected_fav(0))
        button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        button2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        button3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        button4.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        # Create a Listbox that holds the openings
        listbox = tk.Listbox(master=self.twoMoveContainer)
        listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create a Scrollbar
        scrollbar = tk.Scrollbar(self.twoMoveContainer, command=listbox.yview)
        scrollbar.grid(row=2, column=3, padx=0, pady=10, sticky="ns")

        # Configure the Listbox and Scrollbar
        listbox.config(yscrollcommand=scrollbar.set)

        self.listbox = listbox

        # Define the onclick event handler
        def on_listbox_select(event):
            selected_index = listbox.curselection()
            self.current_selection_Listbox = listbox.get(selected_index)

            # Pass the selected item to the Treeview widget
            self.treeviewContainer.set_selected_item(self.current_selection_Listbox)

            # Other Commands
            self._COMMAND_reset_MainChessTile()
            self._COMMAND_update_MainChessTile()
            self._COMMAND_populate_treeview()



        # Bind the onclick event to the Listbox
        listbox.bind('<<ListboxSelect>>', on_listbox_select)

        # Initial population of the Listbox
        self.populate_listbox(2)  # Initial selection

    def populate_listbox(self, move_combination):
        self.listbox.delete(0, tk.END)
        opening_dict = self.AllOpenings.filter_opening_dict("MOVENUMBER", move_combination)
        openings = list(opening_dict.keys())
        self.listbox.insert(tk.END, *openings)

    def on_button_selected(self, move_combination):
        self.populate_listbox(move_combination)

    def on_button_selected_fav(self, move_combination):
        self.listbox.delete(0, tk.END)
        opening_dict = self.AllOpenings.filter_opening_dict("FAVOURITE", 0)
        openings = list(opening_dict.keys())
        self.listbox.insert(tk.END, *openings)

    # CREATE WIDGETS - BUTTONS
    # ==========================================
    def _create_button_widgets(self):
        # user input buttons
        self.btnFetchECOS = tk.Button(self.inputContainer, text="Empty Btn", command=self._btn_empty_btn_on_single_click)
        self.btnEmptyBtn = tk.Button(self.inputContainer, text="Empty Btn", command=self._btn_empty_btn_on_single_click)
        self.btnClearAll = tk.Button(self.inputContainer, text="Clear All", command=self._btn_clear_all_on_single_click)
        self.btnFillGrid = tk.Button(self.inputContainer, text="Fill Grid", command=self._btn_fill_grid_on_single_click)

        # Grid to self.inputContainer
        self.btnFetchECOS.grid(row=0, column=0, padx=10, pady=10)
        self.btnEmptyBtn.grid(row=1, column=0, padx=10, pady=10)
        self.btnClearAll.grid(row=0, column=1, padx=10, pady=10)
        self.btnFillGrid.grid(row=1, column=1, padx=10, pady=10)

    def _btn_empty_btn_on_single_click(self):
        a = self._COMMAND_return_TopLevelFrameLEFT_width()
        b = self._COMMAND_return_TopLevelFrameRIGHT_width()
        print(a, b)

    # BUTTON CLICK EVENT - CLEAR DATA
    # ==========================================
    def _btn_clear_all_on_single_click(self):
        self._COMMAND_clear_treeview()
        self._COMMAND_reset_MainChessTile()
        self._COMMAND_clear_ChessBoardContainer()

    # BUTTON CLICK EVENT - FILL GRID
    # ==========================================
    def _btn_fill_grid_on_single_click(self):
        self.current_selection_Listbox = self._COMMAND_return_listbox_selection().strip()
        if not self.current_selection_Listbox or self.current_selection_Listbox == "":
            return
        self._COMMAND_populate_ChessBoardContainer()

    # TREEVIEW CLICK EVENTS
    # ==========================================
    def _treeview_on_select(self, event):
        selected_item = self.treeviewContainer.treeview.focus()
        # Do something with the selected item


    def _treeview_double_click(self, event):
        self._COMMAND_clear_ChessBoardContainer()

        selected_item = self.treeviewContainer.treeview.focus()
        selected_item_values = self.treeviewContainer.treeview.item(selected_item)['values']

        mydictionary = self._COMMAND_fetch_dictionary_openings_eco(selected_item_values[0])
        self._COMMAND_populate_ChessBoardContainer_eco(mydictionary)

    def _COMMAND_return_listbox_selection(self) -> str:
        selected_index = self.listbox.curselection()
        if selected_index:
            return self.listbox.get(selected_index)

    def _COMMAND_return_treeview_selection(self) -> str:
        selected_index = self.listbox.curselection()
        if selected_index:
            return self.listbox.get(selected_index)

    def _COMMAND_clear_treeview(self):
        self.treeviewContainer.CLEAR_THE_TREEVIEW()

    def _COMMAND_populate_treeview(self):
        self.treeviewContainer.CLEAR_THE_TREEVIEW()
        myDictionary = self._COMMAND_fetch_dictionary_openings_continuation()
        self.treeviewContainer.POPULATE_TREEVIEW(myDictionary)

    def _COMMAND_update_MainChessTile(self):
        new_chess_logic = ChessGameLogic(self.AllOpenings, self.current_selection_Listbox)
        self.MainChessboardTile.ChessboardFrame.reset_chessboard()
        notation = new_chess_logic.return_game_notation()
        name = new_chess_logic.return_game_name()
        # print(notation, name)
        self.MainChessboardTile.update_chess_tile(new_chess_logic.ChessDictionary, notation, name)

    def _COMMAND_reset_MainChessTile(self):
        pass

    def _COMMAND_fetch_dictionary_openings_continuation(self):
        return self.AllOpenings.filter_opening_dict('CONTINUATION', self.current_selection_Listbox)

    def _COMMAND_fetch_dictionary_openings_notation(self):
        return self.AllOpenings.filter_opening_dict('MOVESTART', self.current_selection_Listbox)

    def _COMMAND_fetch_dictionary_openings_eco(self, eco_string):
        return self.AllOpenings.filter_opening_dict('ECO', eco_string)

    def _COMMAND_clear_ChessBoardContainer(self):
        self.ChessBoardContainer.clear_items()

    def _COMMAND_populate_ChessBoardContainer_eco(self, eco_dictionary: dict):
        list_pgn_strings = list(eco_dictionary.keys())

        a = round(self._COMMAND_return_TopLevelFrameRIGHT_width() / 4)

        for i, pgn in enumerate(list_pgn_strings):
            new_uiTile = self._create_uiTile_sub(i, a)
            self._update_uiTile(new_uiTile, pgn)

    def _COMMAND_populate_ChessBoardContainer(self):
        dictionary_of_openings = self._COMMAND_fetch_dictionary_openings_notation()
        list_pgn_strings = list(dictionary_of_openings.keys())

        for i, pgn in enumerate(list_pgn_strings):
            new_uiTile = self._create_uiTile_sub(i, 150)
            self._update_uiTile(new_uiTile, pgn)

    def _create_uiTile_sub(self, ref_num: int, frame_width: int) -> uiTile:
        new_uiTile = uiTile(self.ChessBoardContainer.content_frame, ref_num=ref_num, main_or_sub="Sub",
                            colour="black", frame_width=frame_width, frame_height=frame_width)
        new_uiTile.grid(row=ref_num // 2, column=ref_num % 2, padx=10, pady=10)
        return new_uiTile

    def _update_uiTile(self, uiTile_instance: uiTile, pgn: str):
        new_chess_logic = ChessGameLogic(self.AllOpenings, pgn)
        notation = new_chess_logic.return_game_notation()
        name = new_chess_logic.return_game_name()
        uiTile_instance.update_chess_tile(new_chess_logic.ChessDictionary, name, notation)

    def _COMMAND_return_TopLevelFrameLEFT_width(self) -> int:
        return int(self.TopLevelFrameLEFT.winfo_width())

    def _COMMAND_return_TopLevelFrameRIGHT_width(self) -> int:
        return int(self.TopLevelFrameRIGHT.winfo_width())

    def run_program(self):
        self.root.mainloop()



    def set_double_click_command(self, command):
        self.double_click_command = command

    def set_single_click_command(self, command):
        self.single_click_command = command

    def handle_double_click(self):
        if self.double_click_command:
            self.double_click_command.execute()

    def handle_single_click(self):
        if self.single_click_command:
            self.single_click_command.execute()

    def _treeview_double_click(self):
        # ...

        # Handle the double-click event
        self.handle_double_click()

    def _treeview_on_select(self):
        # ...

        # Handle the single-click event
        self.handle_single_click()


if __name__ == "__main__":
    ui = UIRoot()

    # Create commands
    double_click_command = DoubleClickCommand(ui)
    single_click_command = SingleClickCommand(ui)

    # Associate commands with UI events
    ui.treeviewContainer.treeview.bind("<Double-1>", lambda event: ui.set_double_click_command(double_click_command))
    ui.treeviewContainer.treeview.bind("<<TreeviewSelect>>", lambda event: ui.set_single_click_command(single_click_command))

    ui.run_program()
