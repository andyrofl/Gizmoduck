#!/usr/bin/env pybricks-micropython

#CONSTANTS
INDEX_DISTANCE = 0
INDEX_ROTATION = 1
INDEX_TRACKING_EDGE = 2
INDEX_FISH = 3

EDGE_LEFT = -1
EDGE_CENTER = 0
EDGE_RIGHT = 1

ROTATE_90_LEFT = -90
ROTATE_90_RIGHT = 90
ROTATE_NONE = 0
'''
Each step in the instructions is manually entered here
'''

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=0		#True=check fish, False=do nothing   0 do nothing, greater than zero go that distance to be near the fish
	if(step == 1):
		forward_distance=6
		turn_angle=ROTATE_90_RIGHT
		tracking_edge=EDGE_RIGHT
	elif(step == 2):
		forward_distance=2
		turn_angle=ROTATE_90_RIGHT
		tracking_edge=EDGE_RIGHT
	elif(step == 3):
		forward_distance=2
		turn_angle=ROTATE_90_RIGHT
		tracking_edge=EDGE_RIGHT
	elif(step == 4):
		forward_distance=2
		turn_angle=ROTATE_90_LEFT
		tracking_edge=EDGE_RIGHT
	elif(step == 5):
		forward_distance=0.5
		turn_angle=ROTATE_90_LEFT
		tracking_edge=EDGE_RIGHT
	elif(step == 6):
		forward_distance=2
		turn_angle=ROTATE_90_RIGHT
		tracking_edge=EDGE_RIGHT
	elif(step == 7):
		forward_distance=1
		turn_angle=ROTATE_90_RIGHT
		tracking_edge=EDGE_RIGHT
	elif(step == 8):
		forward_distance=2
		turn_angle=ROTATE_90_LEFT
		tracking_edge=EDGE_RIGHT
	elif(step == 9):
		forward_distance=2
		turn_angle=ROTATE_90_LEFT
		tracking_edge=EDGE_RIGHT
	elif(step == 10):
		forward_distance=2
		turn_angle=ROTATE_NONE
		tracking_edge=EDGE_CENTER
	elif(step == 11):
		forward_distance=0
		turn_angle=ROTATE_NONE
		tracking_edge=EDGE_CENTER
		check_fish=57

	return [forward_distance, turn_angle, tracking_edge, check_fish]
'''
	function returns a set of instructions to navigate from the current point to the dock and back
	IDs are not the same as the previous function and are specific to the location of each fish
'''
def get_return_path_by_fishID(fishID, step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	drop_fish=0
	if(fishID ==1):
		#need to differentiate between path to dock and path back to original location?
		if(step ==1):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==2):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==3):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==4):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==5):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==6):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0
		if(step ==7):
			forward_distance=0
			turn_angle=0
			tracking_edge=EDGE_CENTER
			drop_fish=0

	return [forward_distance, turn_angle, tracking_edge]