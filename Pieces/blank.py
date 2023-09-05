from commons import *
from Pieces import Piece
    
class Blank(Piece):
    def __init__(self, code):
        super().__init__(code, BLANK, 0, " ")