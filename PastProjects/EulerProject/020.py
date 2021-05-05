
def factorial(x):
	mult = 1
	for i in range(x):
		mult *= i+1
	return mult

print(factorial(100))
#list = str(factorial(10)).split()
#list = [int(d) for d in str(factorial(100))]

sum = 0
for i in str(factorial(100)):
	sum += int(i)
	
print(sum)