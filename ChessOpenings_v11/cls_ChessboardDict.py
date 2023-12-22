import inspect
from itertools import product

class ChessboardDict(dict):
   def __init__(self,*arg,**kw):
      super(ChessboardDict, self).__init__(*arg, **kw)

      colour1 = "#769656"
      colour2 = "#eeeed2"


      self['a1'] = {'square':'a1', 'file':'a', 'rank':1, 'gridRow':7, 'gridCol':0, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['b1'] = {'square':'b1', 'file':'b', 'rank':1, 'gridRow':7, 'gridCol':1, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['c1'] = {'square':'c1', 'file':'c', 'rank':1, 'gridRow':7, 'gridCol':2, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['d1'] = {'square':'d1', 'file':'d', 'rank':1, 'gridRow':7, 'gridCol':3, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['e1'] = {'square':'e1', 'file':'e', 'rank':1, 'gridRow':7, 'gridCol':4, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['f1'] = {'square':'f1', 'file':'f', 'rank':1, 'gridRow':7, 'gridCol':5, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['g1'] = {'square':'g1', 'file':'g', 'rank':1, 'gridRow':7, 'gridCol':6, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['h1'] = {'square':'h1', 'file':'h', 'rank':1, 'gridRow':7, 'gridCol':7, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}

      self['a2'] = {'square':'a2', 'file':'a', 'rank':2, 'gridRow':6, 'gridCol':0, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['b2'] = {'square':'b2', 'file':'b', 'rank':2, 'gridRow':6, 'gridCol':1, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['c2'] = {'square':'c2', 'file':'c', 'rank':2, 'gridRow':6, 'gridCol':2, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['d2'] = {'square':'d2', 'file':'d', 'rank':2, 'gridRow':6, 'gridCol':3, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['e2'] = {'square':'e2', 'file':'e', 'rank':2, 'gridRow':6, 'gridCol':4, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['f2'] = {'square':'f2', 'file':'f', 'rank':2, 'gridRow':6, 'gridCol':5, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['g2'] = {'square':'g2', 'file':'g', 'rank':2, 'gridRow':6, 'gridCol':6, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['h2'] = {'square':'h2', 'file':'h', 'rank':2, 'gridRow':6, 'gridCol':7, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}

      self['a3'] = {'square':'a3', 'file':'a', 'rank':3, 'gridRow':5, 'gridCol':0, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['b3'] = {'square':'b3', 'file':'b', 'rank':3, 'gridRow':5, 'gridCol':1, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['c3'] = {'square':'c3', 'file':'c', 'rank':3, 'gridRow':5, 'gridCol':2, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['d3'] = {'square':'d3', 'file':'d', 'rank':3, 'gridRow':5, 'gridCol':3, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['e3'] = {'square':'e3', 'file':'e', 'rank':3, 'gridRow':5, 'gridCol':4, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['f3'] = {'square':'f3', 'file':'f', 'rank':3, 'gridRow':5, 'gridCol':5, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['g3'] = {'square':'g3', 'file':'g', 'rank':3, 'gridRow':5, 'gridCol':6, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['h3'] = {'square':'h3', 'file':'h', 'rank':3, 'gridRow':5, 'gridCol':7, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}

      self['a4'] = {'square':'a4', 'file':'a', 'rank':4, 'gridRow':4, 'gridCol':0, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['b4'] = {'square':'b4', 'file':'b', 'rank':4, 'gridRow':4, 'gridCol':1, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['c4'] = {'square':'c4', 'file':'c', 'rank':4, 'gridRow':4, 'gridCol':2, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['d4'] = {'square':'d4', 'file':'d', 'rank':4, 'gridRow':4, 'gridCol':3, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['e4'] = {'square':'e4', 'file':'e', 'rank':4, 'gridRow':4, 'gridCol':4, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['f4'] = {'square':'f4', 'file':'f', 'rank':4, 'gridRow':4, 'gridCol':5, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['g4'] = {'square':'g4', 'file':'g', 'rank':4, 'gridRow':4, 'gridCol':6, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['h4'] = {'square':'h4', 'file':'h', 'rank':4, 'gridRow':4, 'gridCol':7, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}

      self['a5'] = {'square':'a5', 'file':'a', 'rank':5, 'gridRow':3, 'gridCol':0, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['b5'] = {'square':'b5', 'file':'b', 'rank':5, 'gridRow':3, 'gridCol':1, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['c5'] = {'square':'c5', 'file':'c', 'rank':5, 'gridRow':3, 'gridCol':2, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['d5'] = {'square':'d5', 'file':'d', 'rank':5, 'gridRow':3, 'gridCol':3, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['e5'] = {'square':'e5', 'file':'e', 'rank':5, 'gridRow':3, 'gridCol':4, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['f5'] = {'square':'f5', 'file':'f', 'rank':5, 'gridRow':3, 'gridCol':5, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['g5'] = {'square':'g5', 'file':'g', 'rank':5, 'gridRow':3, 'gridCol':6, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['h5'] = {'square':'h5', 'file':'h', 'rank':5, 'gridRow':3, 'gridCol':7, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}

      self['a6'] = {'square':'a6', 'file':'a', 'rank':6, 'gridRow':2, 'gridCol':0, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['b6'] = {'square':'b6', 'file':'b', 'rank':6, 'gridRow':2, 'gridCol':1, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['c6'] = {'square':'c6', 'file':'c', 'rank':6, 'gridRow':2, 'gridCol':2, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['d6'] = {'square':'d6', 'file':'d', 'rank':6, 'gridRow':2, 'gridCol':3, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['e6'] = {'square':'e6', 'file':'e', 'rank':6, 'gridRow':2, 'gridCol':4, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['f6'] = {'square':'f6', 'file':'f', 'rank':6, 'gridRow':2, 'gridCol':5, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['g6'] = {'square':'g6', 'file':'g', 'rank':6, 'gridRow':2, 'gridCol':6, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['h6'] = {'square':'h6', 'file':'h', 'rank':6, 'gridRow':2, 'gridCol':7, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}

      self['a7'] = {'square':'a7', 'file':'a', 'rank':7, 'gridRow':1, 'gridCol':0, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['b7'] = {'square':'b7', 'file':'b', 'rank':7, 'gridRow':1, 'gridCol':1, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['c7'] = {'square':'c7', 'file':'c', 'rank':7, 'gridRow':1, 'gridCol':2, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['d7'] = {'square':'d7', 'file':'d', 'rank':7, 'gridRow':1, 'gridCol':3, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['e7'] = {'square':'e7', 'file':'e', 'rank':7, 'gridRow':1, 'gridCol':4, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['f7'] = {'square':'f7', 'file':'f', 'rank':7, 'gridRow':1, 'gridCol':5, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['g7'] = {'square':'g7', 'file':'g', 'rank':7, 'gridRow':1, 'gridCol':6, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['h7'] = {'square':'h7', 'file':'h', 'rank':7, 'gridRow':1, 'gridCol':7, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}

      self['a8'] = {'square':'a8', 'file':'a', 'rank':8, 'gridRow':0, 'gridCol':0, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['b8'] = {'square':'b8', 'file':'b', 'rank':8, 'gridRow':0, 'gridCol':1, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['c8'] = {'square':'c8', 'file':'c', 'rank':8, 'gridRow':0, 'gridCol':2, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['d8'] = {'square':'d8', 'file':'d', 'rank':8, 'gridRow':0, 'gridCol':3, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['e8'] = {'square':'e8', 'file':'e', 'rank':8, 'gridRow':0, 'gridCol':4, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['f8'] = {'square':'f8', 'file':'f', 'rank':8, 'gridRow':0, 'gridCol':5, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}
      self['g8'] = {'square':'g8', 'file':'g', 'rank':8, 'gridRow':0, 'gridCol':6, 'colour':colour2, 'squareType':'Light', 'pieceObj':None}
      self['h8'] = {'square':'h8', 'file':'h', 'rank':8, 'gridRow':0, 'gridCol':7, 'colour':colour1, 'squareType':'Dark' , 'pieceObj':None}

      self.reset_starting_pieces()


   def reset_starting_pieces(self):
      # print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
      # print("\t [Variables]: None= \n".format())

      for key, value in self.items():
         value['pieceObj'] = None

      self["a1"]['pieceObj'] = 'wR'  
      self["b1"]['pieceObj'] = 'wN'
      self["c1"]['pieceObj'] = 'wB'
      self["d1"]['pieceObj'] = 'wQ'
      self["e1"]['pieceObj'] = 'wK'
      self["f1"]['pieceObj'] = 'wB'
      self["g1"]['pieceObj'] = 'wN'
      self["h1"]['pieceObj'] = 'wR'

      self["a2"]['pieceObj'] = 'wp'
      self["b2"]['pieceObj'] = 'wp'
      self["c2"]['pieceObj'] = 'wp'
      self["d2"]['pieceObj'] = 'wp'
      self["e2"]['pieceObj'] = 'wp'
      self["f2"]['pieceObj'] = 'wp'
      self["g2"]['pieceObj'] = 'wp'
      self["h2"]['pieceObj'] = 'wp'        

      self["a7"]['pieceObj'] = 'bp'  
      self["b7"]['pieceObj'] = 'bp'  
      self["c7"]['pieceObj'] = 'bp'  
      self["d7"]['pieceObj'] = 'bp'  
      self["e7"]['pieceObj'] = 'bp'  
      self["f7"]['pieceObj'] = 'bp'  
      self["g7"]['pieceObj'] = 'bp'  
      self["h7"]['pieceObj'] = 'bp'  

      self["a8"]['pieceObj'] = 'bR'
      self["b8"]['pieceObj'] = 'bN'
      self["c8"]['pieceObj'] = 'bB'
      self["d8"]['pieceObj'] = 'bQ'
      self["e8"]['pieceObj'] = 'bK' 
      self["f8"]['pieceObj'] = 'bB'
      self["g8"]['pieceObj'] = 'bN'
      self["h8"]['pieceObj'] = 'bR'
  


   def move_piece_standard(self, piece_code:str, starting_square:str, ending_square:str):
      # print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
      # print("\t [Variables]: piece_code={0}, starting_square={1}, ending_square={2} \n".format(piece_code, starting_square, ending_square))


      if piece_code != self[starting_square]["pieceObj"]:
         raise ValueError("You attempted to move a {0} on {1}, but there is a {2} on that square".
                          format(piece_code, self[starting_square]["square"], self[starting_square]["pieceObj"]))
      else:
         self[starting_square]["pieceObj"] = None
         self[ending_square]["pieceObj"] = piece_code


   def move_piece_castling(self, colour:str, side:str):
      # print("\n[Current Function]: {0}".format(inspect.stack()[0][3]))
      # print("\t [Variables]: colour={0}, side={1} \n".format(colour, side))

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
         self[position]["pieceObj"] = piece



   def get_dictionary_to_list(self) -> list:
      # Create an empty 2D array for the chessboard
      chessboard = [['' for _ in range(8)] for _ in range(8)]

      # Iterate over the dictionary and populate the chessboard
      for key, value in self.items():
         file, rank = value['gridRow'], value['gridCol']
         if value['pieceObj'] is not None:
               chessboard[file][rank] = value['pieceObj']
         elif value['pieceObj'] is None:
               chessboard[file][rank] = None

      # Combine all the lists within chessboard into a single list
      combined_list = [item for sublist in chessboard for item in sublist]

      return combined_list



   def get_dictionary_as_lists(self):
      # Create an empty 2D array for the chessboard
      chessboard = [['' for _ in range(8)] for _ in range(8)]

      # Iterate over the dictionary and populate the chessboard
      for key, value in self.items():
         file, rank = value['gridRow'], value['gridCol']
         if value['pieceObj'] != None:
            chessboard[file][rank] = value['pieceObj']
         elif value['pieceObj'] == None:
            chessboard[file][rank] = "--"

      return chessboard
       
       
   def get_filter_list_by_piececode(self, piece_code:str) -> list:
      """Returns a list of dictionary entries where pieceObj matches the requested code"""
      # print("[Current Function]: {0}".format(inspect.stack()[0][3]))
      # print("\t [Variables]: piece_code= {0} \n".format(piece_code))
      return list(filter(lambda x: x['pieceObj'] == piece_code, self.values()))    

