import tkinter as tk
from tkinter import ttk

class uiScrollableTileContainer(tk.Frame):
    def __init__(self, parent, colour):
        super().__init__(parent, background="black")

        self.selected_item = None

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        self.content_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor=tk.NW)

        self.bind_events()

    def bind_events(self):
        self.content_frame.bind("<Configure>", self.update_scroll_region)
        self.canvas.bind_all("<MouseWheel>", self.scroll_canvas)
        self.canvas.bind("<Configure>", self.configure_canvas_scrollregion)


    def set_selected_item(self, item):
        self.selected_item = item
        
    def update_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def scroll_canvas(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def configure_canvas_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_item(self, obj_to_add, ref_num):
        obj_to_add.grid(row=ref_num // 2, column=ref_num % 2, rowspan=1, columnspan=1)


    def clear_items(self):
        for child in self.content_frame.winfo_children():
            child.destroy()

    def return_all_items_as_list(self, object_instance) -> list:
        return [child for child in self.content_frame.winfo_children() if isinstance(child, object_instance)]