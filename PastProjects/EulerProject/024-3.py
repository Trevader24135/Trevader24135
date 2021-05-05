import math
number = 1000000
numbers = [0,1,2,3,4,5,6,7,8,9]
result = []
while number != 0:
	i = 0
	while i < len(numbers) and number - math.factorial(len(numbers)-1) > 0:
		number -= math.factorial(len(numbers)-1)
		i += 1
	result.append(numbers[i])
	del numbers[i]
	print(numbers)
	print(result)