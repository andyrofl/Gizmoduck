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
	last_turn_condition = False
	'''
	constructor for Gizmoduck object
	arguments street_initial and avenue_initial are integers from the Navigation file
	'''
	def __init__(self, x_initial, y_initial):
		DuckDrive.set_x_coordinate = x_initial
		DuckDrive.set_y_coordinate = y_initial
		DuckDrive.calibrate_sensors()

	'''
	This is the main routine for the Gizmoduck object. consider it the actual main() once the Left or Right dock positioning is established by the executable script.
	'''
	def run_expedition(self):
		step=1
		last_turn_condition = False
		#if there is a fish to check, find a way to the dock and then run that in reverse to go back to where we wer ein the main process
		while step<12:
			path = Navigation.get_path_by_ID(step)
			print('step:', step, ' with distance :', path[Navigation.INDEX_DISTANCE], ' and rotation: ', path[Navigation.INDEX_ROTATION], ' and fish status:', path[Navigation.INDEX_FISH])
			last_turn_condition = DuckDrive.move_forward_by_blocks(path[Navigation.INDEX_DISTANCE], path[Navigation.INDEX_TRACKING_EDGE], path[Navigation.INDEX_ROTATION], last_turn_condition)
			DuckDrive.rotate_degrees(path[Navigation.INDEX_ROTATION])
			if(path[Navigation.INDEX_FISH]>0):
				print('there is a fish to catch')
				#check if the fish is valid
					#execute nested loop for return and stuff
						#if value states to grab the fish
							# grab the fish
						#if value states to drop the fish
							# drop the fish
					#exit the subroutine
			step+=1

		