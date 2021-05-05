import math
from decimal import *
getcontext().prec = 100000

long = 0
leng = 0

for d in range(3,1000):
	print("D: " + str(d))
	string = str(Decimal(1) / Decimal(d))
	dec = [str(i) for i in string]
	if len(dec) < 10:
		continue
	del dec[0]
	del dec[0]
	for i in range(0,5):
		del dec[0]
	del dec[-1]
	
	for i in range(0,10):
		if dec.count(str(i)) == 1:
			dec.remove(str(i))
	#print("dec: " + str(dec))
	
	if dec == []:
		continue
		
	temp = []
	temp.append(dec[0])
	for i in dec[1:]:
		if i == temp[0]:
			for n in range(1,len(temp)):
				if temp[n] == dec[len(temp) + n]:
					continue
				else:
					break
			else:
				break
		temp.append(i)
		#print("temp: " + str(temp))

	if len(temp) > long:
		leng = len(temp)
		long = d
	print("length: " + str(len(temp)))
print("longest number: " + str(long))
print("length of number: " + str(leng))