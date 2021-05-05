def letnum(letter):
	if letter == "A":
		return 1
	if letter == "B":
		return 2
	if letter == "C":
		return 3
	if letter == "D":
		return 4
	if letter == "E":
		return 5
	if letter == "F":
		return 6
	if letter == "G":
		return 7
	if letter == "H":
		return 8
	if letter == "I":
		return 9
	if letter == "J":
		return 10
	if letter == "K":
		return 11
	if letter == "L":
		return 12
	if letter == "M":
		return 13
	if letter == "N":
		return 14
	if letter == "O":
		return 15
	if letter == "P":
		return 16
	if letter == "Q":
		return 17
	if letter == "R":
		return 18
	if letter == "S":
		return 19
	if letter == "T":
		return 20
	if letter == "U":
		return 21
	if letter == "V":
		return 22
	if letter == "W":
		return 23
	if letter == "X":
		return 24
	if letter == "Y":
		return 25
	if letter == "Z":
		return 26
	return 0
	
file = open("022.txt", "r").read()
names = list(set(file.split("\"")))
names.sort()
scores = []
n = 0
names.pop(0)
names.pop(0)
#for x in names[0]:
#		print(x)

print(names)
for x in names[0]:
	print(x)
for i in names:
	sum = 0
	for x in names[n]:
		sum += letnum(x)
	sum *= (n+1)
	scores.append(sum)
	n += 1

print(scores)

sum = 0
for i in scores:
	sum += i
print(sum)