from commons import *

class Piece:
    def __init__(self, code, team, value, expression):
        self.pos = [ord(code[0]) - ord('a'), ord(code[1]) - ord('1')]
        self.team = team
        self.value = value * team
        self.expression = expression
        if team == BLACK:
            self.expression = self.expression.lower()
        self.hasMoved = False
        self.range = 7 if abs(self.value) > 300 else 1
        self.moves = []
        if abs(self.value) == 479:
            self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        elif abs(self.value) == 320:
            self.moves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        elif abs(self.value) > 900:
            self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        elif abs(self.value) == 280:
            self.moves = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
        elif abs(self.value) == 100:
            self.moves = [[1, 1], [-1, 1], [0, 1], [0, 2]]
            for i in range(len(self.moves)):
                self.moves[i][1] *= self.team

    def isValidMove(self, fromPos, toPos, state, lastMove):
        # check if self is in fromPos position
        if fromPos[0] != self.pos[0] or fromPos[1] != self.pos[1]:
            return INVALID_MOVE
        
        # check the color of the piece on the toPos
        if state[toPos[0]][toPos[1]] == self.team:
            return INVALID_MOVE
        elif state[toPos[0]][toPos[1]] == self.team * (-1):
            return self.isValidPath(fromPos, toPos, state, lastMove) * VALID_CAPTURE
        
        return self.isValidPath(fromPos, toPos, state, lastMove) * VALID_MOVE
    
    def getPossibleMoves(self, state):
        possibleMoves = []
        for index, i in enumerate(self.moves):
            for j in range(1, self.range + 1):
                pos = [self.pos[0] + i[0] * j, self.pos[1] + i[1] * j]

                # out of bounds
                if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                    break
                
                # same team
                if state[pos[0]][pos[1]] * self.team > 0:
                    break

                possibleMoves.append(pos)

        return possibleMoves
    
    def isValidPath(self, fromPos, toPos, state, lastMove):
        pass

    def move(self, newPos):
        self.pos = newPos
        self.hasMoved = True