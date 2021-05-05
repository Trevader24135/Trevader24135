fracs = []
for a in range(10,100):
	if a%10==0:
		continue
	for b in range(a,100):
		if b%10==0:
			continue
		if a % b == 0:
			continue
		c = list(str(a))
		d = list(str(b))
			
		poss = False
		if c[1] == 0 or d[1] == 0:
			continue
		if c[0] == d[0]:
			del c[0]
			del d[0]
			poss = True
		elif c[0] == d[1]:
			del c[0]
			del d[1]
			poss = True
		elif c[1] == d[0]:
			del c[1]
			del d[0]
			poss = True
		elif c[1] == d[1]:
			del c[1]
			del d[1]
			poss = True
			
		if poss == True and int(c[0]) / int(d[0]) == a / b:
			print("a: " + str(a) + " | b: " + str(b))
			print("c: " + str(c) + " | d: " + str(d))
			fracs.append(a/b)
print(fracs)
prod = fracs[0]
for i in fracs[1:]:
	prod *= i
print(float((str(prod)[:-1])))