import numpy as np
import pandas as pd


df = pd.DataFrame()
print(df)

try:
	chunk = 0
	while True:
# 		for i in range(bit_size):
# 			timecode[i] = time()		
# 			data[i] = t.get_position(total=True)
        datachunk=np.load(f"{path}\Treadmill-data_{chunk}", data = data, timecode = timecode)
        chunk += 1        