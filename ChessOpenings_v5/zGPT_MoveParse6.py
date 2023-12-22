class Move:
    def __init__(self, notation):
        self._notation = notation
        self._colour = None
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
        # Your existing logic for parsing the notation and populating the attributes goes here
        # Access the attributes using self._notation, self._colour, self._piece, etc.

        # Example logic for assigning some attributes based on notation
        if self._notation == 'O-O':
            self._castling = 'Kingside'
        elif self._notation == 'O-O-O':
            self._castling = 'Queenside'

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
