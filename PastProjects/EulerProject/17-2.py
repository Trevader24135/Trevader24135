import inflect
p = inflect.engine()
L = 0
for i in range(1000):
	i += 1
	L += len(p.number_to_words(i).replace(" ","").replace("-",""))
print(L)