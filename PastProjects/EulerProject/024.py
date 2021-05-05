import math
numbers = [0,1,2]
combos = math.factorial(len(numbers))
print(combos)
permutations = []
for i in range(combos):
	permutations.append(int(str(numbers[len(numbers)-3])+str(numbers[len(numbers)-2])+str(numbers[len(numbers)-1])))
print(permutations)