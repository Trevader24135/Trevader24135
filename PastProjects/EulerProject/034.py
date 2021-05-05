def factorial(n):
	product = 1
	for i in range(2,n+1):
		product *= i
	return product
	
digitfactorial = []

for n in range(3,1000000):
	num = [int(i) for i in list(str(n))]
	sum = 0
	for i in num:
		sum += factorial(i)
	if sum == n:
		digitfactorial.append(n)
print(digitfactorial)