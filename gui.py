# importing everything from tkinter
from tkinter import *
from commons import *

class GUIBoard:
    def __init__(self, board):
        self.observer = board
        self.currentPossibleMoves = []
        self.currentActive = [-1, -1]
        # creating the tkinter self.window
        self.window = Tk()

        self.input_move = Entry(self.window)

        self.turn = WHITE

        # function define for
        # updating the self.tk_board
        # widget content

        # create a button widget and attached
        # with makeMove function
        self.move_button = Button(self.window, text = "Move", command = self.makeMove)

        # create a Label widget
        self.tk_board = []
        for i in range(8):
            self.tk_board.append([])
            for j in range(8):  
                button = Button(self.window, text = self.observer.board[i][j].unicode, font=("Arial", 20), state='normal', bg = 'grey', command = lambda: self.getPossibleMoves([1, 3]))
                self.tk_board[-1].append(button)

        # place the widgets
        # in the gui self.window
        for i in range(8):
            for j in range(8):
                self.tk_board[i][j].grid(row=7-j, column=i)

        self.input_move.grid(row=0, column=8, columnspan=2)
        self.move_button.grid(row=1, column=8, columnspan=2)

        # Start the GUI
        self.window.mainloop()

    def getPossibleMoves(self, pos):
        if self.currentActive[0] > -1 and self.currentActive[1] > -1:
            self.tk_board[pos[0]][pos[1]].configure(state = 'normal')
            for move in self.currentPossibleMoves:
                move_pos = [-1, -1]
                if len(move) == 3: # 0-0
                    move_pos = [pos[0] + 2, pos[1]]
                elif len(move) == 5: # 0-0-0
                    move_pos = [pos[0] - 2, pos[1]]
                else:
                    move_pos = [ord(move[4]) - ord('a'), ord(move[4]) - ord('1')]
                self.tk_board[move_pos[0]][move_pos[1]].configure(state = 'active', bg = 'yellow', command = lambda: self.getPossibleMoves(move_pos[0], move_pos[1])) 

        self.currentPossibleMoves.clear()

        if pos[0] == self.currentActive[0] and pos[1] == self.currentActive[1]:
            self.currentActive = [-1, -1]
        else:
            self.currentActive = pos
            self.currentPossibleMoves = self.observer.getPossibleMovesOfPiece(pos)

            print(self.currentPossibleMoves)
            print(self.currentActive)
            
            self.tk_board[pos[0]][pos[1]].configure(state = 'active')
            for move in self.currentPossibleMoves:
                move_pos = [-1, -1]
                if len(move) == 3: # 0-0
                    move_pos = [pos[0] + 2, pos[1]]
                elif len(move) == 5: # 0-0-0
                    move_pos = [pos[0] - 2, pos[1]]
                else:
                    move_pos = [ord(move[4]) - ord('a'), ord(move[5]) - ord('1')]
                self.tk_board[move_pos[0]][move_pos[1]].configure(state = 'active', bg = 'yellow', command = lambda: self.makeMove(move)) 

    def makeMove(self, move):

        # configure
        self.observer.move(move)
        self.changeBoard()
        self.input_move.delete(0, 'end')
        possibleMoves = self.observer.getAllPossibleMoves()
        if len(possibleMoves) == 0:
            self.move_button["state"] = "disabled"
            self.input_move.grid_remove()
        else:
            for move in possibleMoves:
                print(move, end=" ")
            print()

    def changeBoard(self):
        for i in range(8):
            for j in range(8):
                self.tk_board[i][j].config(text = self.observer.board[i][j].unicode)