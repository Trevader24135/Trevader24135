grid = []
lengths = (1001-1)/2
total = 1
for i in range(3,1002,2):
	for n in range(0,4):
		total += i**2 - (n * (i - 1))
print(total)