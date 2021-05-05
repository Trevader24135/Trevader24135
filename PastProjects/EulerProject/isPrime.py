def isPrime(number):
	if number % 2 == 0:
		return False
	primes = [2]
	for i in range(3, int(number**(1/2))):
		for n in primes:
			if i % n == 0:
				break
		else:
			primes.append(i)
			if number % i == 0:
				return False
		break
	return True

def oldPrimeList(number): #unnecessarily tests ALL primes below i
	primes = [2]
	for i in range(3,int(number)):
		for n in primes:
			if i % n == 0:
				break
		else:
			primes.append(i)
		continue
	#print(primes)
	return primes

def primeList(number): #eratosthenes sieve
	primes = [2] #inital prime list
	nums = 0 #used for finding total numbers checked for primality
	for i in range(3,int(number)): #checks all numbers below number (the ceiling given to the function)
		n = 0 #used for iterating through list of primes
		nums += 1 #one more number checked for primality
		while primes[n] <= i**(1/2): #it's only necessary for trial division to check primes below the square root of the candidate
			if i % primes[n] == 0: #if there's a remainder of zero, it was evenly divided and is not prime
				break #the break stops the while from continuing to "else"
			n += 1 #iterate to next prime to check
		else: #if the while was never broken, i is prime
			primes.append(i) #add i to the list of primes
	print("List nums crunched: " + str(nums)) #just for testing, show numbers checked for primality
	return primes

def fermatPrimeList(number): #warning! not accurate!
	primes = [2,3]
	a = 3
	for n in range(5,number):
		if (a**(n-1)) % n==1:
			primes.append(n)
	return primes
	
def fermatComboPrimeList(number): #warning! slow at large numbers!
	primes = [2,3]
	a = 3
	for i in range(3, number):
		print(i)
		if (a**(i-1)) % i != 1:
			continue
		n = 0
		while primes[n] <= i**(1/2):
			if i % primes[n] == 0:
				break
			n += 1
		else:
			primes.append(i)
		continue
	return primes

def oldWheelPrimeList(number):
	def primeList(number): #preferred method!
		primes = [2]
		for i in range(3,int(number)):
			#print(i)
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
	def isPrime(number):
		if number % 2 == 0:
			return False
		primes = [2]
		for i in range(3, int(number**(1/2))):
			for n in primes:
				if i % n == 0:
					break
			else:
				primes.append(i)
				if number % i == 0:
					return False
			break
		return True
	
	seedPrimes = [2,3,5]
	wheelPrimes = seedPrimes
	primes = []
	
	product = 1
	for i in seedPrimes:
		product *= i
	
	innerWheelPrimes = primeList(product)
	primes = innerWheelPrimes[:]
	innerWheelPrimes.insert(0,1)
	for i in seedPrimes:
		innerWheelPrimes.remove(i)
	
	#print("product: " + str(product))
	#i = product + 1
	#while i < number:
	#print("number / product: " + str(int(number / product) + (number % product > 0)))
	for i in range(1,int(number / product) + (number % product > 0)):
		#print("i: " + str(i))
		for n in innerWheelPrimes:
			if (n + (product * i)) > number:
				break
			#print(" n: " + str(n))
			for k in primes:
				#print("  k: " + str(k))
				#print("   n+(p*i): " + str(n+(product * i)))
				if ((n + (product * i)) % k) == 0:
					break
			else:
				#print("                 ADDED: " + str(n + (product * i)))
				primes.append(n + (product * i))
	
	return primes

def gwheelPrimeList(number):
	innerWheel = [1,7,11,13,17,19,23,29]
	primes = [2,3,5,7,11,13,17,19,23,29]
	nums = 0
	while primes[-1] < number:
		innerWheel = [int(30 + i) for i in innerWheel]
		for i in innerWheel:
			n = 0
			nums += 1
			while primes[n] <= i**(1/2):
				
				#print("num: " + str(nums) + " | number: " + str(i))
				#print("n: " + str(n))
				if i % primes[n] == 0:
					break
				n += 1
			else:
				primes.append(i)
				#print(primes)
				if i > number:
					break
	del primes[-1]
	print("wheel nums crunched: " + str(nums))
	return primes

def wheelPrimeList(number):
	if number < 29: #pick the largest wheel possible, to a point
		wheelBase = [2,3] #wheel of 6
		product = 6
	elif number < 209:
		wheelBase = [2,3,5] #wheel of 30, like wiki page
		product = 30
	elif number < 2309:
		wheelBase = [2,3,5,7] #wheel of 210
		product = 210
	else:
		wheelBase = [2,3,5,7,11] #wheel of 2310
		product = 2310
		
	innerWheel = [i for i in range(1,product + 1)] #generate the first circle
	for i in wheelBase: #remove all multiples of the initial primes from the wheel
		k = 1 #used to iterate multiples
		while i * k <= product: #remove all multples within the list
			#print(i * k)
			try: #some multples are hit by multiple primes, so try is used to ignore "not found" errors
				innerWheel.remove(i * k) #remove current multiple from list
			except: #except not needed
				pass #ignore
			k += 1 #iterate k
	
	primes = primeList(product) #find all primes within the first circle, this is the only circle with exceptions from the prime list
	nums = 0 #used for finding total numbers checked for primality
	while primes[-1] < number: #continue for as long as it's below the ceiling
		innerWheel = [int(product + i) for i in innerWheel] #generate the next circle in the factor wheel
		for i in innerWheel: #iterate through prime candidates
			n = 0 #used for iterating through list of primes
			nums += 1 #one more number checked for primality
			while primes[n] <= i**(1/2): #it's only necessary for trial division to check primes below the square root of the candidate
				if i % primes[n] == 0: #if there's a remainder of zero, it was evenly divided and is not prime
					break #the break stops the while from continuing to "else"
				n += 1 #iterate to next prime to check
			else: #if the while was never broken, i is prime
				primes.append(i) #add i to the list of primes
				if i > number: #if the last prime added is above the ceiling
					break #cancel the rest of the for loop
	del primes[-1] #remove the last added prime, it is larger than the ceiling
	print("wheel nums crunched: " + str(nums)) #just for testing, show numbers checked for primality
	return primes
	
def oldSieveList(n):
	nums, primes = [i for i in range(3,n)], [2]
	for i in primes:
		if len(nums) == 0:
			break
		k = 2
		print("removing: " + str(i * k))
		while i * k < n:
			print(k)
			try:
				nums.remove(i*k)
			except:
				pass
			k += 1
		primes.append(nums[0])
		del nums[0]
	return len(primes)

def sieveList(n):
	i, p, ps, m = 0, 3, [2], n // 2
	sieve = [True] * m
	while p <= n:
		if sieve[i]:
			ps.append(p)
			for j in range(int((p*p-3)/2), m, p):
				sieve[j] = False
		i, p = i+1, p+2
	#print(sieve)
	return ps

import time
start_time = time.time()
#print(len(primeList(1000000)))
#print("primeList time: " + str(time.time() - start_time))
#print(len(wheelPrimeList(1000000)))
#print("wheelPrime time: " + str(time.time() - start_time))
#print(stolen(1000000))
print(isPrime(32416190071))
end_time = time.time()
# print(ps)
print(end_time-start_time)