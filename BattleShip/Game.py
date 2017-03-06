from random import randint
from time import sleep

# Creating and initializing the playing board.
ocean = []

for x in range(5):
	ocean.append(["O"] * 5)


def print_board(board):
	for row in board:
		print(" ".join(row))

# The game starts here.
print("Let's play Battleship!")
print_board(ocean)


# Place the ship on board.
def random_row(board):
	return randint(0, len(board) - 1)


def random_col(board):
	return randint(0, len(board[0]) - 1)

# Display the ocean.
ship_row = random_row(ocean)
ship_col = random_col(ocean)
# Debug code:
# print ship_row
# print ship_col

# User input and determination.
for turn in range(10):
	print("Turn", turn + 1)
	guess_row = int(input("Guess Row:"))
	guess_col = int(input("Guess Col:"))

# guess_* -1 because len(*) starts with 0 instead of 1
	if guess_row == ship_row and guess_col == ship_col:
		print("Congratulations! You sunk my battleship!")
		break
	else:
		if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
			print("Oops, that's not even in the ocean.")
			if turn == 9:
				print("Game Over")
				break
		elif ocean[guess_row - 1][guess_col - 1] == "X":
			print("You guessed that one already.")
			if turn == 9:
				print("Game Over")
				break
		else:
			print("You missed my battleship!")
			if turn == 9:
				print("Game Over")
				break
			ocean[guess_row - 1][guess_col - 1] = "X"
			print(print_board(ocean))

sleep(20)
