def is_valid_rook_move(rook, destination):
    return rook['rank'] == destination['rank'] or rook['file'] == destination['file']

def is_valid_bishop_move(bishop, destination):
    return abs(ord(bishop['file']) - ord(destination['file'])) == abs(bishop['rank'] - destination['rank'])

def is_valid_knight_move(knight, destination):
    return (abs(ord(knight['file']) - ord(destination['file'])) == 2 and abs(knight['rank'] - destination['rank']) == 1) or \
           (abs(ord(knight['file']) - ord(destination['file'])) == 1 and abs(knight['rank'] - destination['rank']) == 2)

def is_valid_queen_move(queen, destination):
    return is_valid_rook_move(queen, destination) or is_valid_bishop_move(queen, destination)

def is_valid_king_move(king, destination):
    return abs(ord(king['file']) - ord(destination['file'])) <= 1 and abs(king['rank'] - destination['rank']) <= 1

def get_piece_able_to_move(pieces, destination):
    for piece in pieces.values():
        if piece['pieceObj'] == 'wR' and is_valid_rook_move(piece, destination):
            return piece
        elif piece['pieceObj'] == 'wB' and is_valid_bishop_move(piece, destination):
            return piece
        elif piece['pieceObj'] == 'wN' and is_valid_knight_move(piece, destination):
            return piece
        elif piece['pieceObj'] == 'wQ' and is_valid_queen_move(piece, destination):
            return piece
        elif piece['pieceObj'] == 'wK' and is_valid_king_move(piece, destination):
            return piece
    return None

# Assuming a dictionary of pieces on the chessboard
pieces = {
    'a1': {'square': 'a1', 'file': 'a', 'rank': 1, 'gridRow': 7, 'gridCol': 0, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wR'},
    'h1': {'square': 'h1', 'file': 'h', 'rank': 1, 'gridRow': 7, 'gridCol': 7, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wR'},
    'c1': {'square': 'c1', 'file': 'c', 'rank': 1, 'gridRow': 7, 'gridCol': 2, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wB'},
    'g1': {'square': 'g1', 'file': 'g', 'rank': 1, 'gridRow': 7, 'gridCol': 6, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wB'},
    'b1': {'square': 'b1', 'file': 'b', 'rank': 1, 'gridRow': 7, 'gridCol': 1, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wN'},
    'f1': {'square': 'f1', 'file': 'f', 'rank': 1, 'gridRow': 7, 'gridCol': 5, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wN'},
    'd1': {'square': 'd1', 'file': 'd', 'rank': 1, 'gridRow': 7, 'gridCol': 3, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wQ'},
    'e1': {'square': 'e1', 'file': 'e', 'rank': 1, 'gridRow': 7, 'gridCol': 4, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wK'}
}

destination = {'square': 'a5', 'file': 'a', 'rank': 5, 'gridRow': 3, 'gridCol': 0, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': None}

piece_able_to_move = get_piece_able_to_move(pieces, destination)

if piece_able_to_move:
    print(f"The piece on {piece_able_to_move['square']} can move to {destination['square']}")
else:
    print("No piece can move to the destination square")

print(destination)


