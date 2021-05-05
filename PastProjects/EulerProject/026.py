import math
limit = 10
longest = 0
length = 0
for d in range(3,4):
	print(d)
	
	string = str(1/d)
	k=[str(i) for i in string]
	del k[0]
	del k[0]
	
	print(k)
	
	repeat = False
	i = 0
	for n in k:
		print(k)
		i = 0
		del k[0]
		for m in k:
			i += 1
			if m == k:
				break
		else:
			
			continue
		break
	print(i)
	if i > length:
		i = length
		longest = d
	
print(longest)
print(length)
