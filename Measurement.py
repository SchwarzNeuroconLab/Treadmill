from base import Treadmill
import numpy as np
from time import time
import os

channel = 'Dev1/ai0'
bit_size = 10000

"""Experiment"""

t = Treadmill(light_channel = channel)
t.calibrate()
input("Press Enter to continue...")

n = 100
pos = t.get_position()
prog = int(pos*(n+1) / t.belt_length)
print('\r |' + ('#'*prog) + ('-'*(n-prog)) + '| ' + f'{round(pos, 1)}'.zfill(6), end='')

print("Starting...")
print("Press Ctrl+C/Ctrl+F2 to stop")

data = np.zeros(bit_size)
timecode = np.zeros(bit_size)

"""File Names"""
pr = "B01-3" #project
exp = "1.1" #experiment
gr = "Ta1" #group
an = "MT-04.1" #animal
folder = f"{pr}_{exp}_{gr}_{an}" #folder name
he = "r" #hemisphere
he = "left" if he == "l" else "right" if he == "r" else None #writing out hemisphere name
path = f"D:\Liliia\Treadmill Recordings\{folder}" #path with folder
sub = f"{path}\{he}" #subdirectory within folder
if os.path.isdir(sub):
	print(f"subdirectory {sub} already exists")
else:
	if os.path.isdir(path):
		print(f"path {path} already exists")
	else:
		os.mkdir(path)
		print(f"path {path} is created")
	os.mkdir(sub)
	print(f"subdirectory {sub} is created")
os.chdir(sub)
#try:
#	os.chdir(folder)
#except:
#	os.mkdir(folder)
#	os.chdir(folder)
#try:
#	os.chdir(he)
#except:
#	os.mkdir(he)
#	os.chdir(he)

"""Saving Measurements"""
try:
	chunk = 0
	while True:
		for i in range(bit_size):
			timecode[i] = time()		
			data[i] = t.get_position(total=True)
		file=f"{sub}\Treadmill-data_{chunk}_(belt-length {round(t.belt_length)} mm)"
		np.savez(file, data=data, timecode=timecode)
		print(f"{chunk} - saving chunk {chunk} to {file}")
		chunk += 1

except KeyboardInterrupt:
	print("Exiting")
finally:
	np.savez(f"{sub}\Treadmill-data_{chunk}_(belt-length {round(t.belt_length)} mm", position=data[:i], timecode=timecode[:i])