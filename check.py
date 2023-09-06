from board import Board
from Pieces import King
from commons import *

state = [[479, 100, 0, 0, 0, 0, -100, 0], [280, 100, 0, 0, 0, 0, 0, 0], [320, 100, 0, 0, 0, 0, 0, 0], [929, 100, 0, 0, 0, 0, 0, -60000], [60000, 0, 0, 0, -280, 0, -100, 0], [320, 100, 0, 0, -320, 0, -100, -320], [280, 100, 0, 0, 0, 0, -100, -280], [479, 100, 0, 0, 0, 0, -100, -479]]

print(Board().isInCheck(state, BLACK))

print(King("a1", BLACK).range)