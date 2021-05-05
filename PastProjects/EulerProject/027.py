def isPrime(num):
	primes = [2]
	try:
		for k in range(3,int(num/2)):
			for n in primes:
				if k%n==0:
					break
			else:
				if num % k == 0:
					break
		else:
			return True
		return False
	except:
		return "not a number"
	
a = -999
b = -999
finala = 0
finalb = 0
primes = []
endprimes = []
total = 0
for a in range(-1000,1000):
	print(a)
	for b in range(-1000,1000):
		n = 0
		while True:
			if isPrime(n**2 + (a * n) + b) == False or n**2 + (a * n) + b < 0:
				break
			n += 1
			
		if n > total:
			total = n
			finala = a
			finalb = b
			endprimes = primes[:]
			
print("finala: " + str(finala))
print("finalb: " + str(finalb))
print("primes: " + str(total))
print("a * b : " + str(finala * finalb))
print(endprimes)