
class opCodes:
	def ZeroSourceOne(registerT):
		return registerT + "00"
		
	def OneSourceZero(registerA):
		return "0" + registerA + "0"

	def OneSourceOne(registerT, registerA):
		return registerT + registerA + "0"

	def TwoSourceZero(registerA, registerB):
  		return "0" + registerA + registerB
	
	def TwoSourceOne(registerT, registerA, registerB):
		return registerT + registerA + registerB


	def Load(registerT, data):
		if len(data) == 1:
			data = "0" + data
		return "01" + registerT + data

	def Move(registerT, registerA):
		return "02" + opCodes.OneSourceOne(registerT, registerA)

	def Disp(registerA):
		return "03" + opCodes.OneSourceZero(registerA)

	def Hop(Data):
		return "050" + Data

	def Loc():
		return "06000"

	def Goto(Data):
		return "070" + Data

	def Branch(Data):
		return "080" + Data
	
	def Spop():
		return "09000"

	def Loop():
		return "0a000"

	def Return():
		return "0b000"

	def Store(registerA, registerB):
		return "0d" + opCodes.TwoSourceZero(registerA, registerB)

	def Read(registerT, registerA):
		return "0e" + opCodes.OneSourceOne(registerT, registerA)


	def Not(registerT, registerA):
		return "10" + opCodes.OneSourceOne(registerT, registerA)

	def And(registerT, registerA, registerB):
		return "11" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Or(registerT, registerA, registerB):
		return "12" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Xor(registerT, registerA, registerB):
		return "13" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def ShiftLeft(registerT, registerA):
		return "14" + opCodes.OneSourceOne(registerT, registerA)

	def ShiftRight(registerT, registerA):
		return "15" + opCodes.OneSourceOne(registerT, registerA)

	def Add(registerT, registerA, registerB):
		return "16" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Sub(registerT, registerA, registerB):
		return "17" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Mult(registerT, registerA, registerB):
		return "18" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Div(registerT, registerA, registerB):
		return "19" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Equal(registerT, registerA, registerB):
		return "1a" + opCodes.TwoSourceOne(registerT, registerA, registerB)

	def Greater(registerT, registerA, registerB):
		return "1b" + opCodes.TwoSourceOne(registerT, registerA, registerB)
	
	def Test(registerA, registerB):
		return "1c" + opCodes.TwoSourceZero(registerA, registerB)

	def Ascii0(registerT, registerA):
		return "1d" + opCodes.OneSourceOne(registerT, registerA)
	
	def Ascii1(registerT, registerA):
		return "1e" + opCodes.OneSourceOne(registerT, registerA)
	
	def Ascii2(registerT, registerA):
		return "1f" + opCodes.OneSourceOne(registerT, registerA)

	def Print(args):
		return None

fileName = input("name of file: ")
#fileName="program.txt"
with open(fileName, 'r') as textFile:
	print("v2.0 raw")
	lineOffset = 0
	codes = []
	for lineNum, line in enumerate(textFile.readlines()):
		line = line.rstrip("\n")
		if ";" in line:
			line = line.split(";")[0]
		
		line = line.split(" ")
		key = ""
		
		if line[0] == "LD":
			key = opCodes.Load(*line[1:3])
		elif line[0] == "MOV":
			key = opCodes.Move(*line[1:3])
		elif line[0] == "DISP":
			key = opCodes.Disp(*line[1:2])
		elif line[0] == "LOC":
			key = opCodes.Loc()
		elif line[0] == "GOTO":
			key = opCodes.Goto(*line[1:2])
		elif line[0] == "HOP":
			key = opCodes.Hop(*line[1:2])
		elif line[0] == "BRANCH":
			key = opCodes.Branch(*line[1:2])
		elif line[0] == "LOOP":
			key = opCodes.Loop()
		elif line[0] == "SPOP":
			key = opCodes.Spop()
		elif line[0] == "RETURN":
			key = opCodes.Return()

		elif line[0] == "STORE":
			key = opCodes.Store(*line[1:3])
		elif line[0] == "READ":
			key = opCodes.Read(*line[1:3])

		elif line[0] == "NOT":
			key = opCodes.Not(*line[1:3])
		elif line[0] == "AND":
			key = opCodes.And(*line[1:4])
		elif line[0] == "OR":
			key = opCodes.Or(*line[1:4])
		elif line[0] == "XOR":
			key = opCodes.Xor(*line[1:4])
		elif line[0] == "SHL":
			key = opCodes.ShiftLeft(*line[1:3])
		elif line[0] == "SHR":
			key = opCodes.ShiftRight(*line[1:3])
		elif line[0] == "ADD":
			key = opCodes.Add(*line[1:4])
		elif line[0] == "SUB":
			key = opCodes.Sub(*line[1:4])
		elif line[0] == "MULT":
			key = opCodes.Mult(*line[1:4])
		elif line[0] == "DIV":
			key = opCodes.Div(*line[1:4])
		elif line[0] == "EQL":
			key = opCodes.Equal(*line[1:4])
		elif line[0] == "GRTR":
			key = opCodes.Greater(*line[1:4])
		elif line[0] == "TEST":
			key = opCodes.Test(*line[1:3])
		elif line[0] == "ASCII0":
			key = opCodes.Ascii0(*line[1:3])
		elif line[0] == "ASCII1":
			key = opCodes.Ascii1(*line[1:3])
		elif line[0] == "ASCII2":
			key = opCodes.Ascii2(*line[1:3])
		if key != "":
			codes.append(key)
		else:
			codes.append("00000")

i = 0
while len(codes) != 0: 
	print(codes[0], end=" ")
	codes.pop(0)
	i += 1
	if i % 8 == 0:
		i = 0
		print()