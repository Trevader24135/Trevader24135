def factors(x):
	factors = []
	for i in range(x-1):
		if (x)%(i+1)==0:
			factors.append(i+1)
	return factors

amicable = set([])
for n in range(10000):
	if n not in amicable:
		sumone = 0
		for i in factors(n):
			sumone += i
		sumtwo = 0
		for i in factors(sumone):
			sumtwo += i
		#print("n: " + str(n) + " | n-factors: " + str(factors(n)) + " | sumone: " + str(sumone) + " | sumtwo: " + str(sumtwo))
		if n == sumtwo:
			print(str(sumone) + " | " + str(sumtwo))
			if sumone != sumtwo:
				amicable.add(sumone)
				amicable.add(sumtwo)
print(amicable)
sum = 0
for i in amicable:
	sum += i
	
print(sum)