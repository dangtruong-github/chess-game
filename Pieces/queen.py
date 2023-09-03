import commons
from Pieces import Piece

class Queen(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 929, "Q")

    def isValidPath(self, fromPos, toPos, state, lastMove):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if abs(moving[0]) != abs(moving[1]) and moving[0] != 0 and moving[1] != 0:
            return commons.INVALID_MOVE
        
        # check if any piece blocked
        if abs(moving[0]) == abs(moving[1]):
            for i in range(abs(moving[0]) - 1, 0, -1):
                if state[fromPos[0] + commons.signum(moving[0]) * i][fromPos[1] + commons.signum(moving[1]) * i] != 0:
                    return commons.INVALID_MOVE

            return commons.VALID_MOVE
        else:
            for i in range(max(abs(moving[0]), abs(moving[1])) - 1, 0, -1):
                if state[fromPos[0] + commons.signum(moving[0]) * i][fromPos[1] + commons.signum(moving[1]) * i] != 0:
                    return commons.INVALID_MOVE

            return commons.VALID_MOVE