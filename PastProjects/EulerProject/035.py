def isPrime(number):
	if number % 2 == 0 or number == 2:
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
		
digits = ['1','3','7','9']
circularPrimes = []
for i in range(2,100):
	if isPrime(i) == False:
		print(i)
		continue
	#print(i)
	num = list(str(i))
	bool = False
	for n in num:
		if not n in digits:
			bool = True
			#print(i)
			break
	if bool:
		break
	for n in range(1,len(num)):
		num.append(num[0])
		del num[0]
		if isPrime(int(''.join(num))) == False:
			break
	else:
		circularPrimes.append(i)
print(circularPrimes)