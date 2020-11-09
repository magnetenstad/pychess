import math
import time
import copy

class Piece:
	def __init__(self, _color, _type):
		self.color = _color
		self.type = _type
		self.value = 0
		self.move_count = 0
		self.moved = False
	def copy(self):
		piece = Piece(self.color, self.type)
		piece.value = self.value
		piece.move_count = self.move_count
		return piece
	def __str__(self) -> str:
		return self.type + str(self.color)

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
boards = []

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

def board_write(board):
	string = ""
	y = 7
	while y >= 0:
		row = str(y + 1) + " "
		for x in range(len(board)):
			tile = board[x][y]
			if tile != -1: row += icons[tile.type][tile.color] + " "
			else: row += "  "
		y -= 1
		string += row + "\n"
	string += "  A B C D E F G H\n"
	return string

def board_print(board):
	print(board_write(board))

def board_string(board):
	string = ""
	for x in range(8):
		for y in range(8):
			string += str(board[x][y])
	return string

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

def board_eval_recursive(board, boards, depth, turn):
	depth -= 1
	turn = (turn + 1) % 2
	value = None
	

	for x in range(8):
		for y in range(8):
			tile = board[x][y]

			if tile != -1 and tile.color == turn:
				moves = tile_get_moves(board, x, y)
				board[x][y].move_count = len(moves)

				for move in moves:
					tile_new = board[move[0]][move[1]]
					
					boards_new = boards.copy()
					if tile_new != -1:
						tile_new = tile_new.copy()
					
					tile_move(board, (x, y), move)
					
					string = board_string(board)
					
					if not "K" + str(turn) in string or string in boards_new:
						board[x][y] = tile
						board[move[0]][move[1]] = tile_new
						continue
					else:
						boards_new.append(string)
					
					if y == 0 or y == 7 and tile.type == "P":
						tile.type == "Q"
					
					if depth > 0:
						_eval = board_eval_recursive(board, boards_new, depth, turn)
						if _eval == None:
							_eval = ((x, y), move, board_eval_move(board, (x, y), move))
					else:
						_eval = ((x, y), move, board_eval_move(board, (x, y), move))

					board[x][y] = tile
					board[move[0]][move[1]] = tile_new

					if _eval == None:
						continue

					if value == None or (turn == 0 and _eval[2] > value[2]) or (turn == 1 and _eval[2] < value[2]):
						value = ((x, y), move, _eval[2])

	return value

def tile_eval(board, x, y, tile):
	return (values[tile.type] + (0.08 - 0.05 * (tile.type == "Q") + 0.03 * (tile.type == "N")) * tile.move_count ) * (1 - 2 * tile.color)

def tile_move(board, a, b):
	board[a[0]][a[1]].moved = True
	board[b[0]][b[1]] = board[a[0]][a[1]]
	board[a[0]][a[1]] = -1

def tile_get_moves(board, x, y):
	tile = board[x][y]
	moves = []

	if tile != -1:
		if tile.type == "P":
			y1 = y + 1 - 2 * tile.color

			if y1 < 0 or 8 <= y1:
				return moves

			if board[x][y1] == -1:
				moves.append((x, y1))

				if tile.color == 0 and y == 1 and board[x][3] == -1:
					moves.append((x, 3))

				if tile.color == 1 and y == 6 and board[x][4] == -1:
					moves.append((x, 4))

			if 0 < x:
				tile_l = board[x - 1][y1]
				if tile_l != -1 and tile_l.color != tile.color:
					moves.append((x - 1, y1))
			if x < 7:
				tile_r = board[x + 1][y1]
				if tile_r != -1 and tile_r.color != tile.color:
					moves.append((x + 1, y1))
		
		elif tile.type == "N":
			moves = notpawn_get_moves(board, x, y, tile.color, [-1, 1, 2, 2, 1, -1, -2, -2], [-2, -2, -1, 1, 2, 2, 1, -1], 8, 1)
		elif tile.type == "B":
			moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1], [-1, 1, -1, 1], 4, 7)
		elif tile.type == "R":
			moves = notpawn_get_moves(board, x, y, tile.color, [-1, 1, 0, 0], [0, 0, -1, 1], 4, 7)
		elif tile.type == "Q":
			moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 7)
		elif tile.type == "K":
			moves = notpawn_get_moves(board, x, y, tile.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 1)

	return moves

def notpawn_get_moves(board, x, y, color, dx, dy, dlen, _len, count = False):
	moves = []
	for i in range(dlen):
		for j in range(1, _len + 1):
			x1 = x + dx[i] * j
			y1 = y + dy[i] * j

			if x1 < 0 or 8 <= x1: break
			if y1 < 0 or 8 <= y1: break

			tile = board[x1][y1]
			
			if tile == -1 or tile.color != color:
				moves.append((x1, y1))
			if tile != -1: break
			
	return moves
