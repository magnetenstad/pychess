from chess import *

board = board_create()
boards = []

print("\n")
board_print(board)

while True:
	a = (0, 0)
	b = (0, 0)
	i = [""]

	while True:
		try:
			i = input("\n" + ("white", "black")[(turn - 1) % 2] + " to play:").split()
			if len(i) == 0:
				break
			if i[0] == "-":
				turn -= 1
			if i[0] == "exit":
				break
			a = (letters.index(i[0][0]), numbers.index(i[0][1]))
			if len(i) == 1:
				print(board[a[0]][a[1]].value)
			b = (letters.index(i[1][0]), numbers.index(i[1][1]))
			break
		except:
			pass
	
	if len(i) == 0:
		t = time.time()
		print("thinking..")
		_eval = board_eval_recursive(board, boards, 4, turn)
		if _eval != None:
			tile_move(board, _eval[0], _eval[1])
			print("Computer played:", letters[_eval[0][0]] +
				  numbers[_eval[0][1]], letters[_eval[1][0]] + numbers[_eval[1][1]])
			print("Eval: ", _eval[2])
			turn += 1
		else:
			print("No legal moves.")
		print("Time:", time.time() - t)
	else:
		if i[0] == "exit":
			break
		moves = tile_get_moves(board, a[0], a[1])
		if not b in moves:
			print("Not a legal move.")
		tile_move(board, a, b)
		turn += 1
	print("Current evaluation: ", board_eval(board), "\n")
	board_print(board)
	boards.append(board_string(board))
	print(board_string(board))
