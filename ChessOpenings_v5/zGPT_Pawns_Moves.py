import inspect
from valid_moves import *

def is_valid_pawn_move(pawn, destination, is_white):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: pawn={0}, destination={1} \n".format(pawn, destination))

    file_diff = ord(destination['file']) - ord(pawn['file'])
    rank_diff = destination['rank'] - pawn['rank']
    
    if is_white:
        # White pawn can move forward by 1 rank
        if file_diff == 0 and rank_diff == 1:
            return True
        # White pawn can move forward by 2 ranks from its starting position
        if pawn['rank'] == 1 and file_diff == 0 and rank_diff == 2:
            return True
        # White pawn can capture diagonally
        if abs(file_diff) == 1 and rank_diff == 1:
            return True
    else:
        # Black pawn can move forward by 1 rank
        if file_diff == 0 and rank_diff == -1:
            return True
        # Black pawn can move forward by 2 ranks from its starting position
        if pawn['rank'] == 6 and file_diff == 0 and rank_diff == -2:
            return True
        # Black pawn can capture diagonally
        if abs(file_diff) == 1 and rank_diff == -1:
            return True
    
    return False

def get_piece_able_to_move(chessboard_dict:dict, destination_square:str, piece_code_name:str):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: chessboard_dict={0}, destination={1}, piece_code_name={2} \n".format("Ommitted", destination_square, piece_code_name))

    # get all squares that have a piece on them
    all_pieces = [value for key, value in chessboard_dict.items() if value.get("pieceObj") != None]

    for each_piece_location in all_pieces:
        if piece_code_name == 'wR' and each_piece_location['pieceObj'] == 'wR' and is_valid_rook_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'wB' and each_piece_location['pieceObj'] == 'wB' and is_valid_bishop_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'wN' and each_piece_location['pieceObj'] == 'wN' and is_valid_knight_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'wQ' and each_piece_location['pieceObj'] == 'wQ' and is_valid_queen_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'wK' and each_piece_location['pieceObj'] == 'wK' and is_valid_king_move(each_piece_location, destination_square):
            return each_piece_location

        if piece_code_name == 'bR' and each_piece_location['pieceObj'] == 'bR' and is_valid_rook_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'bB' and each_piece_location['pieceObj'] == 'bB' and is_valid_bishop_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'bN' and each_piece_location['pieceObj'] == 'bN' and is_valid_knight_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'bQ' and each_piece_location['pieceObj'] == 'bQ' and is_valid_queen_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'bK' and each_piece_location['pieceObj'] == 'bK' and is_valid_king_move(each_piece_location, destination_square):
            return each_piece_location
        elif piece_code_name == 'wP' and each_piece_location['pieceObj'] == 'wP' and is_valid_pawn_move(each_piece_location, destination_square, True):
            return each_piece_location
        elif piece_code_name == 'bP' and each_piece_location['pieceObj'] == 'bP' and is_valid_pawn_move(each_piece_location, destination_square, False):
            return each_piece_location
