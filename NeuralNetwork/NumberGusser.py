# The program will use random output to guess the five number given
# in the input list.
# This is a simple implication of Neural Network.

raw = input("Please enter a list with 5 items: ")
raw_list = raw.split()
raw_list = [int(i) for i in raw_list]


def guessing(numbers):
	process = []
	num_guesses = 0
	i_0 = 50
	increase = 0
	decrease = 0
	while True:
		num_guesses += 1
		process.append(i_0)

# Level 2 from decreasing, then increase.
		if decrease > 1 and increase == 1:
			i_0 -= 5
			process.append(i_0)
			if i_0 == numbers[0]:
				print(process)
				print('I have guessed for ' + str(num_guesses) + ' times.')
				break
			elif i_0 < numbers[0]:
				for i_0 in range(i_0, i_0 + 5):
					num_guesses += 1
					process.append(i_0)
					if i_0 == numbers[0]:
						print(process)
						print('I have guessed for ' + str(num_guesses) + ' times.')
						break

# Level 2 from decreasing, then decrease.
		if decrease > 1 and increase == 1:
			i_0 += 5
			process.append(i_0)
			if i_0 == numbers[0]:
				print(process)
				print('I have guessed for ' + str(num_guesses) + ' times.')
				break
			elif i_0 > numbers[0]:
				for i_0 in range(i_0, i_0 - 5):
					num_guesses += 1
					process.append(i_0)
					if i_0 == numbers[0]:
						print(process)
						print('I have guessed for ' + str(num_guesses) + ' times.')
						break

# Level 2 from increasing, then increase.

		if decrease == 1 and increase > 1:
			i_0 -= 5
			process.append(i_0)
			if i_0 == numbers[0]:
				print(process)
				print('I have guessed for ' + str(num_guesses) + ' times.')
				break
			elif i_0 < numbers[0]:
				for i_0 in range(i_0, i_0 + 5):
					num_guesses += 1
					process.append(i_0)
					if i_0 == numbers[0]:
						print(process)
						print('I have guessed for ' + str(num_guesses) + ' times.')
						break

# Level 2 from increasing, then decrease.
		if decrease == 1 and increase > 1:
			i_0 -= 5
			process.append(i_0)
			if i_0 == numbers[0]:
				print(process)
				print('I have guessed for ' + str(num_guesses) + ' times.')
				break
			elif i_0 > numbers[0]:
				for i_0 in range(i_0, i_0 - 5):
					num_guesses += 1
					process.append(i_0)
					if i_0 == numbers[0]:
						print(process)
						print('I have guessed for ' + str(num_guesses) + ' times.')
						break

# Level 1 guessing.
		if i_0 == numbers[0]:
			print(process)
			print('I have guessed for ' + str(num_guesses) + ' times.')
			break
		elif i_0 < numbers[0]:
			increase += 1
			i_0 += 10
		else:
			decrease += 1
			i_0 -= 10

	print(process)


guessing(raw_list)
