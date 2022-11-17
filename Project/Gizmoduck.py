#!/usr/bin/env pybricks-micropython
import Navigation
import DuckEyes
import DuckFlippers
import DuckDrive

'''
this file holds data for the overall operation of the robot, calls functions in Navigation and in Grabbing to get path info.
should there be a separate script to deal with actually moving? or should Grabbing just be included in this file?
'''
class Gizmoduck:
	#CONSTANTS


	#VARIABLES
	street_current = 0
	avenue_current = 0

	'''
	constructor for Gizmoduck object
	arguments street_initial and avenue_initial are integers from the Navigation file
	'''
	def __init__(self, street_initial, avenue_initial):
		self.street_current = street_initial
		self.avenue_current = avenue_initial

	'''
	This is the main routine for the Gizmoduck object. consider it the actual main() once the Left or Right dock positioning is established by the executable script.
	'''
	def run_expedition(self):
		#with the starting position known, start getting a list of movement instructions then execute the movement, make any inspections needed with the sensors, and either grab and drop the target or continue on to the next path.
		step=1 #keeps track of the step of the instructions that we are on
		while step<4:
			path = Navigation.get_path_by_ID(step)
			print('step:', step, ' with distance :', path[Navigation.INDEX_DISTANCE], ' and rotation: ', path[Navigation.INDEX_ROTATION], ' and fish status:', path[Navigation.INDEX_FISH])
			DuckDrive.move_forward_unchecked(path[Navigation.INDEX_DISTANCE])
			DuckDrive.rotate_degrees_unchecked(path[Navigation.INDEX_ROTATION])
			step+=1
			#branch test
	'''
	given that we are at the right dock, relocate to the starting position on the left dock
	'''
	def relocate_dock_left(self):
		return
		
	'''
	given that we are at the left dock, relocate to the starting position on the right dock
	'''
	def relocate_dock_right():
		DuckDrive.rotate_degrees_unchecked(90)
		DuckDrive.move_forward_unchecked(2)
		DuckDrive.rotate_degrees_unchecked(-90)
		