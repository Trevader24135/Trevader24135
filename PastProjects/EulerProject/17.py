import math

def text(num,slot):
	if slot == 1:
		return {
			'0': "",
			'1': "one",
			'2': "two",
			'3': "three",
			'4': "four",
			'5': "five",
			'6': "six",
			'7': "seven",
			'8': "eight",
			'9': "nine",
			'10': "ten",
			'11': "eleven",
			'12': "twelve",
			'13': "thirteen",
			'14': "fourteen",
			'15': "fifteen",
			'16': "sixteen",
			'17': "seventeen",
			'18': "eighteen",
			'19': "nineteen",
			
		}[num]
	elif slot == 10:
		return {
			'0': "",
			'2': "twenty",
			'3': "thirty",
			'4': "fourty",
			'5': "fifty",
			'6': "sixty",
			'7': "seventy",
			'8': "eighty",
			'9': "ninety",
		}[num]
num = 341
L = 0
for i in range(342,num + 1):
	if i < 20:
		L += len(text(str(i),1))
	elif i < 100:
		#print(i,math.floor(i / 10) * 10)
		L += len(text(str(int(math.floor(i/10))),10))
		L += len(text(str(int(i-(10 * math.floor(i / 10)))),1))
	elif i < 1000:
		L += len(text(str(int(math.floor(i/100))),1)) + len("hundredand")
		if int(i - (100 * math.floor(i / 100))) < 20:
			L += len(text(str(int(i - (100 * math.floor(i / 100)))),1))
		else:
			L += len(text(str(int(math.floor((i - (100 * math.floor(i / 100)))/10))),10))
			L += len(text(str(int(i - (10 * math.floor(i / 10)))),1))
	print(L)
L += len("onethousand")
print(L)