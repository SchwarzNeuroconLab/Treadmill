from base import Treadmill
import numpy as np
from time import time

channel = 'Dev1/ai0'
bit_size = 10000


belt_length = input("How long is the belt in mm? (Press enter without input to start calibration) ")

if len(belt_length) == 0:
	t = Treadmill(light_channel = channel)
else:
	t = Treadmill(light_channel = channel, belt_length = int(belt_length))

print("Starting...")
print("Press Ctrl+C to stop")

data = np.zeros(bit_size)
timecode = np.zeros(bit_size)

try:
	chunk = 0
	while True:
		for i in range(bit_size):
			timecode[i] = time()		
			data[i] = t.get_position()
		np.savez(f"data_{chunk}", data = data, timecode = timecode)
		chunk += 1
finally:
	np.savez(f"data_{chunk}", position = data[:i], timecode = timecode[:i])
