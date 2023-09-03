import commons

class Piece:
    def __init__(self, code, team, value, expression):
        self.pos = [ord(code[0]) - ord('a'), ord(code[1]) - ord('1')]
        self.team = team
        self.value = value * team
        self.expression = expression
        if team == commons.BLACK:
            self.expression = self.expression.lower()
        self.hasMoved = False

    def isValidMove(self, fromPos, toPos, state, lastMove):
        # check if self is in fromPos position
        if fromPos[0] != self.pos[0] or fromPos[1] != self.pos[1]:
            return commons.INVALID_MOVE
        
        # check the color of the piece on the toPos
        if state[toPos[0]][toPos[1]] == self.team:
            return commons.INVALID_MOVE
        elif state[toPos[0]][toPos[1]] == self.team * (-1):
            return self.isValidPath(fromPos, toPos, state, lastMove) * commons.VALID_CAPTURE
        
        return self.isValidPath(fromPos, toPos, state, lastMove) * commons.VALID_MOVE
    
    def isValidPath(self, fromPos, toPos, state, lastMove):
        pass

    def move(self, newPos):
        self.pos = newPos
        self.hasMoved = True