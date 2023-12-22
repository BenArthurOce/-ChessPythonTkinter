# Apologies for any confusion caused. You are correct that we want to utilize the Move class instead of a dictionary to encapsulate the move details.

# In the example provided, the parse method of the MoveParser class currently returns a dictionary, but we can modify it to return an instance of the Move class instead. This way, the move details will be encapsulated within a dedicated object, which provides better encapsulation, readability, and extensibility.

# Here's an updated version of the code, incorporating the Move class:

class Move:
    def __init__(self, notation, colour, piece, code, location, destination, castling, capture, checkormate, promotion, file, rank):
        self.notation = notation
        self.colour = colour
        self.piece = piece
        self.code = code
        self.location = location
        self.destination = destination
        self.castling = castling
        self.capture = capture
        self.checkormate = checkormate
        self.promotion = promotion
        self.file = file
        self.rank = rank


class MoveParser:
    def __init__(self, notation):
        self.notation = notation

    def parse(self):
        colour = None
        piece = None
        code = None
        location = None
        destination = None
        castling = None
        capture = None
        checkormate = None
        promotion = None
        file = None
        rank = None

        # Implement the logic to parse the notation and extract the move details
        # Assign the extracted details to the respective variables

        # Example logic for extracting the colour
        if self.notation[0].isupper():
            colour = 'White'
        else:
            colour = 'Black'

        # Example logic for extracting the piece
        if self.notation[0].lower() in ['k', 'q', 'r', 'b', 'n']:
            piece = self.notation[0].lower()
        else:
            piece = 'P'

        # Example logic for extracting other elements like castling, capture, destination, etc.
        # ...

        move = Move(self.notation, colour, piece, code, location, destination, castling, capture, checkormate,
                    promotion, file, rank)
        return move


class ChessGame:
    def __init__(self):
        self.chessboard = Chessboard()
        self.moves = []

    def process_notation(self, notation):
        move_parser = MoveParser(notation)
        move = move_parser.parse()

        # Use the move details from the Move instance to locate the current piece and perform the move
        # ...
        # Assuming you have a method `make_move` in Chessboard that takes a Move instance
        self.chessboard.make_move(move)

        self.moves.append(move)


# Usage example
game = ChessGame()
notation = "e4"
game.process_notation(notation)

# Now you can access the moves and their details from the `game` instance
print(game.moves[0].notation)
print(game.moves[0].colour)
print(game.moves[0].piece)
# ... access other move details as needed
