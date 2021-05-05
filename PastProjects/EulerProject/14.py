starter = 0
steps = 0
for x in range(13,1000000):
	i = 0
	n = x
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = (3 * n) + 1
		i += 1
	i += 1
	if i > steps:
		print("starter: %s | steps: %s" %(x,i))
		steps = i
		starter = x
print starter