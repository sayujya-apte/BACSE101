def zigzagConversion(s, numRows):
	currRow = 0
	direction = 1

	lines = []
	for i in range(0, numRows):
		lines.append([])

	for char in s:
		lines[currRow].append(char)
		if currRow == 0:
			direction = 1
		elif currRow == numRows - 1:
			direction = -1

		currRow += direction

	convertstr = ""
	for j in range(0, numRows):
		convertstr += "".join(lines[j])

	return convertstr

s = input("Enter string : ")
numRows = int(input("Enter the number of rows : "))

print(zigzagConversion(s, numRows))