aas = []
bbs = []
pandigital = []

for a in range(10,1000):
	#print(a)
	for b in range(10,1000):
		number = set()
		for i in list(str(a)):
			number.add(int(i))
		for i in list(str(b)):
			number.add(int(i))
		for i in list(str(a*b)):
			number.add(int(i))
		
		if len(number) != 9 or len((str(a)+str(b)+str(a*b))) != 9 or 0 in number:
			continue
		else:
			pandigital.append(a*b)
			aas.append(a)
			bbs.append(b)
			print(a)
			print(b)
			print(a*b)
			print(number)
			
print(aas)
print(bbs)
print(pandigital)
sum = 0
for i in pandigital:
	sum += i
print(sum)