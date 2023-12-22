#credit https://github.com/tomgp/chess-canvas/blob/master/pgn/chess_openings_adjusted.csv

import re
import inspect

import csv


class Openings(dict):
    def __init__(self,*arg,**kw):
        super(Openings, self).__init__(*arg, **kw)
        self = {}


    def populate_dictionary(self):
        """Populates a opening move dictionary using CSV file"""
        print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
        print("\t [Variables]: None \n".format())

        csv_filename = r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\chess_moves3.csv"
        with open(csv_filename) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                key = row['PGN']
                volume = row['VOLUME']
                eco = row['ECO']
                name = row['NAME']
                move_dict = self.convert_notation_into_move_dict(key)

                self[key] = {  
                     'VOLUME': volume
                    ,'ECO': eco
                    ,'NAME': name
                    ,'MOVES': move_dict
                }

    def convert_notation_into_move_dict(self, pgn_string) -> dict:
        """Takes a chess PGN string and converts it into a nested dictionary. KEY: Move Number  VALUE: White,Black move in tuple"""
        # print("[Current Function]: {0}".format(inspect.stack()[0][3]))   #Removed because adds a slow 2700 print lines to terminal
        # print("\t [Variables]: None \n".format())
        # source: https://stackoverflow.com/questions/23638515/regex-challenge-custom-chess-notation

        regx_pattern = r"\s*(\d{1,3})\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?"
        split_notation = re.split(regx_pattern, pgn_string)

        cleaned_notation = [a for a in split_notation if a != '']
        each_move = {int(cleaned_notation[x].replace('.','')):(tuple(cleaned_notation[x+1:x+3])) for x in range(0,len(cleaned_notation),3)}
        return each_move


    def filter_opening_dict(self, search_category:str, search_item:str, move_number=None):
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
            # result = {key: value for key, value in result.items() if move_number in value['MOVES'].keys()}
            result = {key: value for key, value in result.items() if any(k >= move_number for k in value['MOVES'].keys())}


            # Stop Code, return error if no lines reached the certain turn number
            if not result:
                raise ValueError("There are no entries for turn {0} when searching for {1} as a {2}".format(move_number, search_item, search_category))

        return result

