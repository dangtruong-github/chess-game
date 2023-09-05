WHITE = 1
BLACK = -1
BLANK = 0
INVALID_MOVE = 0
VALID_MOVE = 1
VALID_CAPTURE = 2
VALID_EN_PASSANT = 3

PAWN_VALUE = 100
KNIGHT_VALUE = 280
BISHOP_VALUE = 320
ROOK_VALUE = 479
QUEEN_VALUE = 929
KING_VALUE = 60000
BLANK_VALUE = 0

def signum(z):
    if z == 0:
        return (int)(0)
    return (int)(z / abs(z))

chrs = {
    'b_checker': u'\u25FB',
    'b_pawn': u'\u265F',
    'b_rook': u'\u265C',
    'b_knight': u'\u265E',
    'b_bishop': u'\u265D',
    'b_king': u'\u265A',
    'b_queen': u'\u265B',
    'w_checker': u'\u25FC',
    'w_pawn': u'\u2659',
    'w_rook': u'\u2656',
    'w_knight': u'\u2658',
    'w_bishop': u'\u2657',
    'w_king': u'\u2654',
    'w_queen': u'\u2655'
}