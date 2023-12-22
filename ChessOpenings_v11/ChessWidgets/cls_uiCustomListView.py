import tkinter as tk

class TileFrame(tk.Frame):
    def __init__(self, parent, text, list_view):
        super().__init__(parent)
        self.list_view = list_view
        self.configure(bg='white', relief='raised', bd=2)
        self.pack(side='top', fill='x', padx=10, pady=5)
        self.label = tk.Label(self, text=text, bg='white')
        self.label.pack(padx=10, pady=5)

        # Bind click event to all child widgets
        self.bind_all_children("<Button-1>", self.on_tile_click)

    def bind_all_children(self, event, callback):
        for child in self.winfo_children():
            child.bind(event, callback)

    def on_tile_click(self, event):
        self.list_view.select_tile(self)

class ListView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.container = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor='nw')

        self.tiles = []
        self.selected_tile = None

    def add_tile(self, text):
        tile = TileFrame(self.container, text, self)
        self.tiles.append(tile)

    def select_tile(self, tile):
        if self.selected_tile:
            self.selected_tile.configure(bg='white')
        self.selected_tile = tile
        self.selected_tile.configure(bg='lightblue')


