import re


class NotationParser:
    def __init__(self, notation_string):
        self._notation_string = notation_string
        self._notation_dict = {}

        self.parse()

    @property
    def notation_string(self):
        return self._notation_string

    @notation_string.setter
    def notation_string(self, new_notation_string):
        self._notation_string = new_notation_string
        self.parse()

    @property
    def notation_dict(self):
        return self._notation_dict

    def parse(self):
        regx_pattern = r"\s*(\d{1,3})\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)(?:\s*\d+\.?\d+?m?s)?\.?\s*((?:(?:O-O(?:-O)?)|(?:[KQNBR][1-8a-h]?x?[a-h]x?[1-8])|(?:[a-h]x?[a-h]?[1-8]\=?[QRNB]?))\+?)?(?:\s*\d+\.?\d+?m?s)?"
        matches = re.findall(regx_pattern, self._notation_string)

        for match in matches:
            move_number = int(match[0])
            white_move = match[1].strip()
            black_move = match[2].strip() if match[2] else None

            if move_number in self._notation_dict:
                raise ValueError(f"Duplicated move number: {move_number}")

            self._notation_dict[move_number] = (white_move, black_move)

    def __str__(self):
        return str(self._notation_dict)


