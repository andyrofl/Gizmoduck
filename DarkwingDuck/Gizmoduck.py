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

	#VARIABLES
	last_turn_condition = False
	'''
	constructor for Gizmoduck object
	arguments street_initial and avenue_initial are integers from the Navigation file
	'''
	def __init__(self, x_initial, y_initial):
		#DuckDrive.set_x_coordinate = x_initial
		#DuckDrive.set_y_coordinate = y_initial
		DuckDrive.calibrate_sensors()

	'''
	This is the main routine for the Gizmoduck object. consider it the actual main() once the Left or Right dock positioning is established by the executable script.
	'''
	def run_expedition(self):
		step=1
		last_turn_condition = False
		while step<53:#change value to maximum number of steps in path
			path = Navigation.get_path_by_ID(step)
			print('step:', step, ' with distance :', path[Navigation.INDEX_DISTANCE], ' and rotation: ', path[Navigation.INDEX_ROTATION], ' and fish status:', path[Navigation.INDEX_FISH])
			if(path[Navigation.INDEX_TRACKING_EDGE] == Navigation.EDGE_CENTER):
				print('entered unchecked function ', path[Navigation.INDEX_DISTANCE], step)
				last_turn_condition = DuckDrive.move_forward_unchecked(path[Navigation.INDEX_DISTANCE])#, path[Navigation.INDEX_ROTATION])
			else:
				last_turn_condition = DuckDrive.move_forward_by_blocks(path[Navigation.INDEX_DISTANCE], path[Navigation.INDEX_TRACKING_EDGE], path[Navigation.INDEX_ROTATION], last_turn_condition, path[Navigation.INDEX_FISH])
			DuckDrive.rotate_degrees(path[Navigation.INDEX_ROTATION])
			'''if(path[Navigation.INDEX_FISH]>0):
				if(True): #if fish is valid
					# grab the fish
					print('there is a fish to catch')
					return_step = 1
					return_turn_condition= False
					while return_step<12:#change value to maximum number of steps that can exist in a return path
						return_path = Navigation.get_return_path_by_fishID(step, return_step)
						if(return_path == None): #might not work lol
							break
						#if value states to drop the fish
							# drop the fish
						print('step:', return_step, ' with distance :', return_path[Navigation.INDEX_DISTANCE], ' and rotation: ', return_path[Navigation.INDEX_ROTATION], ' and fish status:', return_path[Navigation.INDEX_FISH])
						if(path[Navigation.INDEX_TRACKING_EDGE == Navigation.EDGE_CENTER]):
							last_turn_condition = DuckDrive.move_forward_unchecked(return_path[Navigation.INDEX_DISTANCE])#, return_path[Navigation.INDEX_ROTATION])
						else:
							last_turn_condition = DuckDrive.move_forward_by_blocks(return_path[Navigation.INDEX_DISTANCE], return_path[Navigation.INDEX_TRACKING_EDGE], return_path[Navigation.INDEX_ROTATION], return_turn_condition)
						DuckDrive.rotate_degrees(return_path[Navigation.INDEX_ROTATION])'''
				#if fish is invalid, exit and continue with main route
			#if there is no fish to check exit and continue with main route
			step+=1

		