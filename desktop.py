import ctypes
import time
import os, os.path
import random

class times:
	def __init__(self, start_time, end_time):
		self.start_time = start_time
		self.end_time = end_time


# The Directiories for our images
wallpapers = os.path.join(os.path.expanduser('~'), 'Pictures', 'Wallpapers')
workDir = os.path.join(wallpapers, 'Motivational')
playDir = os.path.join(wallpapers, 'Generic')

# Our 'Schedule' Dictionary of start and end times
schedule = []
schedule.append(times(19,22))

working = False

while (True):
	# Get our current time
	currTime = time.localtime()

	# Check if we should be working
	for i in schedule:
		if i.start_time > currTime.tm_hour and i.end_time < currTime.tm_hour:
			working = True
	
	if currTime.tm_sec % 30 == 0:
		if working:
			path = os.path.join(workDir, random.choice(os.listdir(workDir)))
		else:
			path = os.path.join(playDir, random.choice(os.listdir(playDir)))
		
		print(path, ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3))
		time.sleep(1)
			

