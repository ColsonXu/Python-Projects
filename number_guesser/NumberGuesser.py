# 
# Number Guesser. Copyright 2017 Colson Xu
# 

import random
import time

num = random.randint(0, 100)
count = 0

print("The range is from 0 to 100.")

while True:
	guess = input("Enter your guess here: ")
	if guess == num:
		count += 1
		print("Congratulations! You have guessed the right number!")
		print("You have guessed " + str(count) + " times.")
		break
	elif guess > num:
		print("lower")
		count += 1
	elif guess < num:
		print("higher")
		count += 1

time.sleep(20)
