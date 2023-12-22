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
        move_details = {'notation': self.notation, 'colour': None, 'piece': None, 'code': None, 'location': None,
                        'destination': None, 'castling': None, 'capture': None, 'checkormate': None, 'promotion': None,
                        'file': None, 'rank': None}

        # Implement the logic to parse the notation and extract the move details
        # Assign the extracted details to the move_details dictionary

        # Example logic for extracting the colour
        if self.notation[0].isupper():
            move_details['colour'] = 'White'
        else:
            move_details['colour'] = 'Black'

        # Example logic for extracting the piece
        if self.notation[0].lower() in ['k', 'q', 'r', 'b', 'n']:
            move_details['piece'] = self.notation[0].lower()
        else:
            move_details['piece'] = 'P'

        # Example logic for extracting other elements like castling, capture, destination, etc.
        # ...

        move = Move(**move_details)
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
