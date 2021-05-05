primes = []
for i in range (2000000 - 1):
	i += 2
	if i % 100 == 0:
		print(i)
	Bool = True
	for n in range(i-2):
		n += 2
		if i % n == 0:
			Bool = False
			break
	if Bool == True:
		primes.append(i)

Sum = 0
for i in primes:
	Sum += i

print(Sum)