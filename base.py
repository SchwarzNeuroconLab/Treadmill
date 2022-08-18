import nidaqmx as ni
import atexit

class Treadmill:
	def __init__(self, light_channel, belt_length = None):
		''' Class for using the Treadmill
			If no belt length is specified, a calibration process is needed. Otherwise
			no calibration is necessary but usefull to get a position relative to the marker
			on the belt. '''
		self.rotation = self.RotaryEncoder()
		self.laser = self.Light(channel = light_channel)
		self.radius = 57.6#mm Inaccurate! Please measure again
		if belt_length is None: self.calibrated = False
		else:
			if type(belt_length) is int or float:
				self.belt_length = belt_length
				self.offset = 0
				self.calibrated = True
			else: raise TypeError(f"Belt Length must be integer or float, not {type(belt_length)}!")
	def calibrate(self):
		print("Please rotate the belt!")
		start = None
		end = None
		while start is None:
			if self.laser.read(): start = self.rotation.read()
		print("Start found")
		self.offset = start
		while end is None:
			if self.laser.read():
				end = self.rotation.read()
				if self.radius*abs(start-end) < 20: end = None		# If belt ran less than 20mm, it hasn't run a full round
		self.belt_length = self.radius*abs(start-end)#mm
		print(f"Belt length: {round(self.belt_length, 1)}mm")
		self.calibrated = True
	def get_position(self, total = False):
		''' Function to get the current position of the Treadmill.'''
		if not total and not self.calibrated: raise Exception("For belt positions the Treadmill has to be calibrated. Please run Treadmill.calibrate()")
		if total: return self.rotation.read()*self.radius
		else: return ((self.rotation.read() - self.offset)*self.radius) % self.belt_length
	class RotaryEncoder:
		def __init__(self):
			ptask = ni.system.storage.persisted_task.PersistedTask('Treadmill Position')
			self.task = ptask.load()
			self.task.start()
			atexit.register(self.close)
		def read(self):
			return self.task.read()
		def close(self):
			self.task.close()
	class Light:
		def __init__(self, channel):
			self.channel = channel
			self.limit = 5
			self.task = ni.Task()
			self.task.ai_channels.add_ai_voltage_chan(self.channel)
			atexit.register(self.close)
		def read(self):
			return self.task.read() > self.limit
		def close(self):
			self.task.close()
