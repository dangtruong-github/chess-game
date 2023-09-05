from Pieces import Piece, Rook, Knight, Bishop, Queen, King, Pawn, Blank
import commons
import copy

standard_board = [[Rook("a1", commons.WHITE), Pawn("a2", commons.WHITE), Blank("a3"), Blank("a4"), Blank("a5"), Blank("a6"), Pawn("a7", commons.BLACK), Rook("a8", commons.BLACK)],
                  [Knight("b1", commons.WHITE), Pawn("b2", commons.WHITE), Blank("b3"), Blank("b4"), Blank("b5"), Blank("b6"), Pawn("b7", commons.BLACK), Knight("b8", commons.BLACK)],
                  [Bishop("c1", commons.WHITE), Pawn("c2", commons.WHITE), Blank("c3"), Blank("c4"), Blank("c5"), Blank("c6"), Pawn("c7", commons.BLACK), Bishop("c8", commons.BLACK)],
                  [Queen("d1", commons.WHITE), Pawn("d2", commons.WHITE), Blank("d3"), Blank("d4"), Blank("d5"), Blank("d6"), Pawn("d7", commons.BLACK), Queen("d8", commons.BLACK)],
                  [King("e1", commons.WHITE), Pawn("e2", commons.WHITE), Blank("e3"), Blank("e4"), Blank("e5"), Blank("e6"), Pawn("e7", commons.BLACK), King("e8", commons.BLACK)],
                  [Bishop("f1", commons.WHITE), Pawn("f2", commons.WHITE), Blank("f3"), Blank("f4"), Blank("f5"), Blank("f6"), Pawn("f7", commons.BLACK), Bishop("f8", commons.BLACK)],
                  [Knight("g1", commons.WHITE), Pawn("g2", commons.WHITE), Blank("g3"), Blank("g4"), Blank("g5"), Blank("g6"), Pawn("g7", commons.BLACK), Knight("g8", commons.BLACK)],
                  [Rook("h1", commons.WHITE), Pawn("h2", commons.WHITE), Blank("h3"), Blank("h4"), Blank("h5"), Blank("h6"), Pawn("h7", commons.BLACK), Rook("h8", commons.BLACK)]]

initialized_boolBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

