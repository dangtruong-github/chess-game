from piece import Piece, Rook, Knight, Bishop, Queen, King, Pawn, Blank
import commons

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

    def updateBoolBoard(self):
        for i in range(8):
            for j in range(8):
                self.boolBoard[i][j] = self.board[i][j].value * self.board[i][j].team

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
        return realPiece.isValidMove(fromPos, toPos, self.boolBoard)
        
    def isInCheck(self, state):
        pass

    def isNextInCheck(self, fromPos, toPos):   
        pass

    # special moves
    def isValidCastling(self, side):
        team = 0 if self.turn == commons.WHITE else 7
        
        print("inside func")

        # king and rook hasn't moved
        supposed_king = self.board[4][team]
        if supposed_king.expression.lower() != "k" or supposed_king.hasMoved == True:
            return False
        
        supposed_rook = self.board[side][team]
        if supposed_rook.expression.lower() != "r" or supposed_rook.hasMoved == True:
            return False
        
        print("pass stage 1")

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

        return True
    
    def move_code(self, code):
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

        if self.isValidMove(movingPiece.expression, fromPos, toPos) == commons.INVALID_MOVE:
            print("Invalid move!")
            return False

        movingPiece.move(toPos)
        self.board[fromPos[0]][fromPos[1]] = Blank("a1")
        self.board[fromPos[0]][fromPos[1]].move(fromPos)
        self.board[toPos[0]][toPos[1]] = movingPiece
        self.boolBoard[fromPos[0]][fromPos[1]] = 0
        self.boolBoard[toPos[0]][toPos[1]] = movingPiece.team

        self.turn *= -1

        return True
    
    def showBoard(self):
        print("********")
        for i in range(8):
            for j in range(8):
                print(self.board[j][7 -i].expression, end="")
            print()
        print("********")