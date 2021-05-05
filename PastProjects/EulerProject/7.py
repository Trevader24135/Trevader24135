primes = 0
i = 1

while primes < 10001:
	i += 1
	Bool = True
	n = 2
	while n < i:
		if i%n==0 & n != 1:
			Bool = False
			break
		n += 1
	if Bool == True:
		primes += 1
		prime = i
		if primes%10==0:
			print(str(prime) + " | " + str(primes))
	
print(prime)