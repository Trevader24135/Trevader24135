year = 1901
day = -1
mon = 1
hits = 0
while year < 2001:
	day += 7
	if (day > 31) and (mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12):
		day -= 31
		mon += 1
	elif (day > 30) and (mon == 4 or mon == 6 or mon == 9 or mon == 11):
		day -= 30
		mon += 1
	elif (day > 28) and (mon == 2) and (year % 4 != 0):
		day -= 28
		mon += 1
	elif (day > 29) and (mon == 2):
		day -= 29
		mon += 1
	if (mon > 12):
		mon -= 12
		year += 1
	if day == 1:
		hits += 1
	print(str(day) + " - " + str(mon) + " - " + str(year))
print(hits)