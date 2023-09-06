from commons import *
from Pieces import Piece
    
class Pawn(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, "P")

    def isValidPath(self, fromPos, toPos, state, lastMove):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]
        #print(moving)

        # check if moving in the right direction
        if moving[1] != self.team:
            # move two steps from the starting position
            if self.hasMoved == True:
                return INVALID_MOVE
            
            # white
            if state[fromPos[0]][2] == BLANK and state[fromPos[0]][3] == BLANK and self.team == WHITE: 
                return VALID_MOVE
            
            # black
            if state[fromPos[0]][5] == BLANK and state[fromPos[0]][4] == BLANK and self.team == BLACK: 
                return VALID_MOVE
            
            return INVALID_MOVE
        else:
            #print("self.pos=", self.pos)
            if moving[0] == 0:
                if state[fromPos[0] + moving[0]][fromPos[1] + moving[1]] != BLANK:
                    return INVALID_MOVE
                
                return VALID_MOVE
            
            elif abs(moving[0]) == 1:
                #print("piece in to pos=", state[fromPos[0] + moving[0]][fromPos[1] + moving[1]])
                if state[fromPos[0] + moving[0]][fromPos[1] + moving[1]] * self.team < 0:
                    return VALID_MOVE
                
                # en passant
                # if pawn is in 4th/5th row
                if self.team == WHITE:
                    if self.pos[1] != 4:
                        return INVALID_MOVE
                    
                if self.team == BLACK:
                    if self.pos[1] != 3:
                        return INVALID_MOVE
                # if last move is a 2-squared pawn move
                if len(lastMove) != 6:
                    #print("lastMove=", lastMove)
                    return INVALID_MOVE
                
                if lastMove[0].lower() != "p":
                    return INVALID_MOVE

                if lastMove[1] != lastMove[4] or ord(lastMove[2]) - ord(lastMove[5]) != 2 * self.team:
                    #print("lastMove=!", lastMove)
                    return INVALID_MOVE

                col = ord(lastMove[1]) - ord('a')

                if abs(self.pos[0] - col) != 1:
                    #print("col=", col, "self.col=", self.pos[0])
                    return INVALID_MOVE

                return VALID_EN_PASSANT

        return INVALID_MOVE
    
    def getPossibleMoves(self, state, lastMove):
        possibleMoves = []
        for i in range(2):
            pos = [self.pos[0] + self.moves[i][0], self.pos[1] + self.moves[i][1]]

            # out of bounds
            if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                continue
            
            # piece
            if state[pos[0]][pos[1]] * self.team < 0:
                possibleMoves.append(pos)
                continue
            
            # en passant
            # if pawn is in 4th/5th row
            if self.team == WHITE:
                if self.pos[1] != 4:
                    continue
                
            if self.team == BLACK:
                if self.pos[1] != 3:
                    continue
            # if last move is a 2-squared pawn move
            if len(lastMove) != 6:
                continue
            
            if lastMove[0].lower() != "p":
                continue

            if lastMove[1] != lastMove[4] or ord(lastMove[2]) - ord(lastMove[5]) != 2 * self.team:
                continue

            col = ord(lastMove[1]) - ord('a')

            if self.moves[i][0] != col - self.pos[0]:
                continue

            possibleMoves.append(pos)

        
        for i in range(2, len(self.moves)):
            pos = [self.pos[0] + self.moves[i][0], self.pos[1] + self.moves[i][1]]

            # out of bounds
            if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                continue

            if state[pos[0]][pos[1]] != 0:
                break

            possibleMoves.append(pos)

            if self.hasMoved == True:
                break
            
        return possibleMoves