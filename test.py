from base import Treadmill


channel = 'Dev1/ai0' # Replace this with your channel!

t = Treadmill(light_channel = channel)
t.calibrate()
n = 100
try:
	while True:
		pos = t.get_position()
		prog = int(pos*(n+1) / t.belt_length)
		print('\r |' + ('#'*prog) + ('-'*(n-prog)) + '| ' + f'{round(pos, 1)}'.zfill(6), end='')
finally:
	print('')
