from board import Board

b = Board()
b.showBoard()

while(True):
    move = input()
    b.move(move)
    b.showBoard()
    possibleMoves = b.getAllPossibleMoves()
    if len(possibleMoves) == 0:
        break
    print(b.turn, possibleMoves)