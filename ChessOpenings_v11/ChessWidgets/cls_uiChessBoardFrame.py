import tkinter as tk
from cls_ChessboardDict import ChessboardDict
from ChessWidgets.cls_uiChessSquareCanvas import uiChessSquareCanvas

class uiChessBoardFrame(tk.Frame):
    def __init__(self, master, colour:str, board_width:int, board_height:int):
        super().__init__(master, background=colour, bd=2, width=board_width, height=board_height)
        self.board_width = board_width
        self.board_height = board_height
        self.squares = [] # Store uiChessSquareCanvas objects
        self.piece_images = {}  # Store PhotoImage objects

        self.generate_chessboard_squares(board_width / 8, board_height / 8)

    def generate_chessboard_squares(self, square_width:int, square_height:int):
        colours = ["#eeeed2", "#769656"]

        for row in range(8):
            for col in range(8):
                x = col * square_width
                y = row * square_height
                square_color = colours[(row + col) % 2]
                square = uiChessSquareCanvas(self, square_color, square_width, square_height)
                square.grid(row=row, column=col)
                self.squares.append(square)

    def loop_through_squares(self, ChessBoardDict:ChessboardDict, isReversed:bool):
        chessboardList = ChessBoardDict.get_dictionary_to_list()

        if isReversed:
            chessboardList = reversed(chessboardList)

        for square, piece_code in zip(self.squares, chessboardList):
            if piece_code is not None:
                if piece_code not in self.piece_images:
                    image_path = self.get_photoimage(piece_code, self.board_width / 8, self.board_height / 8)
                    self.piece_images[piece_code] = tk.PhotoImage(file=image_path)
                piece_image = self.piece_images[piece_code]
                square.set_piece_image(piece_image, self.board_width / 8, self.board_height / 8)
                square.display_image(0, 0)
            else:
                square.remove_piece()

    def reset_chessboard(self):
        for square in self.squares:
            square.remove_piece()

    def get_photoimage(self, piece_code: str, square_width: int, square_height: int) -> str:
        chess_images = {
            "wp": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_pawn.png",
            "wB": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_bishop.png",
            "wN": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_knight.png",
            "wR": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_rook.png",
            "wK": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_king.png",
            "wQ": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_white_queen.png",
            "bp": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_pawn.png",
            "bB": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_bishop.png",
            "bN": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_knight.png",
            "bR": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_rook.png",
            "bK": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_king.png",
            "bQ": r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\504p_black_queen.png",
        }
        return chess_images.get(piece_code)
