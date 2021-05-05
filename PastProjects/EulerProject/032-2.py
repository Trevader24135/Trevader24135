pandigital = set()
for a in range(1,10000):
	print(a)
	for b in range(a,10000):
		string = str(a)+str(b)+str(a*b)
		if len(set(string)) == 9 and len(list(string)) == 9 and '0' not in set(string):
			pandigital.add(a*b)
			print("a: " + str(a))
			print("b: " + str(b))
			print("ab: " + str(a*b))
sum = 0
for i in pandigital:
	sum += i
print(sum)