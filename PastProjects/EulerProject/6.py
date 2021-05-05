i = 100
Sum = 0
Dif = 0

for n in range(i):
	n += 1
	Sum += n**2
	Dif += n

Dif *= Dif
print(Dif - Sum)