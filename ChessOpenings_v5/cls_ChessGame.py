from cls_ChessDictionary import *

from cls_NotationParser import *

class ChessGame:
    def __init__(self):
        self._ChessboardDictionary = ChessBoardDictionary()
        self._notationString = ''
        self._notationDict = {}

    @property
    def ChessboardDictionary(self):
        return self._ChessboardDictionary

    @ChessboardDictionary.setter
    def ChessboardDictionary(self, value):
        self._ChessboardDictionary = value

    @property
    def notationString(self):
        return self._notationString

    @notationString.setter
    def notationString(self, value):
        if isinstance(value, str) and value != '':
            self._notationString = value
        else:
            raise ValueError("notationString must be a non-empty string")

    @property
    def notationDict(self):
        return self._notationDict

    @notationDict.setter
    def notationDict(self, value):
        self._notationDict = value

    def parse_notation(self):
        parser = NotationParser(self._notationString)
        self._notationDict = parser.notation_dict


    def process_all_moves(self, moves_to_execute:list):


        # new version
        for each_move_dict in moves_to_execute:
            if each_move_dict['castling'] is None:
                piece_info = self.get_piece_able_to_move2(each_move_dict)
                if piece_info is None:
                    raise ValueError("No piece able to move for the given move information: {0}".format(each_move_dict))
                each_move_dict['location'] = piece_info['square']
                self.move_piece2(each_move_dict)
            elif each_move_dict['castling'] is not None:
                self.move_castling(colour=each_move_dict['colour'],side=each_move_dict['castling'])
                pass




    def move_piece2(self, each_move_dict:dict):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\teach_move_dict={0} \n".format(each_move_dict))

        piece_to_move = each_move_dict['colour'] + each_move_dict['piece']
        current_square_string = each_move_dict['location']
        current_square_dict = self.ChessboardDictionary[current_square_string]
        destination_square_string = each_move_dict['destination']
        destination_square_dict = self.ChessboardDictionary[destination_square_string]

        if piece_to_move != current_square_dict["pieceObj"]:
            raise ValueError("You attempted to move a {0} on {1}, but there is a {2} there".format(piece_to_move, destination_square_dict['square'], destination_square_dict['pieceObj']))
        else:
            self.ChessboardDictionary[current_square_dict["square"]]["pieceObj"] = None
            self.ChessboardDictionary[destination_square_dict["square"]]["pieceObj"] = piece_to_move
        pass
        
    def reset_board(self):
        self.ChessboardDictionary.reset_starting_pieces()


    def process_notation(self, notation:str, colour:str) -> dict:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: notation={0}, colour={1} \n".format(notation, colour))

        # results of the different moves will be stored in a dictionary (location will not be populated here)
        move_details = {'notation':notation, 'colour': colour, 'piece': None, 'code': None, 'location':None, 'destination': None, 
                        'castling': None, 'capture': None, 'checkormate': None, 'promotion': None, 'file': None, 'rank': None}
        
        castling_symbols = {'O-O': 'Kingside', 'O-O-O': 'Queenside'}
        check_symbols = ['+', '#']

        pause = False
        orig_notaiton = ''
        if notation == "Nbd7":
            pause == True
            orig_notaiton = notation

    
        if notation == "O-O" or notation == "O-O-O": # if castle
            if notation == "O-O":
                move_details['castling'] = 'Kingside'
            elif notation == "O-O-O":
                move_details['castling'] = 'Queenside'
        
            #then check for check/checkmate symobol, and leave function
            if any(symbol in notation for symbol in ["+", "#"]): # if check or checkmate remove the symbol from notation
                notation, move_details['destination'] = notation[:-1], notation[-1:] 
            return move_details

        for symbol in check_symbols:
            if symbol in notation:
                move_details['checkormate'] = symbol
                notation = notation.replace(symbol, '')
                break

        if 'x' in notation: # if there is a capture in the notation. Log it and remove the "x"
            move_details['capture'] = 'x'
            notation = notation.replace('x', '')

        # elif any(symbol in notation for symbol in ["+", "#"]): # if check or checkmate remove the symbol from notation
        #     notation, move_details['checkormate'] = notation[:-1], notation[-1:] 

        if '=' in notation: #if there is a promotion, store the promoted piece name and remove the "=" sign
            move_details['promotion'] = notation[-1]
            # notation, move_details['promotion'] = notation[:-1], notation[-1:] #old code. Code above it not yet reviewed
            notation = notation.replace('=', '')
            
        #Split the remaining notation into its moving piece (and rook/file origionality) from the desination square (last 2 characters)
        notation, move_details['destination'] = notation[:-2], notation[-2:]
        
        # if the remaining notation has no capital letters, its a pawn.
        if notation.islower() and len(notation) == 1:
            move_details['piece'] = 'p'
            move_details['file'] = notation
            move_details['code'] = move_details['colour'] + move_details['piece']
            return move_details

        if len(notation) == 1:
            move_details['piece'] = notation
            move_details['code'] = move_details['colour'] + move_details['piece']
        elif len(notation) == 2 and any(char.isdigit() for char in notation): # this means that two pieces share the same file and either can move to the rank
            move_details['piece'], move_details['rank'] = notation[:-1], notation[-1:] 
            move_details['code'] = move_details['colour'] + move_details['piece']
        elif len(notation) == 2: # this means that two pieces share the same rank and either can move to the file
            # print(orig_notaiton)
            # print(notation)
            # input(pause)
            move_details['piece'], move_details['file'] = notation[:-1], notation[-1:]
            move_details['code'] = move_details['colour'] + move_details['piece']
        elif len(notation) == 3: # two queens, two bishops or three pieces can all go to the same square
            move_details['piece'], move_details['file'], move_details['rank'] = list(notation) 
            move_details['code'] = move_details['colour'] + move_details['piece']

        # if piece is "None", its a pawn
        if move_details['piece'] == None:
            move_details['piece'] = 'p'
            move_details['code'] = move_details['colour'] + move_details['piece']
        return move_details


    def move_piece (self, current_square_dict:dict, destination_square_dict:dict, piece_to_move:str):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tcurr_square={0}, \n\tdest_square={1} \n\tpiece_to_move={2} \n".format(current_square_dict, destination_square_dict, piece_to_move))
        if piece_to_move != current_square_dict["pieceObj"]:
            raise ValueError("You attempted to move a {0} on {1}, but there is a {2} there".format(piece_to_move, destination_square_dict['square'], destination_square_dict['pieceObj']))
        else:
            self.ChessboardDictionary[current_square_dict["square"]]["pieceObj"] = None
            self.ChessboardDictionary[destination_square_dict["square"]]["pieceObj"] = piece_to_move
        pass


    def move_castling(self, colour:str, side:str):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: colour={0}, side={1} \n".format(colour, side))

        castling_moves = {
            'w': {
                'Kingside': [("h1", None), ("e1", None), ("f1", "wR"), ("g1", "wK")],
                'Queenside': [("a1", None), ("e1", None), ("d1", "wR"), ("c1", "wK")]
            },
            'b': {
                'Kingside': [("h8", None), ("e8", None), ("f8", "bR"), ("g8", "bK")],
                'Queenside': [("a8", None), ("e8", None), ("d8", "bR"), ("c8", "bK")]
            }
        }

        for move in castling_moves[colour][side]:
            position, piece = move
            self.ChessboardDictionary[position]["pieceObj"] = piece



    def get_piece_able_to_move2(self, each_move_dict: dict):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\teach_move_dict={0}  \n".format(each_move_dict))

        if not isinstance(each_move_dict, dict):
            raise TypeError("each_move_dict must be a dictionary")

        required_keys = ['code', 'destination']
        if not all(key in each_move_dict for key in required_keys):
            raise ValueError("each_move_dict is missing one or more required keys: {0}".format(required_keys))

        # move_details = {'notation':notation, 'colour': colour, 'piece': None, 'location':None, 'destination': None, 'castling': None,
        #                 'capture': None, 'checkormate': None, 'promotion': None, 'file': None, 'rank': None}

        all_active_squares = [value for key, value in self.ChessboardDictionary.items() if value.get("pieceObj") is not None]   # All Chess Squares with a piece on them                                                                          # Information about the piece and its colour
        destination_square_dict = self.ChessboardDictionary[each_move_dict['destination']]                                  # Information about where the piece is going

        for each_piece_location in all_active_squares:


            if each_move_dict['code'] == 'wR' and each_piece_location['pieceObj'] == 'wR' and self.is_valid_rook_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'wB' and each_piece_location['pieceObj'] == 'wB' and self.is_valid_bishop_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'wN' and each_piece_location['pieceObj'] == 'wN' and self.is_valid_knight_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'wQ' and each_piece_location['pieceObj'] == 'wQ' and self.is_valid_queen_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'wK' and each_piece_location['pieceObj'] == 'wK' and self.is_valid_king_move2(each_piece_location, each_move_dict):
                return each_piece_location

            if each_move_dict['code'] == 'bR' and each_piece_location['pieceObj'] == 'bR' and self.is_valid_rook_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'bB' and each_piece_location['pieceObj'] == 'bB' and self.is_valid_bishop_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'bN' and each_piece_location['pieceObj'] == 'bN' and self.is_valid_knight_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'bQ' and each_piece_location['pieceObj'] == 'bQ' and self.is_valid_queen_move2(each_piece_location, each_move_dict):
                return each_piece_location
            elif each_move_dict['code'] == 'bK' and each_piece_location['pieceObj'] == 'bK' and self.is_valid_king_move2(each_piece_location, each_move_dict):
                return each_piece_location

            elif each_move_dict['code'] == 'wp' and each_piece_location['pieceObj'] == 'wp' and self.is_valid_pawn_move2(each_piece_location, each_move_dict, destination_square_dict, True):
                return each_piece_location
            elif each_move_dict['code'] == 'bp' and each_piece_location['pieceObj'] == 'bp' and self.is_valid_pawn_move2(each_piece_location, each_move_dict, destination_square_dict, False):
                return each_piece_location

            

    def is_valid_pawn_move2(self, pawn, move_info:dict, destination, is_white):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tpawn={0}, \n\tmove={1}, \n\tdest={2}, \n\tis_white={3} \n".format(pawn, move_info, destination, is_white))


        file_diff = pawn['gridCol'] - destination['gridCol']
        rank_diff = pawn['gridRow'] - destination['gridRow']

        if move_info['capture'] == "x":
            if move_info['file'] == pawn['file']:
                return True 
            else:
                return False


        # c4 is getting scanned and approved before d4 can be scanned
        if move_info['capture'] == "x" and move_info['file'] == pawn['file']:
            # input("capture")
            return True       

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
            # if abs(file_diff) == 1 and rank_diff == 1 and destination['pieceObj'] != None:
            #     return True
        else:
            # Black pawn can move forward by 1 rank
            if file_diff == 0 and rank_diff == -1:
                return True
            # Black pawn can move forward by 2 ranks from its starting position
            if pawn['gridRow'] == 1 and file_diff == 0 and rank_diff == -2:
            # if pawn['rank'] == 6 and file_diff == 0 and rank_diff == -2:
                return True
            # Black pawn can capture diagonally if something is on it
            # if abs(file_diff) == 1 and rank_diff == -1 and destination['pieceObj'] != None:
            #     return True
        
        return False


    def is_valid_rook_move2(self, rook, move_info):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\trook={0}, \n\tmove={1} \n".format(rook, move_info))

        destination = move_info['destination']
        return rook['rank'] == int(destination[1]) or rook['file'] == ord(destination[0])
        # return rook['rank'] == destination['rank'] or rook['file'] == destination['file']

    def is_valid_bishop_move2(self, bishop, move_info):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tbishop={0}, \n\tmove={1} \n".format(bishop, move_info))
        destination = move_info['destination']
        return abs(ord(bishop['file']) - ord(destination[0])) == abs(bishop['rank'] - int(destination[1]))
        # return abs(ord(bishop['file']) - ord(destination['file'])) == abs(bishop['rank'] - destination['rank'])



    def is_valid_knight_move2(self, knight, move_info):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tknight={0}, \n\tmove={1} \n".format(knight, move_info))

        
        
        if not isinstance(knight, dict):
            raise TypeError("knight must be a dictionary")
        if not isinstance(move_info, dict):
            raise TypeError("move_info must be a dictionary")

        if 'file' not in knight or 'rank' not in knight:
            raise ValueError("knight dictionary must contain 'file' and 'rank' keys")
        if 'destination' not in move_info:
            raise ValueError("move_info dictionary must contain 'destination' key")

        if not isinstance(knight['file'], str) or len(knight['file']) != 1:
            raise ValueError("knight['file'] must be a single character")
        if not isinstance(knight['rank'], int):
            raise ValueError("knight['rank'] must be an integer")

        destination = move_info['destination']
        if move_info['notation'] == "Nbd7":
            print(destination)
            # input("Nbd7 found")
        
        # since its the Night on b file. We just match b file

        if move_info['file'] != None and move_info['rank'] == None:     #two knights can go to the same square
            if knight['file'] == move_info['file']:
                return True
            else:
                return False

        try:
            destination_file = ord(destination[0])
            destination_rank = int(destination[1])
        except (TypeError, ValueError, IndexError):
            raise ValueError("move_info['destination'] is in an invalid format")

        return (abs(ord(knight['file']) - destination_file) == 2 and abs(knight['rank'] - destination_rank) == 1) or \
            (abs(ord(knight['file']) - destination_file) == 1 and abs(knight['rank'] - destination_rank) == 2)


        # return (abs(ord(knight['file']) - ord(destination['file'])) == 2 and abs(knight['rank'] - destination['rank']) == 1) or \
        #     (abs(ord(knight['file']) - ord(destination['file'])) == 1 and abs(knight['rank'] - destination['rank']) == 2)

    def is_valid_queen_move2(self, queen, move_info:dict):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tqueen={0}, \n\tmove={1} \n".format(queen, move_info))
        return self.is_valid_rook_move2(queen, move_info) or self.is_valid_bishop_move2(queen, move_info) #Queens can move like bishops and knights
        # return self.is_valid_rook_move2(queen, destination) or self.is_valid_bishop_move2(queen, destination) #Queens can move like bishops and knights

    def is_valid_king_move2(self, king, move_info:dict):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tking={0}, \n\tmove={1} \n".format(king, move_info))
        destination = move_info['destination']
        return abs(ord(king['file']) - ord(destination[0])) <= 1 and abs(king['rank'] - int(destination[1])) <= 1
        # return abs(ord(king['file']) - ord(destination['file'])) <= 1 and abs(king['rank'] - destination['rank']) <= 1

        # if colour == "w" and side == "Kingside":
        #     self.ChessboardDictionary["h1"]["pieceObj"] = None    # White Kingside Rook
        #     self.ChessboardDictionary["e1"]["pieceObj"] = None    # White King
        #     self.ChessboardDictionary["f1"]["pieceObj"] = "wR"    # White Kingside Rook
        #     self.ChessboardDictionary["g1"]["pieceObj"] = "wK"    # White King
        # if colour == "w" and side == "Queenside":
        #     self.ChessboardDictionary["a1"]["pieceObj"] = None    # White Queenside Rook
        #     self.ChessboardDictionary["e1"]["pieceObj"] = None    # White King
        #     self.ChessboardDictionary["d1"]["pieceObj"] = "wR"    # White Queenside Rook
        #     self.ChessboardDictionary["c1"]["pieceObj"] = "wK"    # White King
        # if colour == "b" and side == "Kingside":
        #     self.ChessboardDictionary["h8"]["pieceObj"] = None    # Black Kingside Rook
        #     self.ChessboardDictionary["e8"]["pieceObj"] = None    # Black King
        #     self.ChessboardDictionary["f8"]["pieceObj"] = "bR"    # Black Kingside Rook
        #     self.ChessboardDictionary["g8"]["pieceObj"] = "bK"    # Black King
        # if colour == "b" and side == "Queenside":
        #     self.ChessboardDictionary["a8"]["pieceObj"] = None    # Black Queenside Rook
        #     self.ChessboardDictionary["e8"]["pieceObj"] = None    # Black King
        #     self.ChessboardDictionary["d8"]["pieceObj"] = "bR"    # Black Queenside Rook
        #     self.ChessboardDictionary["c8"]["pieceObj"] = "bK"    # Black King



