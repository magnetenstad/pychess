import math
import time
import copy

piece_values = {
	"P": 1,
	"N": 3,
	"B": 3,
	"R": 5,
	"Q": 10,
	"K": 999
}

boards = {}
POSITIONS_CHECKED = 0

class Piece:
	def __init__(self, _color, _type):
		self.color = _color
		self.type = _type
		self.value_default = piece_values[self.type]
		self.value = self.value_default
		self.reach = 0
		self.moved = False
		self.reach_factor = 0.08 - 0.06 * (self.type == "Q") + 0.05 * (self.type == "N")

	def copy(self):
		piece = Piece(self.color, self.type)
		piece.value = self.value
		piece.reach = self.reach
		return piece
		
	def __str__(self) -> str:
		return self.type + str(self.color)

	def evaluate(self):
		self.value = (self.value_default + self.reach_factor * self.reach) * (1 - 2 * self.color)
		return self.value

class Chess:
	def __init__(self):
		self.icons = {
			"P": ["♟", "♙"],
			"N": ["♞", "♘"],
			"B": ["♝", "♗"],
			"R": ["♜", "♖"],
			"Q": ["♛", "♕"],
			"K": ["♚", "♔"]
		}

		self.letters = ("a", "b", "c", "d", "e", "f", "g", "h")
		self.numbers = ("1", "2", "3", "4", "5", "6", "7", "8")
		self.turn = 1
		self.board = self.create()
		self.evaluate_board()

	def create(self):
		board = [[-1 for _ in range(8)] for _ in range(8)]
		
		for i in range(2):
			board[0][i*7] = Piece(i, "R")
			board[1][i*7] = Piece(i, "N")
			board[2][i*7] = Piece(i, "B")
			board[3][i*7] = Piece(i, "Q")
			board[4][i*7] = Piece(i, "K")
			board[5][i*7] = Piece(i, "B")
			board[6][i*7] = Piece(i, "N")
			board[7][i*7] = Piece(i, "R")

			for j in range(8):
				board[j][1 + i*5] = Piece(i, "P")

		return board

	def evaluate_board(self):
		value = 0
		for x in range(8):
			for y in range(8):
				piece = self.board[x][y]
				if piece != -1:
					value += self.evaluate_piece(piece, x, y)
		return value

	def evaluate_piece(self, piece, x, y):
		moves = self.get_moves(x, y)
		piece.reach = len(moves)
		return piece.evaluate()

	def print(self):
		string = ""
		y = 7
		while y >= 0:
			row = str(y + 1) + " "
			for x in range(len(self.board)):
				piece = self.board[x][y]
				if piece != -1: row += self.icons[piece.type][piece.color] + " "
				else: row += "  "
			y -= 1
			string += row + "\n"
		string += "  A B C D E F G H\n"
		print(string)

	def string(self):
		string = ""
		for x in range(8):
			for y in range(8):
				string += str(self.board[x][y])
		return string

	def evaluate_recursive(self, depth, turn):
		global POSITIONS_CHECKED

		depth -= 1
		turn = (turn + 1) % 2
		value = None

		string = str(turn) + self.string() + str(depth)
		
		if string in boards:
			value = boards[string]
		else:
			for x in range(8):
				for y in range(8):
					piece = self.board[x][y]
					
					if piece != -1 and piece.color == turn:
						moves = self.get_moves(x, y)

						for move in moves:
							
							tile_new = self.board[move[0]][move[1]]
							if tile_new != -1:
								tile_new = tile_new.copy()

							self.move((x, y), move)

							if (not "K" + str(turn) in self.string()):
								self.board[x][y] = piece
								self.board[move[0]][move[1]] = tile_new
								continue
				
							if y == 0 or y == 7 and piece.type == "P":
								piece.type == "Q"
							
							if depth > 0:
								evaluation = self.evaluate_recursive(depth, turn)
								if evaluation == None:
									evaluation = ((x, y), move, self.evaluate_board())
							else:
								evaluation = ((x, y), move, self.evaluate_board())
								POSITIONS_CHECKED += 1
							
							self.board[x][y] = piece
							self.board[move[0]][move[1]] = tile_new

							if evaluation == None:
								continue
							
							if value == None or (turn == 0 and evaluation[2] > value[2]) or (turn == 1 and evaluation[2] < value[2]):
								if value != None: print("turn:", turn, "depth:", depth, " | ", round(evaluation[2], 3), "beats", round(value[2], 3), ", piece:", piece.type, piece.color)
								value = ((x, y), move, evaluation[2])
								# if depth == 0:
								# 	self.print()
								# 	print("EVALUATION: ", evaluation[2])
						
			boards[string] = value
		return value

	def evaluate_recursive_start(self, depth):
		global POSITIONS_CHECKED
		POSITIONS_CHECKED = 0
		value = self.evaluate_recursive(depth, self.turn)
		boards.clear()
		print("POSITIONS CHECKED:", POSITIONS_CHECKED)
		return value
	
	def move(self, a, b):
		self.board[a[0]][a[1]].moved = True
		self.board[b[0]][b[1]] = self.board[a[0]][a[1]]
		self.board[a[0]][a[1]] = -1

	def get_moves(self, x, y):
		piece = self.board[x][y]
		moves = []

		if piece != -1:
			if piece.type == "P":
				y1 = y + 1 - 2 * piece.color

				if y1 < 0 or 8 <= y1:
					return moves

				if self.board[x][y1] == -1:
					moves.append((x, y1))

					if piece.color == 0 and y == 1 and self.board[x][3] == -1:
						moves.append((x, 3))

					if piece.color == 1 and y == 6 and self.board[x][4] == -1:
						moves.append((x, 4))

				if 0 < x:
					tile_l = self.board[x - 1][y1]
					if tile_l != -1 and tile_l.color != piece.color:
						moves.append((x - 1, y1))
				if x < 7:
					tile_r = self.board[x + 1][y1]
					if tile_r != -1 and tile_r.color != piece.color:
						moves.append((x + 1, y1))
			
			elif piece.type == "N":
				moves = self.notpawn_get_moves(x, y, piece.color, [-1, 1, 2, 2, 1, -1, -2, -2], [-2, -2, -1, 1, 2, 2, 1, -1], 8, 1)
			elif piece.type == "B":
				moves = self.notpawn_get_moves(x, y, piece.color, [-1, -1, 1, 1], [-1, 1, -1, 1], 4, 7)
			elif piece.type == "R":
				moves = self.notpawn_get_moves(x, y, piece.color, [-1, 1, 0, 0], [0, 0, -1, 1], 4, 7)
			elif piece.type == "Q":
				moves = self.notpawn_get_moves(x, y, piece.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 7)
			elif piece.type == "K":
				moves = self.notpawn_get_moves(x, y, piece.color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 1)

		return moves

	def notpawn_get_moves(self, x, y, color, dx, dy, dlen, _len):
		moves = []
		for i in range(dlen):
			for j in range(1, _len + 1):
				x1 = x + dx[i] * j
				y1 = y + dy[i] * j

				if x1 < 0 or 8 <= x1: break
				if y1 < 0 or 8 <= y1: break

				piece = self.board[x1][y1]
				
				if piece == -1 or piece.color != color:
					moves.append((x1, y1))
				if piece != -1: break
				
		return moves
		