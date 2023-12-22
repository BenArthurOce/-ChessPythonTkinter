

# WISHLIST / TO DO
# MAKE A METHOD IN "MAINCHESSGAME" CALLED "DEBUG PRINT DICTIONARY"
# MOVE THE PRINT BOARD METHOD FROM DICTIONARY INTO THE MAINGAME

from cls_Openings import Openings
from cls_Openings import OpeningsLite
from cls__MainChessGame import MainChessGame


E96_opening = "1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nbd7 8.Re1 c6 9.Bf1 a5" # fixed, this now works

StahlbergVariationQGD = "1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Nxe5 12.Nxe5 axb5"

PushVariationSicilian = "1.e4 c5 2.d4 cxd4 3.c3 d3"



# E96_opening = "1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5"

# MyOpenings = Openings()
# MyMainChessGame = MainChessGame(MyOpenings, PushVariationSicilian)


# # MyParser = MyMainChessGame.openings_information['PARSER']

# # MyMainChessGame.ChessDictionary.print_dictionary_board_debug()
# MyMainChessGame.print_dictionary_board_debug()
# print(MyParser)

# for key, (move1, move2) in MyParser.items():
#     print(f"Move {key}:")
#     print("White move:")
#     print(move1)
#     print("Black move:")
#     print(move2)
#     print()

# for line in MyParser:
# # for key, value in MyParser:
# #     print(key, value)

# # from cls_ChessParser2 import *

# # MyParser = ChessParser2(E96_opening)

# # print(MyParser)

MyLiteDictionary = OpeningsLite()

test_notation2 = "1.d4 Nf6 2.c4"
E96_opening = "1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5"
filtered_dict = MyLiteDictionary.filter_opening_dict("MOVESTART", E96_opening)
# print(MyLiteDictionary.filter_opening_dict("MOVESTART", E96_opening))


for a in filtered_dict.items():
    print(a)