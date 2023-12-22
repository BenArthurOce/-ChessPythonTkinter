from cls_ChessDictionary import *
from cls_NotationParser import *
from cls_MovesParser import *

class CHESSGAMECLASSTESTING2:
    def __init__(self, notation_string:str):
        self.notation_string = notation_string
        self._ChessboardDictionary = ChessBoardDictionary()
        self.NotationParser = NotationParser(notation_string)
        self.AllGameMoves = []
        self.process_moves()


    def process_moves(self):
        for turn_num, moves_tuple in self.NotationParser._notation_dict.items():
            if moves_tuple[0] is not None:
                self.AllGameMoves.append(MoveParser(turn_num, moves_tuple[0], "w"))
            if moves_tuple[1] is not None:
                self.AllGameMoves.append(MoveParser(turn_num, moves_tuple[1], "b"))

        # using the details of each move, find the piece that needs to be moved. Return its square location
        for index, each_move in enumerate(self.AllGameMoves):
            if not isinstance(each_move, MoveParser):
                raise TypeError("Element number {0} (base 0) of the self.AllGameMoves list is not a MoveParser class")
            else:           
                if each_move.castling == None:
                    each_move.location = self.get_piece_starting_location(each_move)
                    self._ChessboardDictionary.move_piece_standard(each_move.code, each_move.location, each_move.destination)
                else: 
                    self._ChessboardDictionary.move_piece_castling(each_move.colour, each_move.castling)


    def get_piece_starting_location(self, each_move_details:MoveParser):
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\teach_move_detail={0}  \n".format(each_move_details.print_attributes_dict()))

        if not isinstance(each_move_details, MoveParser):
            raise TypeError("the variable 'each_move_details' must be passed as a MoveParser class")


        all_active_squares = [value for key, value in self._ChessboardDictionary.items() if value.get("pieceObj") is not None]   # All Chess Squares with a piece on them                                                                          # Information about the piece and its colour
        destination_square_dict = self._ChessboardDictionary[each_move_details.destination]                                  # Information about where the piece is going

        for each_piece_location in all_active_squares:


            if each_move_details.code == 'wR' and each_piece_location['pieceObj'] == 'wR' and self.is_valid_rook_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'wB' and each_piece_location['pieceObj'] == 'wB' and self.is_valid_bishop_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'wN' and each_piece_location['pieceObj'] == 'wN' and self.is_valid_knight_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'wQ' and each_piece_location['pieceObj'] == 'wQ' and self.is_valid_queen_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'wK' and each_piece_location['pieceObj'] == 'wK' and self.is_valid_king_move2(each_piece_location, each_move_details):
                return each_piece_location['square']

            if each_move_details.code == 'bR' and each_piece_location['pieceObj'] == 'bR' and self.is_valid_rook_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'bB' and each_piece_location['pieceObj'] == 'bB' and self.is_valid_bishop_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'bN' and each_piece_location['pieceObj'] == 'bN' and self.is_valid_knight_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'bQ' and each_piece_location['pieceObj'] == 'bQ' and self.is_valid_queen_move2(each_piece_location, each_move_details):
                return each_piece_location['square']
            elif each_move_details.code == 'bK' and each_piece_location['pieceObj'] == 'bK' and self.is_valid_king_move2(each_piece_location, each_move_details):
                return each_piece_location['square']

            elif each_move_details.code == 'wp' and each_piece_location['pieceObj'] == 'wp' and self.is_valid_pawn_move2(each_piece_location, each_move_details, destination_square_dict, True):
                return each_piece_location['square']
            elif each_move_details.code == 'bp' and each_piece_location['pieceObj'] == 'bp' and self.is_valid_pawn_move2(each_piece_location, each_move_details, destination_square_dict, False):
                return each_piece_location['square']


        
    def reset_board(self):
        self._ChessboardDictionary.reset_starting_pieces()



            

    def is_valid_pawn_move2(self, pawn, move_info:MoveParser, destination:dict, is_white:bool) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tpawn={0}, \n\tmove={1}, \n\tdest={2}, \n\tis_white={3} \n".format(pawn, move_info.print_attributes_dict(), destination, is_white))

        if not isinstance(pawn, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - pawn must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))
        
        file_diff = pawn['gridCol'] - destination['gridCol']
        rank_diff = pawn['gridRow'] - destination['gridRow']

        if move_info.capture == "x":
            if move_info.file == pawn['file']:
                return True 
            else:
                return False


        # c4 is getting scanned and approved before d4 can be scanned
        if move_info.capture == "x" and move_info.file == pawn.file:
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


    def is_valid_rook_move2(self, rook, move_info:MoveParser) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\trook={0}, \n\tmove={1} \n".format(rook, move_info.print_attributes_dict()))

        if not isinstance(rook, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - rook must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))
        
        destination = move_info.destination
        return rook['rank'] == int(destination[1]) or rook['file'] == ord(destination[0])
    

    def is_valid_bishop_move2(self, bishop, move_info:MoveParser) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tbishop={0}, \n\tmove={1} \n".format(bishop, move_info.print_attributes_dict()))

        if not isinstance(bishop, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - bishop must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))
        
        destination = move_info.destination
        return abs(ord(bishop['file']) - ord(destination[0])) == abs(bishop['rank'] - int(destination[1]))



    def is_valid_knight_move2(self, knight, move_info:MoveParser) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tknight={0}, \n\tmove={1} \n".format(knight, move_info.print_attributes_dict()))

        if not isinstance(knight, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - knight must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))

        # if not isinstance(knight, dict):
        #     raise TypeError("knight must be a dictionary")
        # if not isinstance(move_info, dict):
        #     raise TypeError("move_info must be a dictionary")

        # if 'file' not in knight or 'rank' not in knight:
        #     raise ValueError("knight dictionary must contain 'file' and 'rank' keys")
        # if 'destination' not in move_info:
        #     raise ValueError("move_info dictionary must contain 'destination' key")

        # if not isinstance(knight['file'], str) or len(knight['file']) != 1:
        #     raise ValueError("knight['file'] must be a single character")
        # if not isinstance(knight['rank'], int):
        #     raise ValueError("knight['rank'] must be an integer")

        destination = move_info.destination
        if move_info.notation == "Nbd7":
            print(destination)
            # input("Nbd7 found")
        
        # since its the Night on b file. We just match b file

        if move_info.file != None and move_info.rank == None:     #two knights can go to the same square
            if knight.file == move_info.file:
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

    def is_valid_queen_move2(self, queen, move_info:MoveParser) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tqueen={0}, \n\tmove={1} \n".format(queen, move_info.print_attributes_dict()))

        if not isinstance(queen, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - queen must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))
        
        return self.is_valid_rook_move2(queen, move_info) or self.is_valid_bishop_move2(queen, move_info) #Queens can move like bishops and knights
    

    def is_valid_king_move2(self, king, move_info:MoveParser) -> bool:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: \n\tking={0}, \n\tmove={1} \n".format(king, move_info.print_attributes_dict()))

        if not isinstance(king, dict):
            raise TypeError("turn:{0}, piece:{1}, notation:{2} - king must be a dictionary"
                            .format(move_info.turn_number, move_info.code, move_info.notation))

        destination = move_info.destination
        return abs(ord(king['file']) - ord(destination[0])) <= 1 and abs(king['rank'] - int(destination[1])) <= 1

