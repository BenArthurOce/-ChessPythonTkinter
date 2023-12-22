
from cls_OpeningsDict import OpeningsDict
from cls_ChessboardDict import ChessboardDict

class ChessGameLogic:
    def __init__(self, OpeningsDictionary:OpeningsDict, string_notation:str):
        self.string_notation = string_notation
        self.openings_information = OpeningsDictionary[string_notation]
        self.ChessDictionary = ChessboardDict()

        self.get_piece_locations()


    def return_game_ECO(self):
        # input(self.openings_information)
        return self.openings_information['ECO']

    def return_game_name(self):
        # input(self.openings_information)
        return self.openings_information['NAME']

    def return_game_notation(self):
        # input(self.openings_information)
        return self.openings_information['PGN']

    def return_game_continuationname(self):
        # input(self.openings_information)
        return self.openings_information['CONTINUATIONNAME']

    def get_piece_locations(self):
        parser_information = self.openings_information['PARSER']
        for turn_num, (move1, move2) in parser_information.items():

            if move1 != None:
                if move1['castling'] == None:
                    move1['location'] = self._get_piece_starting_location(move1)

                    self.ChessDictionary.move_piece_standard(move1['code'], move1['location'], move1['destination'])
                else:
                    self.ChessDictionary.move_piece_castling(move1['colour'], move1['castling'])

            if move2 != None:
                if move2['castling'] == None:
                    move2['location'] = self._get_piece_starting_location(move2)

                    self.ChessDictionary.move_piece_standard(move2['code'], move2['location'], move2['destination'])
                else:
                    self.ChessDictionary.move_piece_castling(move2['colour'], move2['castling'])



    def _get_piece_starting_location(self, each_move_details:dict) -> str:
        # self.print_method_call(inspect.currentframe().f_code.co_name, each_move_details)
        piece_validations = {
            'p': self._is_valid_pawn_move,
            'B': self._is_valid_bishop_move,
            'N': self._is_valid_knight_move,
            'R': self._is_valid_rook_move,
            'K': self._is_valid_king_move,
            'Q': self._is_valid_queen_move,
        }

        validation_func = piece_validations[each_move_details['piece']]
        possible_pieces = self.ChessDictionary.get_filter_list_by_piececode(each_move_details['code'])

        for each_piece_location in possible_pieces:
            if validation_func(each_piece_location, each_move_details):
                return each_piece_location['square']
            
        # No piece was found
        raise ValueError("No piece was found.")

        # raise ValueError("No piece was found.\nDetails:\n\t{0}\nNotation:\n\t{1}\nDetails:\n\t{2}".format(each_move_details, self.string_notation, self.print_dictionary_board_debug()))

    # def reset_board(self):
    #     self.ChessboardDictionary.reset_starting_pieces()

    def _get_file_rank_differences(self, piece_square:dict, move_info:dict) -> tuple:
        letter_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        file_diff = letter_to_num[piece_square['file']] - letter_to_num[move_info['destination'][0]]
        rank_diff = piece_square['rank'] - int(move_info['destination'][1])
        return file_diff, rank_diff

    def _is_valid_pawn_move(self, pawn:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, pawn, move_info)
        if not isinstance(pawn, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "pawn must be a dictionary")

        file_diff, rank_diff = self._get_file_rank_differences(pawn, move_info)

        if move_info['capture']:
            return pawn['file'] == move_info['file']

        if move_info['colour'] == 'w':
            if file_diff == 0 and rank_diff == -1:
                return True
            if pawn['gridRow'] == 6 and file_diff == 0 and rank_diff == -2:
                return True

        elif move_info['colour'] == 'b':
            if file_diff == 0 and rank_diff == 1:
                return True
            if pawn['gridRow'] == 1 and file_diff == 0 and rank_diff == 2:
                return True

        return False

    def _is_valid_bishop_move(self, bishop:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, bishop, move_info)
        if not isinstance(bishop, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "bishop must be a dictionary")

        file_diff, rank_diff = self._get_file_rank_differences(bishop, move_info)
        return abs(file_diff) == abs(rank_diff)

    def _is_valid_knight_move(self, knight:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, knight, move_info)
        if not isinstance(knight, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "knight must be a dictionary")

        file_diff, rank_diff = self._get_file_rank_differences(knight, move_info)

        if move_info['file'] is not None and move_info['rank'] is None:
            return knight['file'] == move_info['file']

        return (abs(file_diff) == 1 and abs(rank_diff) == 2) or (abs(file_diff) == 2 and abs(rank_diff) == 1)

    def _is_valid_rook_move(self, rook:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, rook, move_info)
        if not isinstance(rook, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "rook must be a dictionary")
        
        file_diff, rank_diff = self._get_file_rank_differences(rook, move_info)
        return file_diff == 0 or rank_diff == 0

    def _is_valid_king_move(self, king:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, king, move_info)
        if not isinstance(king, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "king must be a dictionary")

        file_diff, rank_diff = self._get_file_rank_differences(king, move_info)
        return abs(file_diff) <= 1 and abs(rank_diff) <= 1

    def _is_valid_queen_move(self, queen:dict, move_info:dict) -> bool:
        # self.print_method_call(inspect.currentframe().f_code.co_name, queen, move_info)
        if not isinstance(queen, dict):
            raise TypeError(f"turn: {move_info['turnnumber']}, piece: {move_info['code']}, notation: {move_info['notation']} - "
                            "queen must be a dictionary")

        return self._is_valid_rook_move(queen, move_info) or self._is_valid_bishop_move(queen, move_info)


    def print_dictionary_board_debug(self):
        chessboard = self.ChessDictionary.get_dictionary_as_lists()

        board = (
            '\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '8 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '7 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '6 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '5 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '4 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '3 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '2 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '1 │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │\n'
            '──│────│────│────│────│────│────│────│────│\n'
            '  │  a │  b │  c │  d │  e │  f │  g │  h │\n'
        ).format(*chessboard[0], *chessboard[1], *chessboard[2], *chessboard[3], *chessboard[4], *chessboard[5], *chessboard[6], *chessboard[7])
        print(board)