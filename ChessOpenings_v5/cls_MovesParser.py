class MoveParser:
    def __init__(self, turn_num, notation, colour):
        self._turn_num = turn_num
        self._notation = notation
        self._colour = colour
        self._piece = None
        self._code = None
        self._location = None
        self._destination = None
        self._castling = None
        self._capture = None
        self._checkormate = None
        self._promotion = None
        self._file = None
        self._rank = None

        # Call the method to process the notation and populate the attributes
        self._process_notation()

    def _process_notation(self):
        if self.notation == None:
            return
        
        original_notation = str(self.notation)

        castling_symbols = {'O-O': 'Kingside', 'O-O-O': 'Queenside'}
        check_symbols = ['+', '#']

        self.castling = castling_symbols.get(original_notation)

        if self.castling:
            # Check for check/checkmate symbol and remove it from the notation
            for symbol in check_symbols:
                original_notation = original_notation.strip(symbol)
            return

        if 'x' in original_notation:
            # print("the letter x has been found in {0}".format(original_notation))
            self.capture = True
            original_notation = original_notation.replace('x', '')
            
            # print("The new original_notation is: {0}".format(original_notation))
            # print("the capture is {0}".format(self.capture))
            # input()

        if '=' in original_notation:
            self.promotion = original_notation[-1]
            original_notation = original_notation.replace('=', '')

        # Split the remaining notation into its moving piece (and rook/file originality) from the destination square (last 2 characters)
        original_notation, self.destination = original_notation[:-2], original_notation[-2:]

        if original_notation.islower() and len(original_notation) == 1:
            self.piece = 'p'
            self.file = original_notation
            self.code = self.colour + self.piece
            return

        if len(original_notation) == 1:
            self.piece = original_notation
            self.code = self.colour + self.piece
        elif len(original_notation) == 2:
            if any(char.isdigit() for char in original_notation):
                self.piece, self.rank = original_notation[:-1], original_notation[-1:]
            else:
                self.piece, self.file = original_notation[:-1], original_notation[-1:]
            self.code = self.colour + self.piece
        elif len(original_notation) == 3:
            self.piece, self.file, self.rank = list(original_notation)
            self.code = self.colour + self.piece

        if self.piece is None:
            self.piece = 'p'
            self.code = self.colour + self.piece

    def print_attributes(self):
        attributes = vars(self)  # Get a dictionary of all the object's attributes
        for attr, value in attributes.items():
            print(f"{attr}: {value}")

    def print_attributes_dict(self):
        move_details = {'notation': self.notation, 'colour': self.colour, 'piece': self.piece, 'code': self.code, 
                        'location': self.location, 'destination': self.destination, 'castling': self.castling, 
                        'capture': self.capture, 'checkormate': self.checkormate, 'promotion': self.promotion, 
                        'file': self.file, 'rank': self.rank}
        print(move_details)



    @property
    def turn_number(self):
        return self._turn_number

    @turn_number.setter
    def turn_number(self, value):
        self._turn_number = value

    @property
    def notation(self):
        return self._notation

    @notation.setter
    def notation(self, value):
        self._notation = value

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = value

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, value):
        self._piece = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    @property
    def castling(self):
        return self._castling

    @castling.setter
    def castling(self, value):
        self._castling = value

    @property
    def capture(self):
        return self._capture

    @capture.setter
    def capture(self, value):
        self._capture = value

    @property
    def checkormate(self):
        return self._checkormate

    @checkormate.setter
    def checkormate(self, value):
        self._checkormate = value

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    # Rest of the Move class code
    # ...
