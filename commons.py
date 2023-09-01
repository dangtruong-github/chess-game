WHITE = 1
BLACK = -1
BLANK = 0
INVALID_MOVE = 0
VALID_MOVE = 1
VALID_CAPTURE = 2

def signum(z):
    if z == 0:
        return (int)(0)
    return (int)(z / abs(z))