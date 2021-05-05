def isPrime(number):
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	primes = [2]
	for i in range(3,int(number/2)):
		for n in primes:
			if i % n == 0:
				break
		else:
			primes.append(i)
			if number % i == 0:
				return False
		continue
	#print(primes)
	return True

def primeList(number):
	primes = [2]
	for i in range(3,int(number)):
		print(i)
		n = 0
		while primes[n] <= i**(1/2):
			if i % primes[n] == 0:
				break
			n += 1
		else:
			primes.append(i)
		continue
	#print(primes)
	return primes

digits = ['1','3','7','9']
Primes = primeList(1000000)
circularPrimes = []

#print(Primes)
for i in Primes:
	print(i)
	num = list(str(i))
	#print(num)
	if len(num) == 1:
		circularPrimes.append(i)
		continue
	
	for n in range(1,len(num)):
		num.append(num[0])
		del num[0]
		if not Primes.count(int(''.join(num))) >= 1:
			break
	else:
		circularPrimes.append(i)
	#print(str(i) + " | " + str(isPrime(i)))
	
	
print(circularPrimes)
print(len(circularPrimes))