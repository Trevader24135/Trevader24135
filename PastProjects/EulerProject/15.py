import math
x = 20
y = 20
def C(a,b):
	return math.factorial(a) / ( math.factorial(b) * math.factorial(a - b))
print(C(x+y,y))