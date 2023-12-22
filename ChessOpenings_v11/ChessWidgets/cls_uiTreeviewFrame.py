import tkinter as tk
from tkinter import ttk

class TreeviewFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.treeviewScrollbar = None
        self.treeview = None
        self.selected_item = None
        self._create_treeview_widgets()


        

    def set_selected_item(self, item):
        self.selected_item = item


    def _create_treeview_widgets(self):
        self.treeviewScrollbar = tk.Scrollbar(self)
        self.treeview = ttk.Treeview(
            self,
            columns=("Column1", "Column2", "Column3"),
            selectmode=tk.BROWSE,
            show="headings",
            height=30,
            yscrollcommand=self.treeviewScrollbar.set
        )
        self.treeview.column("Column1", width=50, anchor=tk.CENTER)
        self.treeview.column("Column2", width=100, anchor=tk.W)
        self.treeview.column("Column3", width=300, anchor=tk.W)
        self.treeview.heading("Column1", text="Code")
        self.treeview.heading("Column2", text="Name")
        self.treeview.heading("Column3", text="Annotation")

        self.treeviewScrollbar.config(command=self.treeview.yview)
        # self.treeview.bind("<<TreeviewSelect>>", self._treeview_onSingleClick)
        # self.treeview.bind("<Double-1>", self._treeview_onDoubleClick)

        self.treeview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.treeviewScrollbar.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

    def POPULATE_TREEVIEW(self, openings_dictionary:dict):
        for index, (each_key, each_value) in enumerate(openings_dictionary.items()):
            self.treeview.insert("", tk.END, values=(each_value['ECO'], each_value['CONTINUATIONNAME'], each_key))
        
    def CLEAR_THE_TREEVIEW(self):
        self.treeview.delete(*self.treeview.get_children())

    # def _treeview_onSingleClick(self):
    #     pass

    # def _treeview_onDoubleClick(self):
    #     pass