# def get_piece_able_to_move(chessboard_dict:dict, destination_square_dict, piece_code_name:str):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tchessboard_dict={0}, \n\tdest_square={1} \n\tpiece_code_name={2} \n".format("Ommitted", destination_square_dict, piece_code_name))

#     # get all squares that have a piece on them
#     all_pieces = [value for key, value in chessboard_dict.items() if value.get("pieceObj") != None]

#     for each_piece_location in all_pieces:
#         if piece_code_name == 'wR' and each_piece_location['pieceObj'] == 'wR' and is_valid_rook_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'wB' and each_piece_location['pieceObj'] == 'wB' and is_valid_bishop_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'wN' and each_piece_location['pieceObj'] == 'wN' and is_valid_knight_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'wQ' and each_piece_location['pieceObj'] == 'wQ' and is_valid_queen_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'wK' and each_piece_location['pieceObj'] == 'wK' and is_valid_king_move(each_piece_location, destination_square_dict):
#             return each_piece_location

#         if piece_code_name == 'bR' and each_piece_location['pieceObj'] == 'bR' and is_valid_rook_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'bB' and each_piece_location['pieceObj'] == 'bB' and is_valid_bishop_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'bN' and each_piece_location['pieceObj'] == 'bN' and is_valid_knight_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'bQ' and each_piece_location['pieceObj'] == 'bQ' and is_valid_queen_move(each_piece_location, destination_square_dict):
#             return each_piece_location
#         elif piece_code_name == 'bK' and each_piece_location['pieceObj'] == 'bK' and is_valid_king_move(each_piece_location, destination_square_dict):
#             return each_piece_location

