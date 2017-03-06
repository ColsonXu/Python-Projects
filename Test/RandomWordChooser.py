from random import randint
wordList = ["Cat", "Is", "In", "The", "Box"]
chosenwordlist = []


def randomwordchooser(listname):
	chosenword = listname[randint(0, len(listname) - 1)]
	if chosenword in chosenwordlist:
		print("NONE")
	else:
		print(chosenword)
		chosenwordlist.append(chosenword)

for i in range(0, 6):
	randomwordchooser(wordList)
