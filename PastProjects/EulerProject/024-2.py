import math
number = 4
numbers = [0,1,2]
result = []
i = 0
brk = False
while number != 0:
	while number != 0 and brk == False:
		if number - math.factorial(len(numbers)-1) >= 0:
			number -= math.factorial(len(numbers)-1)
			i+=1
		else:
			brk = True
	brk = False
	del numbers[i]
	result.append(i)
	i=0
	print(numbers)
	print(result)
