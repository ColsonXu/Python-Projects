list1 = []
while True:
	numIn = int(input("? "))
	if numIn == 0:
		break
	list1.append(numIn)
list1.sort()
print("Min: " + str(list1[0]))
print("Max: " + str(list1[len(list1) - 1]))
