from chess import *

chess = Chess()

print("\n")
chess.print()
print("Current evaluation: ", chess.evaluate_board(), "\n")

while True:
	a = (0, 0)
	b = (0, 0)
	i = [""]

	while True:
		try:
			i = input("\n" + ("white", "black")[(chess.turn - 1) % 2] + " to move:").split()
			if len(i) == 0:
				break
			if i[0] == "-":
				chess.turn -= 1
			if i[0] == "exit":
				break
			a = (chess.letters.index(i[0][0]), chess.numbers.index(i[0][1]))
			if len(i) == 1:
				print(chess.board[a[0]][a[1]].value)
			b = (chess.letters.index(i[1][0]), chess.numbers.index(i[1][1]))
			break
		except:
			pass
	
	if len(i) == 0:
		t = time.time()
		print("thinking..")
		evaluation = chess.evaluate_recursive_start(2)
		if evaluation != None:
			chess.move(evaluation[0], evaluation[1])
			print("Computer played:", chess.letters[evaluation[0][0]] +
				  chess.numbers[evaluation[0][1]], chess.letters[evaluation[1][0]] + chess.numbers[evaluation[1][1]])
			print("Eval: ", evaluation[2])
			chess.turn += 1
		else:
			print("No legal moves.")
		print("Time:", time.time() - t)
	else:
		if i[0] == "exit":
			break
		moves = chess.get_moves(a[0], a[1])
		if not b in moves:
			print("Not a legal move.")
		chess.move(a, b)
		chess.turn += 1
	print("Current evaluation: ", round(chess.evaluate_board(), 4), "\n")
	chess.print()
