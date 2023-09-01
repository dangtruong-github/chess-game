import commons

class Piece:
    def __init__(self, code, team, value, expression):
        self.pos = [ord(code[0]) - ord('a'), ord(code[1]) - ord('1')]
        self.team = team
        self.value = value
        self.expression = expression
        if team == commons.BLACK:
            self.expression = self.expression.lower()
        self.hasMoved = False

    def isValidMove(self, fromPos, toPos, state):
        # check if self is in fromPos position
        if fromPos[0] != self.pos[0] or fromPos[1] != self.pos[1]:
            return commons.INVALID_MOVE
        
        # check the color of the piece on the toPos
        if state[toPos[0]][toPos[1]] == self.team:
            return commons.INVALID_MOVE
        elif state[toPos[0]][toPos[1]] == self.team * (-1):
            return self.isValidPath(fromPos, toPos, state) * commons.VALID_CAPTURE
        
        return self.isValidPath(fromPos, toPos, state) * commons.VALID_MOVE
    
    def isValidPath(self, fromPos, toPos, state):
        pass

    def move(self, newPos):
        self.pos = newPos
        self.hasMoved = True

class Rook(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 479, "R")

    def isValidPath(self, fromPos, toPos, state):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if moving[0] != 0 and moving[1] != 0:
            return commons.INVALID_MOVE
        
        # check if any piece blocked
        for i in range(max(abs(moving[0]), abs(moving[1])) - 1, 0, -1):
            if state[fromPos[0] + commons.signum(moving[0]) * i][fromPos[1] + commons.signum(moving[1]) * i] != 0:
                return commons.INVALID_MOVE

        return commons.VALID_MOVE

class Bishop(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 320, "B")

    def isValidPath(self, fromPos, toPos, state):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if abs(moving[0]) != abs(moving[1]):
            return commons.INVALID_MOVE
        
        # check if any piece blocked
        for i in range(abs(moving[0]) - 1, 0, -1):
            if state[fromPos[0] + commons.signum(moving[0]) * i][fromPos[1] + commons.signum(moving[1]) * i] != 0:
                return commons.INVALID_MOVE

        return commons.VALID_MOVE

class Queen(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 929, "Q")

    def isValidPath(self, fromPos, toPos, state):
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


class Knight(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 280, "N")

    def isValidPath(self, fromPos, toPos, state):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if max(abs(moving[0]), abs(moving[1])) != 2 or min(abs(moving[0]), abs(moving[1])) != 1:
            return commons.INVALID_MOVE
        
        return commons.VALID_MOVE

class King(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 60000, "K")

    def isValidPath(self, fromPos, toPos, state):
        moving = [toPos[0] - fromPos[0], toPos[1] - fromPos[1]]

        # check if moving in the right direction
        if max(abs(moving[0]), abs(moving[1])) != 1:
            return commons.INVALID_MOVE
               
        return commons.VALID_MOVE

class Pawn(Piece):
    def __init__(self, code, team):
        super().__init__(code, team, 100, "P")

    def isValidPath(self, fromPos, toPos, state):
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
                
                return commons.INVALID_MOVE

        return commons.INVALID_MOVE
    
class Blank(Piece):
    def __init__(self, code):
        super().__init__(code, commons.BLANK, 0, "-")