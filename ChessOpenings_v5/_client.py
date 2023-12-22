from cls_ChessGame import *
from cls_Openings import *
from valid_moves import *
import inspect
from cls_NotationParser import *
from cls_MovesParser import *
from cls_ChessGame2 import *

ChessOpenings = Openings()
ChessOpenings.populate_dictionary()


ChessGame1 = ChessGame()
ChessGame2 = ChessGame()
ChessGame3 = ChessGame()
ChessGame4 = ChessGame()
ChessGame5 = ChessGame()
AllChessGames = [ChessGame1, ChessGame2, ChessGame3, ChessGame4, ChessGame5]


e4e5_opening = "1.e4 e5"
pirc_defense = "1.e4 d6 2.d4 Nf6"
testing_knight = "1.e4 d6 2.d4 Nf6 3.Nf3"
scotch_game = "1.e4 e5 2.Nf3 Nc6 3.d4"
sample_notation = "1.e4 e5 2.c3 f5"
B07_Opening = "1.e4 d6"
C39_Opening = "1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4"
D55_Opening = "1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3"  # (11) TODO: There was no bN that was able to move to d5
D27_Opening = "1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6" # Testing White Kingside Castling
Nimzo_Indian = "1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3 c5 5.dxc5 Nc6 6.Nf3 Ne4 7.Bd2 Nxd2 8.Nxd2 O-O 9.O-O-O" # (9) Testing Black Kingside Castle, White Queenside Castle

#ERROR (COMPLETED). Nimzo_Indian Correct version has a pawn on c5 and c4.
# The incorrect version we are producing has a pawn on c5 and d4. Its because of "5.dxc5" The d4 pawn needs to take, but since the code scans c4 first, it moves that
# c4 is getting scanned and approved before d4 can be scanned

#ERROR D55_Opening at (11) has an error #TypeError: 'NoneType' object is not subscriptable
#Error is at Nd5 - 9: ('Bxc4', 'Nd5') BECAUSE there is no code for 6: ('Nf3', 'Nbd7')
# {1: ('d4', 'd5'), 2: ('c4', 'e6'), 3: ('Nc3', 'Nf6'), 4: ('Bg5', 'Be7'), 5: ('e3', 'O-O'), 6: ('Nf3', 'Nbd7'), 7: ('Rc1', 'c6'), 
#  8: ('Bd3', 'dxc4'), 9: ('Bxc4', 'Nd5'), 10: ('Bxe7', 'Qxe7'), 11: ('O-O', 'Nxc3'), 12: ('Rxc3', 'e5'), 13: ('dxe5', None)}
#  1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O Nxc3 12.Rxc3 e5 13.dxe5
# [Current Function]: move_piece2
#          [Variables]:
#         each_move_dict={'notation': 'Nbd7', 'colour': 'b', 'piece': 'N', 'code': 'bN', 'location': 'f6', 'destination': 'd7', 
#                         'castling': None, 'capture': None, 'checkormate': None, 'promotion': None, 'file': None, 'rank': 'b'}

# Obtain a series of openings from the openings database
filtered_openings = ChessOpenings.filter_opening_dict("MOVESTART", D55_Opening , 11) # This is a good testing line as it gives us 5 games with 8 moves or over
# print(len(filtered_openings))
# input(filtered_openings)
# go through each of the filted openings, and apply their information to each ChessGame().
# the ChessGame() will then go through the notation
for i, (opening_notation, opening_details) in enumerate(filtered_openings.items()):
    AllChessGames[i].notationString = opening_notation
    AllChessGames[i].notationDict = opening_details['MOVES']





# currently experimenting with the 4th move of this opening.
moves_to_process1 = dict(ChessOpenings['1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.Qg4']['MOVES'])

# testing castle
moves_to_process2 = dict(ChessOpenings['1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 Nf6 6.O-O O-O 7.b3']['MOVES'])

moves_to_process3 = dict(ChessOpenings['1.e4 e5 2.Qh5']['MOVES'])

moves_to_process4 = dict(ChessOpenings['1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7']['MOVES'])

moves_to_process5 = dict(ChessOpenings['1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Bd6']['MOVES'])


# moves = AllChessGames[0].notationDict.items()

# moves_to_execute = [] # Holds all the moves and their information. And then will be executed in the same part of code
# for turn_number, move_tuple in AllChessGames[0].notationDict.items():
#     # if turn_number == 6:
#     #     input("6")
#     if move_tuple[0] is not None:
#         moves_to_execute.append(ChessGame1.process_notation(move_tuple[0], "w"))     # add white move to list
#     if move_tuple[1] is not None:
#         moves_to_execute.append(ChessGame1.process_notation(move_tuple[1], "b"))     # add black move to list

# # print(moves_to_execute)
# # input()
# ChessGame1.process_all_moves(moves_to_execute)


# AllChessGames[0].reset_board()

#convert to dictionary to prepare board print
ChessGame1.ChessboardDictionary.print_dictionary_board_debug()



# parser = NotationParser(ChessGame1.notationString)
# print(parser)

# print(ChessGame1.notationDict)

# MoveNotation = MoveParser("Nxf6", "w")
# # print(MoveNotation.destination)
# MoveNotation.print_attributes()

MyNotation = NotationParser("1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3")
# MyNotation = NotationParser("1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7")

ChessGameNew2 = CHESSGAMECLASSTESTING2(MyNotation._notation_string)  # Instantiate an object of the ChessGame2 class

# you have create the correct Parsers and they both operate in ChessGame2. They both work.
# you how have a list of classes, that has details of every move. But they are all missing the starting piece location.
# you will need to make a class to seperate the move logic


ChessGameNew2._ChessboardDictionary.print_dictionary_board_debug()





