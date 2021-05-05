decimals = []
#for i in range(1,1000000):
#	dec = list(str(i))
#	bool = True
#	print(dec)
#	for n in range(0,len(dec) // 2):
#		
#		if dec[n] != dec[-(n+1)]:
#			bool = False
#			break
#	else:
#		decimals.append(i)
#	if not bool:
#		continue
dec = [0] * 7

for z in range(0,10):
	num = int(''.join([str(z)]))
	if len(str(num)) == 1:
		decimals.append(num)

for z in range(0,10):
	num = int(''.join([str(z),str(z)]))
	if len(str(num)) == 2:
		decimals.append(num)

for z in range(0,10):
	for x in range(0,10):
		num = int(''.join([str(z),str(x),str(z)]))
		if len(str(num)) == 3:
			decimals.append(num)

for z in range(0,10):
	for x in range(0,10):
		num = int(''.join([str(z),str(x),str(x),str(z)]))
		if len(str(num)) == 4:
			decimals.append(num)

for z in range(0,10):
	for x in range(0,10):
		for c in range(0,10):
			num = int(''.join([str(z),str(x),str(c),str(x),str(z)]))
			if len(str(num)) == 5:
				decimals.append(num)
	
for z in range(0,10):
	for x in range(0,10):
		for c in range(0,10):
			num = int(''.join([str(z),str(x),str(c),str(c),str(x),str(z)]))
			if len(str(num)) == 6:
				decimals.append(num)

for z in range(0,10):
	for x in range(0,10):
		for c in range(0,10):
			for v in range(0,10):
				num = int(''.join([str(z),str(x),str(c),str(v),str(c),str(x),str(z)]))
				if len(str(num)) == 7:
					decimals.append(num)

print(decimals)
sum = 0
for i in decimals:
	if i > 10:
		binary = list(bin(i))
		del binary[0]
		del binary[0]
		bool = True
		for n in range(0,len(binary) // 2):
			if binary[n] != binary[-(n+1)]:
				break
		else:
			print("decimal: " + str(i) + " | binary:" + ''.join(binary))
			sum += i
print(sum)
	