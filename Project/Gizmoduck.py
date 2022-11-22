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

	'''
	constructor for Gizmoduck object
	arguments street_initial and avenue_initial are integers from the Navigation file
	'''
	def __init__(self, x_initial, y_initial):
		DuckDrive.set_x_coordinate = x_initial
		DuckDrive.set_y_coordinate = y_initial

	'''
	This is the main routine for the Gizmoduck object. consider it the actual main() once the Left or Right dock positioning is established by the executable script.
	'''
	def run_expedition(self):
		step=1
		#if there is a fish to check, find a way to the dock and then run that in reverse to go back to where we wer ein the main process
		print('left light level reading: ', DuckEyes.get_left_level())
		print('right light level reading: ', DuckEyes.get_right_level())
		while step<12:
			path = Navigation.get_path_by_ID(step)
			print('step:', step, ' with distance :', path[Navigation.INDEX_DISTANCE], ' and rotation: ', path[Navigation.INDEX_ROTATION], ' and fish status:', path[Navigation.INDEX_FISH])
			#DuckDrive.move_forward_unchecked(path[Navigation.INDEX_DISTANCE])
			undershoot_compensation = DuckDrive.move_forward_by_blocks(path[Navigation.INDEX_DISTANCE], path[Navigation.INDEX_TRACKING_EDGE], path[Navigation.INDEX_ROTATION])
			#DuckDrive.rotate_degrees_unchecked(path[Navigation.INDEX_ROTATION])
			DuckDrive.rotate_degrees(path[Navigation.INDEX_ROTATION], undershoot_compensation)
			step+=1


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
		