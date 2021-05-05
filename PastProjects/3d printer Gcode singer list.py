import math
import os
import itertools
key = 2

def note(n, o, s ='n'):
	if n == 'r':
		return 10
	elif n == "c":
		if s == "n":
			f = 16.35160
		elif s == "f":
			f = 15.43386
		elif s == "s":
			f = 17.32391
	elif n == "d":
		if s == "n":
			f = 18.35405
		elif s == "f":
			f = 17.32391
		elif s == "s":
			f = 19.44544
	elif n == "e":
		if s == "n":
			f = 20.60172
		elif s == "f":
			f = 19.44544
		elif s == "s":
			f = 21.82676
	elif n == "f":
		if s == "n":
			f = 21.82676
		elif s == "f":
			f = 20.60172
		elif s == "s":
			f = 23.12465
	elif n == "g":
		if s == "n":
			f = 24.49971
		elif s == "f":
			f = 23.12465
		elif s == "s":
			f = 25.95654
	elif n == "a":
		if s == "n":
			f = 27.50000
		elif s == "f":
			f = 25.95654
		elif s == "s":
			f = 29.13524
	elif n == "b":
		if s == "n":
			f = 30.86771
		elif s == "f":
			f = 29.13524
		elif s == "s":
			f = 32.70320
	return f * (2**o)
for i in range(8):
	exec("c%d = note('c',%i,'n')" % (i,i))
	exec("d%d = note('d',%i,'n')" % (i,i))
	exec("e%d = note('e',%i,'f')" % (i,i))
	exec("f%d = note('f',%i,'n')" % (i,i))
	exec("g%d = note('g',%i,'n')" % (i,i))
	exec("a%d = note('a',%i,'n')" % (i,i))
	exec("b%d = note('b',%i,'f')" % (i,i))
rr = 10

c = 'c'
s = 's'
tempo = 130
""",
		[,,,,,,,],[,,,,,,,]"""
znotes = [[b5],[s],#0
		[c6,c6,b5,b5,a5,g5,g5,c6],[c,s,c,s,s,c,s,c],
		[c6,b5,b5,a5,a5,g5,g5,g5],[s,c,s,c,s,c,s,s],
		[f5,f5,f5,e5,e5,rr,f5,d5],[c,c,s,s,s,s,s,c],
		[d5,d5,d5,d5,d5,d5,rr,d5],[c,c,c,c,c,s,s,s],
		[d5,d5,d5,d5,d5,d6,d6,d6],[c,s,s,c,s,s,c,c],
		[d6,d6,d6,d6,d6,d6,rr,b5],[c,c,c,c,c,s,s,s],#6
		[a5,a5,a5,a5,a5,b5,b5,b5],[c,s,s,c,s,s,c,c],
		[b5,b5,b5,b5,b5,b5,rr,b5],[c,c,c,c,c,s,s,s],
		[c6,c6,b5,b5,a5,g5,g5,c6],[c,s,c,s,s,c,s,c],
		[c6,b5,b5,a5,a5,g5,g5,g5],[s,c,s,c,s,c,s,s],#10
		[f5,f5,f5,e5,e5,rr,f5,d5],[c,c,s,s,s,s,s,c],
		[d5,d5,d5,d5,d5,d5,rr,d5],[c,c,c,c,c,s,s,s],
		[d5,d5,d5,d5,d5,d6,d6,d6],[c,s,s,c,s,s,c,c],
		[d6,d6,d6,d6,d6,d6,rr,b5],[c,c,c,c,c,s,s,s],#14
		[a5,a5,a5,a5,a5,b5,b5,b5],[c,s,s,c,s,s,c,s]]
xnotes = [[],[],#0
		[g5,g5,g5,g5,g5,g5,b5,b5],[c,c,c,c,c,s,c,s],
		[e5,e5,e5,e5,e5,e5,g5,g5],[c,c,c,c,c,s,c,s],
		[f5,f5,f5,f5,f5,f5,a5,a5],[c,c,c,c,c,s,c,s],
		[g5,g5,g5,g5,g5,g5,rr,d4],[c,c,c,c,c,s,s,s],
		[d4,d4,d4,d4,d4,d5,d5,d5],[c,s,s,c,s,s,c,c],
		[d5,d5,d5,d5,d5,d5,rr,b4],[c,c,c,c,c,s,s,s],#6
		[a4,a4,a4,a4,a4,b4,b4,b4],[c,s,s,c,s,s,c,c],
		[b4,b4,b4,b4,b4,b4,rr,rr],[c,c,c,c,c,s,s,s],
		[rr,c5,rr,b4,a4,rr,g4,g4],[s,s,s,s,s,s,c,s],
		[c5,rr,b4,a4,rr,g4,g4,rr],[s,s,s,s,s,c,s,s],#10
		[a4,b4,rr,rr,a4,a4,a4,a4],[s,s,s,s,c,c,c,s],
		[rr,a4,b4,rr,a4,b4,rr,d4],[s,s,s,s,s,s,s,s],
		[d4,d4,d4,d4,d4,d5,d5,d5],[c,s,s,c,s,s,c,c],
		[d5,d5,d5,d5,d5,d5,rr,b4],[c,c,c,c,c,s,s,s],#14
		[a4,a4,a4,a4,a4,b4,b4,b4],[c,s,s,c,s,s,c,s]]
