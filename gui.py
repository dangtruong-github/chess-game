# importing everything from tkinter
from tkinter import *
from commons import *

class GUIBoard:
    def __init__(self, board):
        self.observer = board
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
                label = Label(self.window, text = self.observer.board[i][j].unicode, font=("Arial", 20))
                self.tk_board[-1].append(label)

        # place the widgets
        # in the gui self.window
        for i in range(8):
            for j in range(8):
                self.tk_board[i][j].grid(row=7-j, column=i)

        self.input_move.grid(row=0, column=8, columnspan=2)
        self.move_button.grid(row=1, column=8, columnspan=2)

        # Start the GUI
        self.window.mainloop()

    def makeMove(self):
        
        # configure
        self.observer.move(self.input_move.get())
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