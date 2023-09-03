import commons
from Pieces import Piece
    
class Blank(Piece):
    def __init__(self, code):
        super().__init__(code, commons.BLANK, 0, "-")