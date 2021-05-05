for a in range(1000):
	for b in range(1000):
		for c in range(1000):
			if a + b + c == 1000:
				if a**2 + b**2 == c**2:
					product = a * b * c
					print("%s | %s | %s | %s" % (a,b,c,product))