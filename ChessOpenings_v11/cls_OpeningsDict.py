#credit https://github.com/tomgp/chess-canvas/blob/master/pgn/chess_openings_adjusted.csv

import re
import inspect

import csv

from cls_ParserDict import ParserDict


# ERROR IN OPENING CSV
#LINE 243
# 1.c4 c5 2.Nc3 Nf6 3.Nf3 Nf6	Vol A: Flank Openings	A34	Four Knights Variation, Symmetrical English




class OpeningsDict(dict):
    def __init__(self, *arg, **kw):
        super(OpeningsDict, self).__init__(*arg, **kw)
        self.read_from_csv_file()  # Call the method at the end of the __init__ method

    def read_from_csv_file(self):
        csv_filename = r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\chess_moves.csv"

        # Open CSV and read
        with open(csv_filename) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                key = row['MOVESKEY']
                volume = row['VOLUME']
                eco = row['ECO']
                name = row['NAME']
                # continuationname = row['CONTINUATIONNAME']

        # Transpose CSV Contents into Dictionary
                self[key] = {  
                     'VOLUME': volume
                    ,'ECO': eco
                    ,'NAME': name
                    ,'CONTINUATIONNAME': ''
                    ,'PGN': key
                    ,'NUMMOVES' : 0
                    ,'CONTINUATION': False
                    ,'PARSER' : None
                    ,'ERROR' : False
                    ,'FAVOURITE' : False
                }

        # Add the Chess Parser object to the dictionary
        for each_key, each_value in self.items():
            self[each_key]['PARSER'] = ParserDict(each_key)

            # Identify if each opening is a continuation or not
            if each_value['ECO'] in each_value['NAME']:
                self[each_key]['CONTINUATION'] = True

            # Get the number of moves in each opening line
            self[each_key]['NUMMOVES'] = len(self[each_key]['PARSER'])

        # Find the incorrect openings and label them as Error
        self['1.c4 c5 2.Nc3 Nf6 3.Nf3 Nf6']['ERROR'] = True
        self['1.d4 c5 2.d5 Nf6 3.Nf3 e4']['ERROR'] = True
        self['1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.e5 Bh7 9.Bd3 Bxd3 10.Qxd3']['ERROR'] = True
        self['1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Nxd4 10.Bxe4']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nd2 Nc6 4.Ngf3 Nf6 5.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nd2 Nc6 4.e4 Nfd7 5.Bd3 c5 6.c3 b6']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Bd7 5.Nf3 Bc6']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Bc5 3.Na4']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Nc6 3.Bc4 Be7 4.d4 exd4 5.c3 Nf6 6.e4 Ne4']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Nc6 3.Bb5 Nc8']['ERROR'] = True
        self['1.d4 d5 2.c4 dxc4 3.Nc3 c5 4.d5 Nf6 5.Nc3 e6 6.e4 exd5 7.e5']['ERROR'] = True
        self['1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 d5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Nf6 5.Nc3 g6']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nf3 Bb4+ 4.Bd2 Bxd2+ 5.Qxd2 b6 6.g3 Bb7 7.Bg2 O-O 8.Nc3 Ne4 9.Qc2 Nxc3 10.Bg5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 exd5 6.Nf3 Qf5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 exd5 6.Nf3 Qf5 7.Qd1 e5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.Nge2']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Bg5 c5 7.d5 c6']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Na6']['ERROR'] = True

        # Add favourite lines here 
        self['1.e4 e5 2.Nf3 Nc6 3.d4']['FAVOURITE'] = True #Scotch Game
        self['1.d4 e5 2.dxe5 Nc6']['FAVOURITE'] = True #Englund Gambit Current bug - Not being found in dict but it should be
        # self['1.e4 d5 2.Nf3']['FAVOURITE'] = True #Tennison Gambit is not a book opening
        self['1.e4 e5 2.Nf3 Nc6 3.Bb5 f5']['FAVOURITE'] = True #Ruy Lopez; Schliemann Defense
        self['1.e4 e5 2.Nf3 Nc6 3.Bc4']['FAVOURITE'] = True #Italian Game
        self['1.e4 e5 2.Nc3']['FAVOURITE'] = True #Vienna Hamppe Opening
        self['1.d4 d5 2.c4 e6']['FAVOURITE'] = True #Queens Gambit Declined
        self['1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 Bc5']['FAVOURITE'] = True #Traxler
             


    def filter_opening_dict(self, search_category:str, search_item:str, move_number=None) -> dict:
        result = ''
        match search_category.upper():
            case "PGN":
                result = {key: value for key, value in self.items() if key == search_item}
            case "MOVESTART":
                result = {key: value for key, value in self.items() if key.startswith(search_item) and value.get("ERROR") == False}

            case "ECO":
                result = {key: value for key, value in self.items() if value.get("ECO") == search_item.upper() and value.get("ERROR") == False}

            case "VOLUME":
                result = {key: value for key, value in self.items() if value.get("VOLUME") == search_item}
            case "NAME":
                result = {key: value for key, value in self.items() if value.get("NAME") == search_item}
            case "CONTINUATION":
                result = {key: value for key, value in self.items() if value.get("CONTINUATION") == True and key.startswith(search_item)}
            case "ALLCONTINUATIONS":
                result = {key: value for key, value in self.items() if value.get("CONTINUATION") == True}
            case "FAVOURITE":
                result = {key: value for key, value in self.items() if value.get("FAVOURITE") == True}
            case "MOVENUMBER":
                search_item = int(search_item)
                result = {key: value for key, value in self.items() if value.get("NUMMOVES") == search_item and value.get("CONTINUATION") == True}
                return result
            case _:
                raise ValueError("Search category: {0} is not a valid search term".format(search_category))

        # # # Redo but without the error'd openings
        # result = {key: value for key, value in self.items() if value.get("ERROR") == False}

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
  

    def find_move_details_in_opening(self, key:str, turn_num:int, isWhite:bool) -> dict:
        move_tuple = self[key]['PARSER'][turn_num]
        return move_tuple[0 if isWhite else 1]







