from cls_ChessDictionary import *
from cls_Openings import *
import inspect

chess_dict = ChessBoardDictionary()



def generate_chessboard(dictionary):
    chessboard = [[' ' for _ in range(8)] for _ in range(8)]
    for key, value in dictionary.items():
        rank = value['gridRow']
        file = value['gridCol']
        chessboard[rank][file] = key

    for rank in range(8):
        for file in range(8):
            square = chessboard[rank][file]
            chessboard[rank][file] = f'{chr(ord("a")+file)}{8-rank}'

    return chessboard

# Example usage
chessboard = generate_chessboard(chess_dict)
for rank in chessboard:
    print(' '.join(rank))
