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
        # Implement the logic to parse the notation and extract the move details
        # You can use regular expressions, string manipulation, or any other method that suits your needs

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

        move = Move(
            notation=self.notation,
            colour=colour,
            piece=piece,
            code=None,  # Set the appropriate value
            location=None,  # Set the appropriate value
            destination=None,  # Set the appropriate value
            castling=None,  # Set the appropriate value
            capture=None,  # Set the appropriate value
            checkormate=None,  # Set the appropriate value
            promotion=None,  # Set the appropriate value
            file=None,  # Set the appropriate value
            rank=None  # Set the appropriate value
        )

        return move


class ChessGame:
    def __init__(self):
        self.moves = []

    def process_notation(self, notation):
        move_parser = MoveParser(notation)
        move = move_parser.parse()

        # Use the move details from the Move instance to locate the current piece and perform the move
        # ...

        self.moves.append(move)
