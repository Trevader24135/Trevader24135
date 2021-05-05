#WORKS BUT INNEFFICIENT
deficient = []
abundant = []
perfect = []

def factors(x):
	factors = []
	
	for i in range(int(x/2)):
		if (x)%(i+1)==0:
			factors.append(i+1)
	return factors
	
for i in range(28123):
	i += 1
	factor = factors(i)
	sum = 0
	for n in factor:
		sum += n
	if sum == i:
		perfect.append(i)
		#print("perfect!")
	elif sum > i:
		abundant.append(i)
		#print("abundant!")
	elif sum < i:
		deficient.append(i)
		#print("deficient!")

print(deficient)
print(perfect)
print(abundant)

sums = set([])

for i in abundant:
	for n in abundant:
		sums.add(i + n)

exclusives = []
for i in range(28123):
	if i not in sums:
		exclusives.append(i)
print(exclusives)

total = 0
for i in exclusives:
	total += i
	
print(total)