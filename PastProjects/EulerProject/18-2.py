py = [[75],[95,64],[17,47,82],[18,35,87,10],[20, 4,82,47,65],[19, 1,23,75, 3,34],[88, 2,77,73, 7,63,67],[99,65, 4,28, 6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]]
row = 1
rows = len(py)
total = py[0][0]

def left():
	del py[0]
	for i in range(len(py)):
		del py[i][len(py[i])-1]
	
def right():
	del py[0]
	for i in range(len(py)):
		del py[i][0]	

print(py[0][0])
while len(py) > 1:
	#print(str(py) + " | " + str(total))
	
	if len(py) >= 3:
		LL = py[1][0] + py[2][0]
		LR = py[1][0] + py[2][1]
		RL = py[1][1] + py[2][1]
		RR = py[1][0] + py[2][2]
		if (LL > RL and LL > RR) or (LR > RL and LR > RR):
			left()
		else:
			right()
	else:
		if py[1][0] > py[1][1]:
			left()
		else:
			right()
	print(str(py[0][0]) + " | LL: " + str(LL) + " | LR: " + str(LR) + " | RL: " + str(RL) + " | RR: " + str(RR) + " | Row: " + str(row))
	row += 1
	if py != []:
		total += py[0][0]
	
print(total)