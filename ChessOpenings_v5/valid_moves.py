import inspect

def get_piece_able_to_move(chessboard_dict:dict, destination_square_dict, piece_code_name:str):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tchessboard_dict={0}, \n\tdest_square={1} \n\tpiece_code_name={2} \n".format("Ommitted", destination_square_dict, piece_code_name))

    # get all squares that have a piece on them
    all_pieces = [value for key, value in chessboard_dict.items() if value.get("pieceObj") != None]

    for each_piece_location in all_pieces:
        if piece_code_name == 'wR' and each_piece_location['pieceObj'] == 'wR' and is_valid_rook_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'wB' and each_piece_location['pieceObj'] == 'wB' and is_valid_bishop_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'wN' and each_piece_location['pieceObj'] == 'wN' and is_valid_knight_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'wQ' and each_piece_location['pieceObj'] == 'wQ' and is_valid_queen_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'wK' and each_piece_location['pieceObj'] == 'wK' and is_valid_king_move(each_piece_location, destination_square_dict):
            return each_piece_location

        if piece_code_name == 'bR' and each_piece_location['pieceObj'] == 'bR' and is_valid_rook_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'bB' and each_piece_location['pieceObj'] == 'bB' and is_valid_bishop_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'bN' and each_piece_location['pieceObj'] == 'bN' and is_valid_knight_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'bQ' and each_piece_location['pieceObj'] == 'bQ' and is_valid_queen_move(each_piece_location, destination_square_dict):
            return each_piece_location
        elif piece_code_name == 'bK' and each_piece_location['pieceObj'] == 'bK' and is_valid_king_move(each_piece_location, destination_square_dict):
            return each_piece_location

        elif piece_code_name == 'wp' and each_piece_location['pieceObj'] == 'wp' and is_valid_pawn_move(each_piece_location, destination_square_dict, True):
            return each_piece_location
        elif piece_code_name == 'bp' and each_piece_location['pieceObj'] == 'bp' and is_valid_pawn_move(each_piece_location, destination_square_dict, False):
            return each_piece_location
        
    # if nothing returned:

    raise ValueError("There was no {0} that was able to move to {1}".format(piece_code_name, destination_square_dict['square']))



def is_valid_pawn_move(pawn, destination, is_white):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tpawn={0}, \n\tdest={1} \n".format(pawn, destination))



    file_diff = pawn['gridCol'] - destination['gridCol']
    rank_diff = pawn['gridRow'] - destination['gridRow']

    # if destination['square'] == "e5":
    #     print(file_diff)
    #     print(rank_diff)
    #     input("hi")

    if is_white:
        # White pawn can move forward by 1 rank
        if file_diff == 0 and rank_diff == 1:
            return True
        # White pawn can move forward by 2 ranks from its starting position
        if pawn['gridRow'] == 6 and file_diff == 0 and rank_diff == 2:
            return True
        # White pawn can capture diagonally if something is on it
        if abs(file_diff) == 1 and rank_diff == 1 and destination['pieceObj'] != None:
            return True
    else:
        # Black pawn can move forward by 1 rank
        if file_diff == 0 and rank_diff == -1:
            return True
        # Black pawn can move forward by 2 ranks from its starting position
        if pawn['gridRow'] == 1 and file_diff == 0 and rank_diff == -2:
        # if pawn['rank'] == 6 and file_diff == 0 and rank_diff == -2:
            return True
        # Black pawn can capture diagonally if something is on it
        if abs(file_diff) == 1 and rank_diff == -1 and destination['pieceObj'] != None:
            return True
    
    return False


def is_valid_rook_move(rook, destination):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\trook={0}, \n\tdest={1} \n".format(rook, destination))
    return rook['rank'] == destination['rank'] or rook['file'] == destination['file']

def is_valid_bishop_move(bishop, destination):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tbishop={0}, \n\tdest={1} \n".format(bishop, destination))
    return abs(ord(bishop['file']) - ord(destination['file'])) == abs(bishop['rank'] - destination['rank'])

def is_valid_knight_move(knight, destination):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tknight={0}, \n\tdest={1} \n".format(knight, destination))
    return (abs(ord(knight['file']) - ord(destination['file'])) == 2 and abs(knight['rank'] - destination['rank']) == 1) or \
           (abs(ord(knight['file']) - ord(destination['file'])) == 1 and abs(knight['rank'] - destination['rank']) == 2)

def is_valid_queen_move(queen, destination):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tqueen={0}, \n\tdest={1} \n".format(queen, destination))
    return is_valid_rook_move(queen, destination) or is_valid_bishop_move(queen, destination) #Queens can move like bishops and knights

def is_valid_king_move(king, destination):
    print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
    print("\t [Variables]: \n\tking={0}, \n\tdest={1} \n".format(king, destination))
    return abs(ord(king['file']) - ord(destination['file'])) <= 1 and abs(king['rank'] - destination['rank']) <= 1