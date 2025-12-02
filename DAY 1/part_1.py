inputFile = open("input.txt")

result = 0
startingNumber = 50

for row in inputFile:
	getLetter = str(row[:1])
	getNumbers = int(row[1:])

	if getLetter == "R":
		startingNumber += getNumbers

		while startingNumber >= 100:
			startingNumber -= 100

		if startingNumber == 0:
			result += 1

	elif getLetter == "L":
		startingNumber -= getNumbers

		while startingNumber <= -1:
			startingNumber += 100

		if startingNumber == 0:
			result += 1

	else:
		print("Unknown input")
		break

print(f"Result is: {result}")