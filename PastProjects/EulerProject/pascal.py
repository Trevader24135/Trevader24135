pascal = [[1]]
rows = 15
for i in range(rows):
	i += 1
	pascal.append([1])
	for n in range(len(pascal[i-1]) - 1):
		pascal[i].append(pascal[i-1][n] + pascal[i-1][n+1])
		#pascal[i][n + 1] = pascal[i-1][n] + pascal[i-1][n + 1]
		#pascal[i].append(pascal[i - 1][n - 1] + pascal[i-1][n])
		#n += 0
		#pascal[i] = pascal[i - 1][n]
	pascal[i].append(1)
print(pascal[len(pascal)-1])

Sum = 0
for i in pascal[len(pascal)-1]:
	Sum += i
print(Sum/2)