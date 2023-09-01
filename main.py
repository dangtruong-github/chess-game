from board import Board

b = Board()
b.showBoard()

while(True):
    move = input()
    b.move_code(move)
    b.showBoard()
    print(b.turn)