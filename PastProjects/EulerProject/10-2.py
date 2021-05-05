primes = [2,3]
i = 6
while i < 2000000:
	if i % 100 == 0:
		print(i)
	
	i -= 1
	Bool = True
	for n in primes:
		if i % n == 0:
			Bool = False
			break
	if Bool == True:
		primes.append(i)
		
	i += 2
	Bool = True
	for n in primes:
		if i % n == 0:
			Bool = False
			break
	if Bool == True:
		primes.append(i)
					  
	i += 5

Sum = 0
for i in primes:
	Sum += i

print(primes)
print(Sum)