#multiples = [] #declaring an array
Sum = 0 # We want sum to start as 0

for i in range(1000): #for every whole number below 1000, store that number in i, then do this
	if i % 3 == 0: # if the remainder of i / 3 is 0
		#multiples.append(i) #add the number currently in i into the array
		Sum += i
	elif i % 5 == 0:# if the remainder of i / 5 is 0
		#multiples.append(i) #add the number currently in i into the array
		Sum += i

#for i in multiples: #for every value in the array called multiples, store that value in i, and loop
	#Sum += i
	
print(Sum)
