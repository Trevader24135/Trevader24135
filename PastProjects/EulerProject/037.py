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

primes = sieveList(1000000)

trunc = []
for i in primes:
	if i < 20:
		continue
	prime = list(str(i))
	temp = prime[:]
	for n in range(0,len(temp)-1):
		del temp[0]
		if not int(''.join(temp)) in primes:
			break
	else:
		temp = prime[:]
		for n in range(0,len(temp)-1):
			del temp[-1]
			if not int(''.join(temp)) in primes:
				break
		else:
			trunc.append(i)
print(trunc)