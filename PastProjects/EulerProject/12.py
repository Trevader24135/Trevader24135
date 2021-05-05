factors = []
i = 1
Sum = 0
while len(factors) < 500:
	factors = []
	Sum += i
	#for n in range(i):
	#	n += 1
	#	Sum += n
	
	for n in range(int(Sum**0.5) + 1):
		n += 1
		if Sum % n == 0:
			factors.append(n)
			factors.append(Sum / n)
	factors = set(factors)
	factors = list(factors)
	
	print("%s | %s" %(Sum, len(factors)))
	i += 1
print(factors)
print(Sum)