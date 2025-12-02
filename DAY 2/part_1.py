inputFile = open("input.txt")

readInput = inputFile.read()

splittedInput = readInput.split(",")

result = 0

for i in splittedInput:
	separateIds = i.split("-")
	print(separateIds)

		