class Board:
    def __init__(self):
        self.board = standard_board
        self.boolBoard = initialized_boolBoard
        self.updateBoolBoard()
        self.turn = commons.WHITE
        self.moveHistory = ""

    def updateBoolBoard(self):
        for i in range(8):
            for j in range(8):
                self.boolBoard[i][j] = self.board[i][j].value

    def getAllPossibleMoves(self):
        possibleMoves = []
        for i in range(8):
            for j in range(8):
                if self.boolBoard[i][j] * self.turn > 0:
                    moves = self.board[i][j].getPossibleMoves(self.boolBoard)
                    for move in moves:
                        checked = self.isNextInCheck([i, j], move)
                        #print(self.board[i][j].expression + chr(i + ord('a')) + chr(j + ord('1')) + "-" + chr(move[0] + ord('a')) + chr(move[1] + ord('1')), checked)
                        if self.turn == commons.WHITE:
                            if checked % 2 == 1:
                                continue
                        else:
                            if checked >= 2:
                                continue
                        
                        possibleMoves.append(self.board[i][j].expression + chr(i + ord('a')) + chr(j + ord('1')) + "-" + chr(move[0] + ord('a')) + chr(move[1] + ord('1')))
        
        if len(possibleMoves) == 0:
            if self.isInCheck(self.boolBoard, self.turn) == True:
                print(self.turn * (-1), "win")
            else:
                print("Draw")
        
        return possibleMoves
    
    def getLastMove(self):
        if len(self.moveHistory) <= 0:
            return False

        for i in range(len(self.moveHistory) - 2, -1, -1):
            if self.moveHistory[i] == ' ':
                return self.moveHistory[i+1:-1]
        
        return self.moveHistory

    def isValidMove(self, piece, fromPos, toPos):
        # check if piece actually appears in 'fromPos'
        realPiece = self.board[fromPos[0]][fromPos[1]]
        if realPiece.expression.lower() != piece.lower():
            return commons.INVALID_MOVE
        
        if realPiece.team != self.turn:
            return commons.INVALID_MOVE

        if realPiece.expression == "-":
            return commons.INVALID_MOVE
        
        # check if it is actually a valid move
        valid = realPiece.isValidMove(fromPos, toPos, self.boolBoard, self.getLastMove())
        if valid == commons.INVALID_MOVE:    
            return commons.INVALID_MOVE

        checked = self.isNextInCheck(fromPos, toPos)

        #print(checked)

        if self.turn == commons.WHITE:
            if checked % 2 == 1:
                return commons.INVALID_MOVE
        else:
            if checked >= 2:
                return commons.INVALID_MOVE
        return valid
        
    def isInCheck(self, state, team):
        king_pos = [0, 0]
        for i in range(8):
            for j in range(8):
                if state[i][j] == King("a1", team).value:
                    king_pos = [i, j]
                    break
        
        #print(team, king_pos)

        # horizontal/vertical -- rook + queen
        horizverti = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        for index, i in enumerate(horizverti):
            for j in range(1, 8):
                pos = [king_pos[0] + i[0] * j, king_pos[1] + i[1] * j]
                if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                    break

                if state[pos[0]][pos[1]] * team > 0:
                    break

                if state[pos[0]][pos[1]] == Queen("a1", team * (-1)).value or state[pos[0]][pos[1]] == Rook("a1", team * (-1)).value:
                    return True
        
        #print("pass horizontal")

        # diagonal -- bishop + queen 
        diagonals = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        for index, i in enumerate(diagonals):
            for j in range(1, 8):
                pos = [king_pos[0] + i[0] * j, king_pos[1] + i[1] * j]
                if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                    break

                #print(chr(pos[0] + ord('a')) + chr(pos[1] + ord('1')))

                if state[pos[0]][pos[1]] * team > 0:
                    break

                if state[pos[0]][pos[1]] == Queen("a1", team * (-1)).value or state[pos[0]][pos[1]] == Bishop("a1", team * (-1)).value:
                    return True
        
        #print("pass diagonal")
            
        # knight
        knight_move = [[-1, -2], [1, 2], [2, 1], [-2, -1], [1, -2], [-1, 2], [2, -1], [-2, 1]]
        for index, i in enumerate(knight_move):
            pos = [king_pos[0] + i[0], king_pos[1] + i[1]]
            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                if state[pos[0]][pos[1]] == Knight("a1", team * (-1)).value:
                    return True
                
        #print("pass knight")
                
        # pawn
        pawn_move = [[-1, team], [1, team]]
        for index, i in enumerate(pawn_move):
            pos = [king_pos[0] + i[0], king_pos[1] + i[1]]
            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                if state[pos[0]][pos[1]] == Pawn("a1", team * (-1)).value:
                    return False

        #print("pass pawn")

        # king
        king_move = [[-1, -1], [1, 1], [1, -1], [-1, 1], [1, 0], [-1, 0], [0, -1], [0, 1]]
        for index, i in enumerate(king_move):
            pos = [king_pos[0] + i[0], king_pos[1] + i[1]]
            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                if state[pos[0]][pos[1]] == King("a1", team * (-1)).value:
                    return True
                
        #print("pass king")
        
        return False
    
    def isNextInCheck(self, fromPos, toPos): 
        state = copy.deepcopy(self.boolBoard)
        state[toPos[0]][toPos[1]] = state[fromPos[0]][fromPos[1]]
        state[fromPos[0]][fromPos[1]] = 0
        return self.isInCheck(state, commons.WHITE) + 2 * self.isInCheck(state, commons.BLACK)

    # special moves
    def isValidCastling(self, side):
        team = 0 if self.turn == commons.WHITE else 7

        # king and rook hasn't moved
        supposed_king = self.board[4][team]
        if supposed_king.expression.lower() != "k" or supposed_king.hasMoved == True:
            return False
        
        supposed_rook = self.board[side][team]
        if supposed_rook.expression.lower() != "r" or supposed_rook.hasMoved == True:
            return False

        # no blocked
        if side == 0:
            for i in range(1, 4):
                if self.boolBoard[i][team] != 0:
                    return False
        else:
            for i in range(5, 7):
                if self.boolBoard[i][team] != 0:
                    return False

        # check if they are in check
        state = copy.deepcopy(self.boolBoard)
        if self.isInCheck(state, self.turn) == True:
            return False
        
        state[5 if side == 7 else 3][team] = supposed_king.value
        state[4][team] = 0
        if self.isInCheck(state, self.turn) == True:
            return False
        
        state[6 if side == 7 else 2][team] = supposed_king.value
        state[5 if side == 7 else 3][team] = 0
        if self.isInCheck(state, self.turn) == True:
            return False
        
        # moving mechanism
        supposed_king.move([6 if side == 7 else 2, team])
        self.board[4][team] = Blank('a1')
        self.board[4][team].move([4, team])
        self.board[6 if side == 7 else 2][team] = supposed_king
        self.boolBoard[4][team] = 0
        self.boolBoard[6 if side == 7 else 2][team] = supposed_king.team

        supposed_rook.move([5 if side == 7 else 3, team])
        self.board[side][team] = Blank('a1')
        self.board[side][team].move([side, team])
        self.board[5 if side == 7 else 3][team] = supposed_rook
        self.boolBoard[side][team] = 0
        self.boolBoard[5 if side == 7 else 3][team] = supposed_rook.team

        self.turn *= -1
        self.moveHistory += "0-0 " if side == 7 else "0-0-0 "

        return True
    
    def move(self, code):
        # castling
        if code == "0-0" or code == "0-0-0":
            return self.isValidCastling(7 if len(code) == 3 else 0)
        
        if len(code) < 5 or len(code) > 6:
            return False
        if len(code) == 5:
            code = "P" + code
        print(code)
        piece = code[0]
        fromPos = [ord(code[1]) - ord('a'), ord(code[2]) - ord('1')]
        toPos = [ord(code[4]) - ord('a'), ord(code[5]) - ord('1')]
        movingPiece = self.board[fromPos[0]][fromPos[1]]

        if movingPiece.expression.lower() != piece.lower():
            print("Invalid piece!")
            return False

        status = self.isValidMove(movingPiece.expression, fromPos, toPos)

        if status == commons.INVALID_MOVE:
            print("Invalid move!")
            return False
        
        if status == commons.VALID_EN_PASSANT:
            self.board[toPos[0]][fromPos[1]] = Blank("a1")
            self.board[toPos[0]][fromPos[1]].move([toPos[0], fromPos[1]])

        movingPiece.move(toPos)
        self.board[fromPos[0]][fromPos[1]] = Blank("a1")
        self.board[fromPos[0]][fromPos[1]].move(fromPos)
        self.board[toPos[0]][toPos[1]] = movingPiece
        self.boolBoard[fromPos[0]][fromPos[1]] = 0
        self.boolBoard[toPos[0]][toPos[1]] = movingPiece.value

        self.turn *= -1

        self.moveHistory += code
        self.moveHistory += " "

        return True
    
    def showBoard(self):
        print("********")
        for i in range(8):
            for j in range(8):
                print(self.board[j][7 -i].expression, end="")
            print()
        print("********")