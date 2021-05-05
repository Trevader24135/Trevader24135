k = 1
digits = []
while True:
	k += 1
	
	total = 0
	for i in list(str(k)):
		total += int(i)**5
	if total == k:
		digits.append(k)
	if k > 200000:
		break
print(digits)
sum = 0
for i in digits:
	sum += i
print(sum)