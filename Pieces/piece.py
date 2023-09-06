from commons import *

class Piece:
    def __init__(self, code, team, expression):
        self.pos = [ord(code[0]) - ord('a'), ord(code[1]) - ord('1')]
        self.team = team
        self.expression = expression
        self.value = BLANK_VALUE
        if expression[0].lower() == 'p':
            self.value = PAWN_VALUE * team
        elif expression[0].lower() == 'n':
            self.value = KNIGHT_VALUE * team 
        if expression[0].lower() == 'b':
            self.value = BISHOP_VALUE * team
        if expression[0].lower() == 'r':
            self.value = ROOK_VALUE * team
        if expression[0].lower() == 'q':
            self.value = QUEEN_VALUE * team
        if expression[0].lower() == 'k':
            self.value = KING_VALUE * team

        if team == BLACK:
            self.expression = self.expression.lower()
        self.hasMoved = False
        self.range = 7 if abs(self.value) > 300 else 1
        # moves
        self.moves = []
        if abs(self.value) == ROOK_VALUE:
            self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        elif abs(self.value) == BISHOP_VALUE:
            self.moves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        elif abs(self.value) == QUEEN_VALUE or abs(self.value) == KING_VALUE:
            self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        elif abs(self.value) == KNIGHT_VALUE:
            self.moves = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
        elif abs(self.value) == PAWN_VALUE:
            self.moves = [[1, 1], [-1, 1], [0, 1], [0, 2]]
            for i in range(len(self.moves)):
                self.moves[i][1] *= self.team
        # unicode
        tmp_str = "b" if self.team == -1 else "w"
        if abs(self.value) == PAWN_VALUE:
            tmp_str += "_pawn"
        elif abs(self.value) == KNIGHT_VALUE:
            tmp_str += "_knight"
        elif abs(self.value) == BISHOP_VALUE:
            tmp_str += "_bishop"
        elif abs(self.value) == ROOK_VALUE:
            tmp_str += "_rook"
        elif abs(self.value) == QUEEN_VALUE:
            tmp_str += "_queen"
        elif abs(self.value) == KING_VALUE:
            tmp_str += "_king"
        
        self.unicode = chrs[tmp_str] if len(tmp_str) > 2 else " "

    def isValidMove(self, fromPos, toPos, state, lastMove):
        # check if self is in fromPos position
        if fromPos[0] != self.pos[0] or fromPos[1] != self.pos[1]:
            #print("not equal from pos")
            return INVALID_MOVE
        
        # check the color of the piece on the toPos
        if state[toPos[0]][toPos[1]] == self.team:
            #print("to pos same team")
            return INVALID_MOVE
        elif state[toPos[0]][toPos[1]] == self.team * (-1):
            return self.isValidPath(fromPos, toPos, state, lastMove) * VALID_CAPTURE
        
        return self.isValidPath(fromPos, toPos, state, lastMove) * VALID_MOVE
    
    def getPossibleMoves(self, state, lastMove = ""):
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

                # different team
                if state[pos[0]][pos[1]] * self.team < 0:
                    break

        return possibleMoves
    
    def isValidPath(self, fromPos, toPos, state, lastMove):
        pass

    def move(self, newPos):
        self.pos = newPos
        self.hasMoved = True