import ctypes
import time
import os, os.path
import random

# Represents our Time Objects for the purposes of our schedule list
class times:
	def __init__(self, start_time, end_time):
		self.start_time = start_time
		self.end_time = end_time


# The Directiories for our images
wallpapers = os.path.join(os.path.expanduser('~'), 'Pictures', 'Wallpapers')
workDir = os.path.join(wallpapers, 'Motivational')
genericDir = os.path.join(wallpapers, 'Generic')

# Our 'Schedule' Dictionary of start and end times
# Each time object represents the 24 hour start and end hours
schedule = []
schedule.append(times(19,22))

# Set the inital Working Variable
working = False

# The number of minutes to wait inbetween wallpaper changes
changeDelay = 5

# Our main loop
while (True):
	# Get our current time
	currTime = time.localtime()

	# Check if we should be working
	for i in schedule:
		if i.start_time >= currTime.tm_hour and i.end_time <= currTime.tm_hour:
			working = True
	
	# See if we should be updating the wallpaper
	if currTime.tm_min % changeDelay == 0:
		# If we are working, make the path the Working Wallpapers
		if working:
			path = os.path.join(workDir, random.choice(os.listdir(workDir)))
		# If we aren't working, make the path the generic wallpapers
		else:
			path = os.path.join(genericDir, random.choice(os.listdir(genericDir)))
		
		# Sets the Wallpaper to the set path
		print(path, ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0))
		# sleeps the program for 60 seconds
		# this ensures we don't set the wallpaper every loop for the given minute 
		time.sleep(60)
			

