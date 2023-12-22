import tkinter as tk
from ChessWidgets.cls_uiChessBoardFrame import uiChessBoardFrame


class uiTile(tk.Frame):
    def __init__(self, parent, ref_num: int, main_or_sub: str, colour: str, frame_width: int, frame_height: int):
        super().__init__(parent, background=colour, bd=2, width=frame_width, height=frame_height, padx=10, pady=10)

        self.frame_width = frame_width
        self.frame_height = frame_height
        self.main_or_sub = main_or_sub
        self.original_background = colour  # Store the original background color
        # self.bind_events()  # Bind the mouse events
        # self.bind_frames(self)
        self.bind("<Button-1>", self.on_tile_click)
        self.create_widgets()


    def bind_all_children(self, event, callback):
        for child in self.winfo_children():
            child.bind(event, callback)

    def on_tile_click(self, event):
        self.list_view.select_tile(self)

    # def on_mouse_click(self, event):
    #     print("tile clicked")
        


    # def on_mouse_enter(self, event):
    #     # Change the background color to red when the mouse enters the tile
    #     self.configure(background="red")

    # def on_mouse_leave(self, event):
    #     # Change the background color back to the original color when the mouse leaves the tile
    #     self.configure(background=self.original_background)

    def create_widgets(self):
        if self.main_or_sub == "Main":
            self.ChessboardFrame = uiChessBoardFrame(self, colour='darkgray', board_width=self.frame_width, board_height=self.frame_height)

            # Determine the width of the chessboard frame
            self.ChessboardFrame.update_idletasks()
            chessboard_width = self.ChessboardFrame.winfo_width()

            self.TextboxUpper = CenteredTextBox(self, width=chessboard_width, height=2, background="#C7E0D4",
                                                font=("Arial", 8), wrap="word")  # Light green background color
            self.TextboxLower = CenteredTextBox(self, width=chessboard_width, height=2, background="#E0C7D1",
                                                font=("Arial", 8), wrap="word")  # Light pink background color

            # Configure the grid weights to expand the chessboard frame horizontally
            self.grid_columnconfigure(0, weight=1)

            self.TextboxLower.grid(row=0, column=0, sticky="ew")
            self.ChessboardFrame.grid(row=1, column=0, sticky="ew")
            self.TextboxUpper.grid(row=2, column=0, sticky="ew")

        elif self.main_or_sub == "Sub":
            self.configure(bd=1, relief="solid", borderwidth=1)  # Add black border

            self.TextboxUpper = CenteredTextBox(self, width=20, height=5, background="#C7E0D4",
                                                font=("Arial", 8), wrap="word")  # Light green background color
            self.TextboxLower = CenteredTextBox(self, width=20, height=5, background="#E0C7D1",
                                                font=("Arial", 8), wrap="word")  # Light pink background color

            self.TextboxUpper.grid(row=0, column=0, sticky="ew")
            self.TextboxLower.grid(row=1, column=0, sticky="ew")

            self.ChessboardFrame = uiChessBoardFrame(self, colour='darkgray', board_width=self.frame_width, board_height=self.frame_height)
            self.ChessboardFrame.grid(row=0, column=1, rowspan=2, sticky="nsew")

            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)

    def update_chess_tile(self, chessboard_dict:dict, upper_string:str, lower_string:str):
        self.TextboxUpper.set_text(upper_string)
        self.TextboxLower.set_text(lower_string)
        self.ChessboardFrame.loop_through_squares(chessboard_dict, False)


class CenteredTextBox(tk.Text):
    def __init__(self, parent, width, height, background, font, wrap):
        super().__init__(parent, background=background, width=width, height=height, padx=5, pady=5, font=font, wrap=wrap)  # Set the wrap attribute
        self.tag_configure("center", justify="center")

    def set_text(self, text):
        self.configure(state="normal")  # Enable modifications to the text
        self.delete("1.0", tk.END)
        self.insert(tk.END, text)
        self.center_text()
        self.configure(state="disabled")  # Disable modifications to the text

    def clear_text(self):
        self.delete("1.0", tk.END)

    def center_text(self):
        self.tag_add("center", "1.0", tk.END)

        lines = int(self.index(tk.END).split(".")[0])
        for line in range(1, lines + 1):
            self.tag_add("center", f"{line}.0", f"{line + 1}.0")

        self.configure(state="disabled")