#         elif piece_code_name == 'wp' and each_piece_location['pieceObj'] == 'wp' and is_valid_pawn_move(each_piece_location, destination_square_dict, True):
#             return each_piece_location
#         elif piece_code_name == 'bp' and each_piece_location['pieceObj'] == 'bp' and is_valid_pawn_move(each_piece_location, destination_square_dict, False):
#             return each_piece_location
        
#     # if nothing returned:

#     raise ValueError("There was no {0} that was able to move to {1}".format(piece_code_name, destination_square_dict['square']))



# def is_valid_pawn_move(pawn, destination, is_white):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tpawn={0}, \n\tdest={1} \n".format(pawn, destination))



#     file_diff = pawn['gridCol'] - destination['gridCol']
#     rank_diff = pawn['gridRow'] - destination['gridRow']

#     # if destination['square'] == "e5":
#     #     print(file_diff)
#     #     print(rank_diff)
#     #     input("hi")

#     if is_white:
#         # White pawn can move forward by 1 rank
#         if file_diff == 0 and rank_diff == 1:
#             return True
#         # White pawn can move forward by 2 ranks from its starting position
#         if pawn['gridRow'] == 6 and file_diff == 0 and rank_diff == 2:
#             return True
#         # White pawn can capture diagonally if something is on it
#         if abs(file_diff) == 1 and rank_diff == 1 and destination['pieceObj'] != None:
#             return True
#     else:
#         # Black pawn can move forward by 1 rank
#         if file_diff == 0 and rank_diff == -1:
#             return True
#         # Black pawn can move forward by 2 ranks from its starting position
#         if pawn['gridRow'] == 1 and file_diff == 0 and rank_diff == -2:
#         # if pawn['rank'] == 6 and file_diff == 0 and rank_diff == -2:
#             return True
#         # Black pawn can capture diagonally if something is on it
#         if abs(file_diff) == 1 and rank_diff == -1 and destination['pieceObj'] != None:
#             return True
    
