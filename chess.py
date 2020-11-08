import math
import time
import copy

class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.value = 0

values = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 10,
    "K": 999
}

icons = {
    "P": ["♟", "♙"],
    "N": ["♞", "♘"],
    "B": ["♝", "♗"],
    "R": ["♜", "♖"],
    "Q": ["♛", "♕"],
    "K": ["♚", "♔"]
}

letters = ("a", "b", "c", "d", "e", "f", "g", "h")
numbers = ("1", "2", "3", "4", "5", "6", "7", "8")
turn = 1

def board_create():
    board = [[-1 for i in range(8)] for i in range(8)]
    color = 0

    for i in range(2):
        board[0][i*7] = Piece(color, "R")
        board[1][i*7] = Piece(color, "N")
        board[2][i*7] = Piece(color, "B")
        board[3][i*7] = Piece(color, "Q")
        board[4][i*7] = Piece(color, "K")
        board[5][i*7] = Piece(color, "B")
        board[6][i*7] = Piece(color, "N")
        board[7][i*7] = Piece(color, "R")

        for j in range(8):
            board[j][1 + i*5] = Piece(color, "P")

        color = 1
    board_eval(board)
    return board

def board_eval(board):
    value = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            tile = board[x][y]
            if tile != -1:
                tile.value = tile_eval(board, x, y, tile)
                value += tile.value
    return value

def board_print(board):
    y = 7
    while y >= 0:
        row = str(y + 1) + " "
        for x in range(len(board)):
            tile = board[x][y]
            if tile != -1: row += icons[tile.type][tile.color] + " "
            else: row += "   "
        y -= 1
        print(row)
    #print(" |_________________________")
    print("  A B C D E F G H ")

def board_eval_move(board, a, b):
    value = 0
    dx = [-1, -1, 1, 1, -1, 1, 0, 0]
    dy = [-1, 1, -1, 1, 0, 0, -1, 1]

    for t in (a, b):
        for i in range(8):
            for j in range(0, 8):
                x = t[0] + dx[i] * j
                y = t[1] + dy[i] * j

                if x < 0 or 7 < x: break
                if y < 0 or 7 < y: break

                tile = board[x][y]

                if tile != -1:
                    tile.value = tile_eval(board, x, y, tile)
                    break

    for x in range(8):
        for y in range(8):
            tile = board[x][y]

            if tile != -1:
                if tile.type == "N":
                    tile.value = tile_eval(board, x, y, tile)

                value += tile.value

    return value

def board_eval_recursive(board, depth, turn):
    depth -= 1
    turn += 1
    value = None

    for x in range(8):
        for y in range(8):
            tile = board[x][y]

            if tile != -1 and tile.color == turn % 2:
                moves = tile_get_moves(board, x, y)

                for move in moves:
                    board_new = copy.deepcopy(board)#[list(x) for x in board]

                    tile_move(board_new, (x, y), move)

                    if depth > 0:
                        _eval = board_eval_recursive(board_new, depth, turn)
                        if _eval == None:
                            _eval = ((x, y), move, board_eval_move(board, (x, y), move))
                    else:
                        _eval = ((x, y), move, board_eval_move(board, (x, y), move))#board_eval(board_new))

                    if _eval == None:
                        continue

                    if value == None or (turn % 2 == 0 and _eval[2] > value[2]) or (turn % 2 == 1 and _eval[2] < value[2]):
                        value = ((x, y), move, _eval[2])

    return value

def tile_eval(board, x, y, tile):
    value = values[tile.type]
    value += (0.08 - 0.04 * (tile.type == "Q") - 0.08 * (tile.type == "K")) * tile_get_moves(board, x, y, count = True)

    if tile.type == "P" or tile.type == "N":
        value -= 0.08 * (math.sqrt((x - 3.5)**2 + (y - 3.5)**2) - 2)

    if tile.type == "R":
        value -= 0.1 * (y != 0 and y != 7)

    return value * (1 - 2 * tile.color)

def tile_move(board, a, b):
    board[b[0]][b[1]] = board[a[0]][a[1]]
    board[a[0]][a[1]] = -1

def tile_get_moves(board, x, y, count = False):
    tile = board[x][y]
    if count: moves = 0
    else: moves = []

    if tile != -1:
        if tile.type == "P":
            y1 = y + 1 - 2 * tile.color

            if y1 < 0 or 8 <= y1:
                return moves

            if board[x][y1] == -1:
                if count: moves += 1
                else: moves.append((x, y1))

                if tile.color == 0 and y == 1 and board[x][3] == -1:
                    if count: moves += 1
                    else: moves.append((x, 3))

                if tile.color == 1 and y == 6 and board[x][4] == -1:
                    if count: moves += 1
                    else: moves.append((x, 4))

            if 0 < x:
                tile_l = board[x - 1][y1]
                if tile_l != -1 and tile_l.color != tile.color:
                    if count: moves += 1
                    else: moves.append((x - 1, y1))
            if x < 7:
                tile_r = board[x + 1][y1]
                if tile_r != -1 and tile_r.color != tile.color:
                    if count: moves += 1
                    else: moves.append((x + 1, y1))
        
        elif tile.type == "N":
            moves = notpawn_get_moves(board, x, y, tile.color, [-1, 1, 2, 2, 1, -1, -2, -2], [-2, -2, -1, 1, 2, 2, 1, -1], 8, 1, count = count)
        elif tile.type == "B":
            moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1], [-1, 1, -1, 1], 4, 7, count = count)
        elif tile.type == "R":
            moves = notpawn_get_moves(board, x, y, tile.color, [-1, 1, 0, 0], [0, 0, -1, 1], 4, 7, count = count)
        elif tile.type == "Q":
            moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 7, count = count)
        elif tile.type == "K":
            moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 1, count = count)

    return moves

def notpawn_get_moves(board, x, y, color, dx, dy, dlen, len, count = False):
    if count: moves = 0
    else: moves = []
    for i in range(dlen):
        for j in range(1, len + 1):
            x1 = x + dx[i] * j
            y1 = y + dy[i] * j

            if x1 < 0 or 8 <= x1: break
            if y1 < 0 or 8 <= y1: break

            tile = board[x1][y1]

            if tile == -1 or tile.color != color:
                if count: moves += 1
                else: moves.append((x1, y1))
            if tile != -1: break
    return moves