class OpeningsLite(dict):
    def __init__(self, *arg, **kw):
        super(OpeningsLite, self).__init__(*arg, **kw)
        self.read_from_csv_file()  # Call the method at the end of the __init__ method

    def read_from_csv_file(self):
        csv_filename = r"C:\Users\benja\Documents\Visual Studio Code\chess_pieces\chess_moves.csv"

        # Open CSV and read
        with open(csv_filename) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                key = row['MOVESKEY']
                volume = row['VOLUME']
                eco = row['ECO']
                name = row['NAME']
                # continuationname = row['CONTINUATIONNAME']

        # Transpose CSV Contents into Dictionary
                self[key] = {  
                     'VOLUME': volume
                    ,'ECO': eco
                    ,'NAME': name
                    ,'CONTINUATIONNAME': ''
                    ,'PGN': key
                    # ,'NUMMOVES' : 0
                    ,'CONTINUATION': False
                    # ,'PARSER' : None
                    ,'ERROR' : False
                    ,'FAVOURITE' : False
                }

        # Add the Chess Parser object to the dictionary
        for each_key, each_value in self.items():
            # self[each_key]['PARSER'] = ChessParser(each_key)

            # Identify if each opening is a continuation or not
            if each_value['ECO'] in each_value['NAME']:
                self[each_key]['CONTINUATION'] = True

            # Get the number of moves in each opening line
            # self[each_key]['NUMMOVES'] = len(self[each_key]['PARSER'])

        # Find the incorrect openings and label them as Error
        self['1.c4 c5 2.Nc3 Nf6 3.Nf3 Nf6']['ERROR'] = True
        self['1.d4 c5 2.d5 Nf6 3.Nf3 e4']['ERROR'] = True
        self['1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.e5 Bh7 9.Bd3 Bxd3 10.Qxd3']['ERROR'] = True
        self['1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Nxd4 10.Bxe4']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nd2 Nc6 4.Ngf3 Nf6 5.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nd2 Nc6 4.e4 Nfd7 5.Bd3 c5 6.c3 b6']['ERROR'] = True
        self['1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Bd7 5.Nf3 Bc6']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Bc5 3.Na4']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Nc6 3.Bc4 Be7 4.d4 exd4 5.c3 Nf6 6.e4 Ne4']['ERROR'] = True
        self['1.e4 e5 2.Nf3 Nc6 3.Bb5 Nc8']['ERROR'] = True
        self['1.d4 d5 2.c4 dxc4 3.Nc3 c5 4.d5 Nf6 5.Nc3 e6 6.e4 exd5 7.e5']['ERROR'] = True
        self['1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 d5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Nf6 5.Nc3 g6']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nf3 Bb4+ 4.Bd2 Bxd2+ 5.Qxd2 b6 6.g3 Bb7 7.Bg2 O-O 8.Nc3 Ne4 9.Qc2 Nxc3 10.Bg5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 exd5 6.Nf3 Qf5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 exd5 6.Nf3 Qf5 7.Qd1 e5']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.Nge2']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Bg5 c5 7.d5 c6']['ERROR'] = True
        self['1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Na6']['ERROR'] = True

        # Add favourite lines here 
        self['1.e4 e5 2.Nf3 Nc6 3.d4']['FAVOURITE'] = True #Scotch Game
        self['1.d4 e5 2.dxe5 Nc6']['FAVOURITE'] = True #Englund Gambit Current bug - Not being found in dict but it should be
        # self['1.e4 d5 2.Nf3']['FAVOURITE'] = True #Tennison Gambit is not a book opening
        self['1.e4 e5 2.Nf3 Nc6 3.Bb5 f5']['FAVOURITE'] = True #Ruy Lopez; Schliemann Defense
        self['1.e4 e5 2.Nf3 Nc6 3.Bc4']['FAVOURITE'] = True #Italian Game
        self['1.e4 e5 2.Nc3']['FAVOURITE'] = True #Vienna Hamppe Opening
        self['1.d4 d5 2.c4 e6']['FAVOURITE'] = True #Queens Gambit Declined
             


    def filter_opening_dict(self, search_category:str, search_item:str, move_number=None) -> dict:
        result = ''
        match search_category.upper():
            case "PGN":
                result = {key: value for key, value in self.items() if key == search_item}
            case "MOVESTART":
                result = {key: value for key, value in self.items() if key.startswith(search_item) and value.get("ERROR") == False}

            case "ECO":
                result = {key: value for key, value in self.items() if value.get("ECO") == search_item.upper() and value.get("ERROR") == False}

            case "VOLUME":
                result = {key: value for key, value in self.items() if value.get("VOLUME") == search_item}
            case "NAME":
                result = {key: value for key, value in self.items() if value.get("NAME") == search_item}
            case "CONTINUATION":
                result = {key: value for key, value in self.items() if value.get("CONTINUATION") == True and key.startswith(search_item)}
            case "ALLCONTINUATIONS":
                result = {key: value for key, value in self.items() if value.get("CONTINUATION") == True}
            case "FAVOURITE":
                result = {key: value for key, value in self.items() if value.get("FAVOURITE") == True}
            case "MOVENUMBER":
                search_item = int(search_item)
                result = {key: value for key, value in self.items() if value.get("NUMMOVES") == search_item and value.get("CONTINUATION") == True}
                return result
            case _:
                raise ValueError("Search category: {0} is not a valid search term".format(search_category))

        # # # Redo but without the error'd openings
        # result = {key: value for key, value in self.items() if value.get("ERROR") == False}

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
  

    def find_move_details_in_opening(self, key:str, turn_num:int, isWhite:bool) -> dict:
        move_tuple = self[key]['PARSER'][turn_num]
        return move_tuple[0 if isWhite else 1]
