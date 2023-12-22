#credit https://github.com/tomgp/chess-canvas/blob/master/pgn/chess_openings_adjusted.csv

import re
import inspect

import csv



class Openings(dict):
    def __init__(self, *arg, **kw):
        super(Openings, self).__init__(*arg, **kw)
        self.read_from_csv_file()  # Call the method at the end of the __init__ method

    def read_from_csv_file(self):
        csv_filename = r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\chess_moves3.csv"

        # Open CSV and read
        with open(csv_filename) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                key = row['PGN']
                volume = row['VOLUME']
                eco = row['ECO']
                name = row['NAME']

        # Transpose CSV Contents into Dictionary
                self[key] = {  
                     'VOLUME': volume
                    ,'ECO': eco
                    ,'NAME': name
                    ,'PGN': key
                    ,'PARSER' : None
                }

        # Add the Chess Parser object to the dictionary
        for each_key, each_value in self.items():
            self[each_key]['PARSER'] = ChessParser(each_key) 



    def filter_opening_dict(self, search_category:str, search_item:str, move_number=None) -> dict:
        """Search the openings for dictionary entries that match pgn, moves, eco, volume or name"""
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: search_category= {0}, search_item= {1}, move_number= {2}\n".format(search_category, search_item, move_number))

        result = ''
        match search_category.upper():
            case "PGN":
                result = {key: value for key, value in self.items() if key == search_item}
            case "MOVESTART":
                result = {key: value for key, value in self.items() if key.startswith(search_item)}
            case "ECO":
                result = {key: value for key, value in self.items() if value.get("ECO") == search_item.upper()}
            case "VOLUME":
                result = {key: value for key, value in self.items() if value.get("VOLUME") == search_item}
            case "NAME":
                result = {key: value for key, value in self.items() if value.get("NAME") == search_item}
            case _:
                raise ValueError("Search category: {0} is not a valid search term".format(search_category))

        # Stop Code, return error if nothing was found from the filter
        if not result:
            raise ValueError("No Entries found when filtering the dictionary")

        # if user nominated a turn number, filter further to find dictionary lines containing that turn number
        if move_number != None:
            # result = {key: value for key, value in result.items() if any(k >= move_number for k in value['MOVES'].keys())}
            result = {key: value for key, value in result.items() if move_number in value['MOVES'].keys()}


            # Stop Code, return error if no lines reached the certain turn number
            if not result:
                raise ValueError("There are no entries for turn {0} when searching for {1} as a {2}".format(move_number, search_item, search_category))

        return result

    def get_continuations(self, pgn_string) -> list:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: pgn_string= {0}\n".format(pgn_string))

        all_continuations = []
        filtered_openings = self.filter_opening_dict("MOVESTART", pgn_string)
        input(filtered_openings)
        for each_key, each_value in filtered_openings.items():
            if each_value['ECO'] in each_value['NAME']:
                all_continuations.append(each_value['ECO'])
        
        return all_continuations

    def get_continuations2(self, pgn_string) -> dict:
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: pgn_string= {0}\n".format(pgn_string))

        all_continuations = {}
        filtered_openings = self.filter_opening_dict("MOVESTART", pgn_string)
        for each_key, each_value in filtered_openings.items():
            if each_value['ECO'] in each_value['NAME']:
                all_continuations[each_key] = each_value

        return all_continuations

    
import re

class ChessParser:
    def __init__(self, notation_string):
        self._notation_string = notation_string
        self._notation_dict = {}
        self.run_parser()

    @property
    def notation_string(self):
        return self._notation_string

    @notation_string.setter
    def notation_string(self, new_notation_string):
        self._notation_string = new_notation_string
        self.run_parser()

    @property
    def notation_dict(self):
        return self._notation_dict

    def run_parser(self):
        tupleDict = self.parse_notation_string_to_notation_tuple()
        self.parse_notation_tuple_to_instruction_tuple(tupleDict)
        

    def parse_notation_string_to_notation_tuple(self) -> dict:
        # source: https://stackoverflow.com/questions/23638515/regex-challenge-custom-chess-notation
        regx_pattern = r"\s*(\d{1,3})\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?"
        split_notation = re.split(regx_pattern, self._notation_string)

        cleaned_notation = [a for a in split_notation if a != '']
        return  {int(cleaned_notation[x].replace('.','')):(tuple(cleaned_notation[x+1:x+3])) for x in range(0,len(cleaned_notation),3)}


    def parse_notation_tuple_to_instruction_tuple(self, notation_tupleDict:dict) -> dict:
        for each_key, each_value in notation_tupleDict.items():

            move_number = each_key
            white_move = each_value[0]
            black_move = each_value[1]
            

            self._notation_dict[move_number] = (
                self._parse_move(move_number, white_move, "w"),
                self._parse_move(move_number, black_move, "b") if black_move else None
            )


    def _parse_move(self, turn_num, notation, colour):
        castling_symbols = {'O-O': 'Kingside', 'O-O-O': 'Queenside'}
        check_symbols = ['+', '#']

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

        original_notation = str(notation)

        move['castling'] = castling_symbols.get(original_notation)

        if move['castling']:
            for symbol in check_symbols:
                original_notation = original_notation.strip(symbol)
            return move

        if 'x' in original_notation:
            move['capture'] = True
            original_notation = original_notation.replace('x', '')

        if '+' in original_notation:
            move['checkormate'] = original_notation[-1:]
            original_notation = original_notation.replace('+', '')

        if '#' in original_notation:
            move['checkormate'] = original_notation[-1:]
            original_notation = original_notation.replace('#', '')

        if '=' in original_notation:
            move['promotion'] = original_notation[-1]
            original_notation = original_notation.replace('=', '')

        original_notation, move['destination'] = original_notation[:-2], original_notation[-2:]

        if original_notation.islower() and len(original_notation) == 1:
            move['piece'] = 'p'
            move['file'] = original_notation
            move['code'] = move['colour'] + move['piece']
            return move

        if len(original_notation) == 1:
            move['piece'] = original_notation
            move['code'] = move['colour'] + move['piece']
        elif len(original_notation) == 2:
            if any(char.isdigit() for char in original_notation):
                move['piece'], move['rank'] = original_notation[:-1], original_notation[-1:]
            else:
                move['piece'], move['file'] = original_notation[:-1], original_notation[-1:]
            move['code'] = move['colour'] + move['piece']
        elif len(original_notation) == 3:
            move['piece'], move['file'], move['rank'] = list(original_notation)
            move['code'] = move['colour'] + move['piece']

        if move['piece'] is None:
            move['piece'] = 'p'
            move['code'] = move['colour'] + move['piece']

        if move['notation'] == '':
            move['notation'] = None
            move['colour'] = None
            move['piece'] = None
            move['destination'] = None
            move['code'] = None

        return move

    def __str__(self):
        return str(self._notation_dict)
        