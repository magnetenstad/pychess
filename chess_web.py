import math
import time
import copy
import sys
from chess import *
from selenium import webdriver

def driver_create():
	if sys.platform == "win32": driver = webdriver.Chrome("lib/chromedriver.exe")
	#if sys.platform == "darwin": driver = webdriver.Chrome("lib/chromedriver")

	driver.get("https://lichess.org/analysis")

	return driver

driver = driver_create()

tile_size = driver.find_element_by_xpath("//piece[@class='white king']").size["width"]

chess = Chess()
chess.print()
print("Current evaluation: ", chess.evaluate_board(), "\n")

while True:
	a = (0, 0)
	b = (0, 0)
	i = [""]
	
	while True:
		try:
			i = []#input("\n" + str((chess.turn - 1) % 2) + " to play:").split()
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
		evaluation = chess.evaluate_recursive_start(2)
		
		if evaluation != None:
			b = driver.find_element_by_class_name("cg-wrap")

			x0 = evaluation[0][0]
			y0 = evaluation[0][1]
			x1 = evaluation[1][0]
			y1 = evaluation[1][1]

			orientation = b.get_attribute("class")

			if "orientation-black" in orientation:
				x0 = 7 - x0
				x1 = 7 - x1
			else:
				y0 = 7 - y0
				y1 = 7 - y1

			action = webdriver.common.action_chains.ActionChains(driver)
			action.move_to_element_with_offset(b, x0 * tile_size + tile_size/2, y0 * tile_size + tile_size/2)
			action.click()
			action.perform()

			action = webdriver.common.action_chains.ActionChains(driver)
			action.move_to_element_with_offset(b, x1 * tile_size + tile_size/2, y1 * tile_size + tile_size/2)
			action.click()
			action.perform()

			chess.move(evaluation[0], evaluation[1])
			print("Computer played:", chess.letters[evaluation[0][0]] + chess.numbers[evaluation[0][1]], chess.letters[evaluation[1][0]] + chess.numbers[evaluation[1][1]])
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

	print("Current evaluation: ", chess.evaluate_board(), "\n")
	chess.print()

