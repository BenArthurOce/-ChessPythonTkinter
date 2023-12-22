import tkinter as tk
from cls_event import EventHandler

class uiChessSquareCanvas(tk.Canvas):
    def __init__(self, parent, colour:str, width:int, height:int):
        super().__init__(parent, borderwidth=0, highlightthickness=0, width=width, height=height, background=colour)
        self.piece_image = None
        self.event_handler = EventHandler()
        self.bind("<Button-1>", self.handle_click)

    def set_piece_image(self, image:tk.PhotoImage, square_width, square_height):
        resize_factor = min(square_width / image.width(), square_height / image.height())
        self.piece_image = image.subsample(int(1 / resize_factor))

    def display_image(self, x:int, y:int):
        if self.piece_image:
            self.create_image(x, y, image=self.piece_image, anchor="nw")

    def remove_piece(self):
        self.delete("all")
        self.piece_image = None

    def handle_click(self, event):
        print(event)
        self.event_handler.handle_event("widget_name")  # Pass the appropriate widget name
