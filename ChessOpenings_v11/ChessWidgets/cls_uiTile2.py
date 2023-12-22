import tkinter as tk


class UITile(tk.Frame):
    def __init__(self, parent, ref_num: int, main_or_sub: str, colour: str, frame_width: int, frame_height):
        super().__init__(parent, background=colour, bd=2, width=frame_width, height=frame_height, padx=10, pady=10)

        self.frame_width = frame_width
        self.frame_height = frame_height
        self.main_or_sub = main_or_sub
        self.original_background = colour

        self.bind("<Button-1>", self.on_mouse_click)

    def on_mouse_click(self, event):
        # Change the color of the clicked tile
        self.configure(background="red")

        # Change the color of other tiles to the original color
        for tile in ui_tiles:
            if tile != self:
                tile.configure(background=tile.original_background)


# Create a list to store the UITile objects
ui_tiles = []

# Create the main Tkinter window
window = tk.Tk()

# Create UITile objects and add them to the list
for i in range(3):
    tile = UITile(window, i, "Main", "white", 100, 100)
    ui_tiles.append(tile)
    tile.pack()

# Start the Tkinter event loop
window.mainloop()
