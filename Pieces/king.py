from commons import *
from Pieces import Piece
    
class King(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, "K")

    def isValidPath(self, fromPos, toPos, state, lastMove):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if max(abs(moving[0]), abs(moving[1])) != 1:
            return INVALID_MOVE
               
        return VALID_MOVE