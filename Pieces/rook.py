import commons
from Pieces import Piece

class Rook(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 479, "R")
        
    def isValidPath(self, fromPos, toPos, state, lastMove):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if moving[0] != 0 and moving[1] != 0:
            return commons.INVALID_MOVE
        
        # check if any piece blocked
        for i in range(max(abs(moving[0]), abs(moving[1])) - 1, 0, -1):
            if state[fromPos[0] + commons.signum(moving[0]) * i][fromPos[1] + commons.signum(moving[1]) * i] != 0:
                return commons.INVALID_MOVE

        return commons.VALID_MOVE