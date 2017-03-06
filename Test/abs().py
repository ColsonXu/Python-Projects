# This program is used to calculate the absolute value of a given number.

import time

num = input('Please enter a number: ')

if num >= 0:
	print(num)
else:
	print(0 - num)

time.sleep(5)