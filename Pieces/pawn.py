import commons
from Pieces import Piece
    
class Pawn(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 100, "P")

    def isValidPath(self, fromPos, toPos, state, lastMove):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if moving[1] != self.team:
            # move two steps from the starting position
            if self.hasMoved == True:
                return commons.INVALID_MOVE
            
            # white
            if state[fromPos[0]][2] == commons.BLANK and state[fromPos[0]][3] == commons.BLANK and self.team == commons.WHITE: 
                return commons.VALID_MOVE
            
            # black
            if state[fromPos[0]][5] == commons.BLANK and state[fromPos[0]][4] == commons.BLANK and self.team == commons.BLACK: 
                return commons.VALID_MOVE
            
            return commons.INVALID_MOVE
        else:
            if moving[0] == 0:
                if state[fromPos[0] + moving[0]][fromPos[1] + moving[1]] != commons.BLANK:
                    return commons.INVALID_MOVE
                
                return commons.VALID_MOVE
            
            elif abs(moving[0]) == 1:
                if state[fromPos[0] + moving[0]][fromPos[1] + moving[1]] == (-1) * self.team:
                    return commons.VALID_MOVE
                
                # en passant
                # if pawn is in 4th/5th row
                if self.team == commons.WHITE:
                    if self.pos[1] != 4:
                        return commons.INVALID_MOVE
                    
                if self.team == commons.BLACK:
                    if self.pos[1] != 3:
                        return commons.INVALID_MOVE
                # if last move is a 2-squared pawn move
                if len(lastMove) != 6:
                    return commons.INVALID_MOVE
                
                if lastMove[0].lower() != "p":
                    return commons.INVALID_MOVE

                if lastMove[1] != lastMove[4] or ord(lastMove[2]) - ord(lastMove[5]) != 2 * self.team:
                    return commons.INVALID_MOVE

                col = ord(lastMove[1]) - ord('a')

                if abs(self.pos[0] - col) != 1:
                    return commons.INVALID_MOVE

                return commons.VALID_EN_PASSANT

        return commons.INVALID_MOVE