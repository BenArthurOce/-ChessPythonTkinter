import re
import inspect

class ParserDict(dict):
    def __init__(self,string, *arg,**kw):
        super(ParserDict, self).__init__(*arg, **kw)
        self._run_parser(string)

    def _run_parser(self, string):

        notation_tuple = self._parse_notation_string_to_notation_tuple(string)
        self._parse_notation_tuple_to_instruction_tuple(notation_tuple)


    def _parse_notation_string_to_notation_tuple(self, notation_string:str) -> dict:
        # self.print_method_call(inspect.currentframe().f_code.co_name)
        regx_pattern = r"\s*(\d{1,3})\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?"
        split_notation = re.split(regx_pattern, notation_string)
        cleaned_notation = [a for a in split_notation if a != '']
        return {int(cleaned_notation[x].replace('.', '')): (tuple(cleaned_notation[x + 1:x + 3])) for x in
                range(0, len(cleaned_notation), 3)}
    

    def _parse_notation_tuple_to_instruction_tuple(self, notation_tupleDict:dict) -> dict:
        # self.print_method_call(inspect.currentframe().f_code.co_name, notation_tupleDict)
        for each_key, each_value in notation_tupleDict.items():
            #each_key is the move number

            self[each_key] = (
                self._parse_move(each_key, each_value[0], "w"),
                self._parse_move(each_key, each_value[1], "b") if each_value[1] else None
            )

    def _parse_move(self, turn_num:int, notation:str, colour:str):
        # self.print_method_call(inspect.currentframe().f_code.co_name, turn_num, notation, colour)
        # print("======_parse_move=====")
        # print(turn_num, notation, colour)
        castling_symbols = {'O-O': 'Kingside', 'O-O-O': 'Queenside'}
        check_symbols = ['+', '#']

        adjusted_notation = str(notation)

        move = {
            'turnnumber': turn_num,
            'notation': notation,
            'colour': colour,
            'piece': None,
            'code': None,
            'location': None,
            'destination': None,
            'castling': None,
            'capture': None,
            'checkormate': None,
            'promotion': None,
            'file': None,
            'rank': None
        }

        # if notation == "cxd4":
        #     print(notation)

        # Code to determine castling
        move['castling'] = castling_symbols.get(adjusted_notation)
        if move['castling']:
            for symbol in check_symbols:
                adjusted_notation = adjusted_notation.strip(symbol)
            return move
        
        # Captures
        if 'x' in adjusted_notation:
            move['capture'] = True
            adjusted_notation = adjusted_notation.replace('x', '')

        # Checks
        if '+' in adjusted_notation:
            move['checkormate'] = adjusted_notation[-1:]
            adjusted_notation = adjusted_notation.replace('+', '')

        # Checkmates 
        if '#' in adjusted_notation:
            move['checkormate'] = adjusted_notation[-1:]
            adjusted_notation = adjusted_notation.replace('#', '')

        # Promotions
        # if '=' in adjusted_notation:
        #     move['promotion'] = adjusted_notation[-1]
        #     adjusted_notation = adjusted_notation.replace('=', '')

        # Destination - remove last 2 characters
        adjusted_notation, move['destination'] = adjusted_notation[:-2], adjusted_notation[-2:]


        if len(adjusted_notation) == 0:
            move['piece'] = 'p'
            move['code'] = move['colour'] + move['piece']
            return move
        
        
        # Extact Major Piece
        if adjusted_notation[0].isupper():
            move['piece'], adjusted_notation  = adjusted_notation[0], adjusted_notation[1:]
            move['code'] = move['colour'] + move['piece']

        # Identify Pawn
        else:
            move['piece'] = 'p'
            move['code'] = move['colour'] + move['piece']


        # if notation == 'Nbd2':
        #     input(adjusted_notation)

        # Remaining Notation is 0, 1, 2 characters of letters, numbers
        if len(adjusted_notation) == 0:
            return move
        
        if len(adjusted_notation) == 1 and adjusted_notation.isnumeric(): # Remaining String Length is 1, and is number
            move['rank'] = adjusted_notation
            return move
        
        if len(adjusted_notation) == 1 and not adjusted_notation.isnumeric(): # Remaining String Length is 1, and is letter
            move['file'] = adjusted_notation
            return move

        if len(adjusted_notation) == 2:
            move['file'], move['rank'] = adjusted_notation[0], adjusted_notation[1]
            return move

    