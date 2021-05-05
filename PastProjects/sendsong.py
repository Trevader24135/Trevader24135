import serial
import io
import time
import keyboard
import os

ser = serial.Serial("COM4", 250000, timeout = 0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
time.sleep(5)

file = open("song.gcode", "r")
line = file.readline()
sio.write(line + "\n")
sio.flush()
for line in file:
	while sio.readline() == "":
		pass
	print(line)
	sio.write(line + "\n")
	sio.flush()
	
ser.close()