#     return False


# def is_valid_rook_move(rook, destination):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\trook={0}, \n\tdest={1} \n".format(rook, destination))
#     return rook['rank'] == destination['rank'] or rook['file'] == destination['file']

# def is_valid_bishop_move(bishop, destination):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tbishop={0}, \n\tdest={1} \n".format(bishop, destination))
#     return abs(ord(bishop['file']) - ord(destination['file'])) == abs(bishop['rank'] - destination['rank'])

# def is_valid_knight_move(knight, destination):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tknight={0}, \n\tdest={1} \n".format(knight, destination))
#     return (abs(ord(knight['file']) - ord(destination['file'])) == 2 and abs(knight['rank'] - destination['rank']) == 1) or \
#            (abs(ord(knight['file']) - ord(destination['file'])) == 1 and abs(knight['rank'] - destination['rank']) == 2)

# def is_valid_queen_move(queen, destination):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tqueen={0}, \n\tdest={1} \n".format(queen, destination))
#     return is_valid_rook_move(queen, destination) or is_valid_bishop_move(queen, destination) #Queens can move like bishops and knights

# def is_valid_king_move(king, destination):
#     print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
#     print("\t [Variables]: \n\tking={0}, \n\tdest={1} \n".format(king, destination))
#     return abs(ord(king['file']) - ord(destination['file'])) <= 1 and abs(king['rank'] - destination['rank']) <= 1