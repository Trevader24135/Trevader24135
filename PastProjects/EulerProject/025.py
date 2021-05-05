fib = [1,1]
digits = []
while len(digits) < 1000:
	digits = [d for d in str(fib[len(fib)-1])]
	fib.append(fib[len(fib)-1] + fib[len(fib)-2])
print(len(fib)-1)