ynotes = [[],[],#0
		[],[],
		[],[],
		[],[],
		[],[],
		[e3,b3,g4,e3,b3,f4,b4,d5],[s,s,s,s,s,s,s,s],
		[g3,d4,b4,g3,d4,b4,g3,d4],[s,s,s,s,s,s,s,s],#6
		[f3,c4,a4,f3,c4,a4,b4,c5],[s,s,s,s,s,s,s,s],
		[g3,d4,b4,g3,d4,b4,g3,d4],[s,s,s,s,s,s,s,s],
		[e3,b3,g4,e3,b3,g4,e3,b3],[s,s,s,s,s,s,s,s],
		[g3,d4,b4,g3,d4,b4,g3,d4],[s,s,s,s,s,s,s,s],#10
		[f3,c4,a4,f3,c4,a4,f3,c4],[s,s,s,s,s,s,s,s],
		[g3,d4,b4,g3,d4,b4,g3,d4],[s,s,s,s,s,s,s,s],
		[e3,b3,g4,e3,b3,g4,e3,b3],[s,s,s,s,s,s,s,s],
		[g3,d4,b4,g3,d4,b4,g3,d4],[s,s,s,s,s,s,s,s],#14
		[f3,c4,a4,f3,c4,a4,f3,f3],[s,s,s,s,s,s,s,s],]

endrat = .95

xmin = 20
xhome = 130
xmax = 200
ymin = 20
yhome = 155
ymax = 200
zmin = 1.5
zhome = 1.67
zmax = 50
xdirection = 1
ydirection = 1
zdirection = 1

#the multiplication value to change between the feedrate and the frequency
FrtFqX = 1.65
FqtFrX = FrtFqX**-1
FrtFqZ = 6.7
FqtFrZ = FrtFqZ**-1

file = open("song.gcode", mode="w")
file.write("""G28;Home
G1 X%f Y%f Z%f F40
""" % (xhome,yhome,zhome + 1.33))

x = xhome
y = yhome
z = zhome + 1.33

for xx,yy,zz,xxt,yyt,zzt in zip(xnotes[0::2],ynotes[0::2],znotes[0::2],xnotes[1::2],ynotes[1::2],znotes[1::2]):
	for xnote,ynote,znote,xt,yt,zt in itertools.zip_longest(xx,yy,zz,xxt,yyt,zzt):
		#print(xnote,ynote,znote,xt,yt,zt)
		#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
		if znote == None:
			znote = 20
		feedz = znote * FqtFrZ
		deltaz = feedz * (4 / (8 * tempo))
		#print("deltaz: ", deltaz)
		if z + deltaz >= zmax and zdirection == 1:
			zdirection = -1
		elif z - deltaz <= zmin and zdirection == -1:
			zdirection = 1
		ztarget = z + (deltaz * zdirection * endrat)
		#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
		if xnote == None:
			xnote = 20
		feedx = xnote * FqtFrX
		deltax = feedx * (4 / (8 * tempo))
		#print("deltax: ", deltax)
		if x + deltax >= xmax and xdirection == 1:
			xdirection = -1
		elif x - deltax <= xmin and xdirection == -1:
			xdirection = 1
		xtarget = x + (deltax * xdirection * endrat)
		#YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
		if ynote == None:
			ynote = 20
		feedy = ynote * FqtFrX
		deltay = feedy * (4 / (8 * tempo))
		#print("deltay: ", deltay)
		if y + deltay >= ymax and ydirection == 1:
			ydirection = -1
		elif y - deltay <= ymin and ydirection == -1:
			ydirection = 1
		ytarget = y + (deltay * ydirection * endrat)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		file.write("G1 X%f Y%f Z%f F%f ;XDir:%d,YDir:%d,ZDir:%d, \n" %(xtarget,ytarget,ztarget,(feedx**2 + feedy**2 + feedz**2)**(1/2),xdirection,ydirection,zdirection))
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		x = xtarget
		y = ytarget
		z = ztarget
		#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
		if znote == None or zt == s:
			znote = 20
		feedz = znote * FqtFrZ
		deltaz = feedz * (4 / (8 * tempo))
		#print("deltaz: ", deltaz)
		if z + deltaz >= zmax and zdirection == 1:
			zdirection = -1
		elif z - deltaz <= zmin and zdirection == -1:
			zdirection = 1
		ztarget = z + (deltaz * zdirection * (1-endrat))
		#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
		if xnote == None or xt == s:
			xnote = 20
		feedx = xnote * FqtFrX
		deltax = feedx * (4 / (8 * tempo))
		#print("deltax: ", deltax)
		if x + deltax >= xmax and xdirection == 1:
			xdirection = -1
		elif x - deltax <= xmin and xdirection == -1:
			xdirection = 1
		xtarget = x + (deltax * xdirection * (1-endrat))
		#YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
		if ynote == None or yt == s:
			ynote = 20
		feedy = ynote * FqtFrX
		deltay = feedy * (4 / (8 * tempo))
		#print("deltay: ", deltay)
		if y + deltay >= ymax and ydirection == 1:
			ydirection = -1
		elif y - deltay <= ymin and ydirection == -1:
			ydirection = 1
		ytarget = y + (deltay * ydirection * (1-endrat))
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		file.write("G1 X%f Y%f Z%f F%f ;XDir:%d,YDir:%d,ZDir:%d, \n" %(xtarget,ytarget,ztarget,(feedx**2 + feedy**2 + feedz**2)**(1/2),xdirection,ydirection,zdirection))
		x = xtarget
		y = ytarget
		z = ztarget
