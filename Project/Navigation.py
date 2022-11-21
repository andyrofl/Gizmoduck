#!/usr/bin/env pybricks-micropython

#CONSTANTS
STREET_1 = 1
STREET_2 = 2
STREET_3 = 3
STREET_4 = 4
STREET_5 = 5
STREET_6 = 6
STREET_7 = 7
STREET_8 = 8
STREET_9 = 9

AVENUE_A = 11
AVENUE_B = 12
AVENUE_C = 13
AVENUE_D = 14
AVENUE_E = 15 #will have to reduce by 10 when doing math later

INDEX_DISTANCE = 0
INDEX_ROTATION = 1
INDEX_TRACKING_EDGE = 2
INDEX_FISH = 3

EDGE_LEFT = -1
EDGE_CENTER = 0
EDGE_RIGHT = 1

'''
Each step in the instructions is manually entered here
'''

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=0		#1=check fish, 0=do nothing
	match step:
		case 1:
			forward_distance=6
			turn_angle=90
			check_fish=0
			tracking_edge=1
		case 2:
			forward_distance=2.2
			turn_angle=90
			check_fish=0
			tracking_edge=1
		case 3:
			forward_distance=2.3
			turn_angle=90
			check_fish=0
			tracking_edge=1
		case 4:
			forward_distance=2.0
			turn_angle=-90
			check_fish=0
			tracking_edge=1
		case 5:
			forward_distance=0.4
			turn_angle=-90
			check_fish=0
			tracking_edge=1
		case 6:
			forward_distance=2
			turn_angle=90
			check_fish=0
			tracking_edge=1
		case 7:
			forward_distance=1.2
			turn_angle=90
			check_fish=0
			tracking_edge=1
		case 8:
			forward_distance=2
			turn_angle=-90
			check_fish=0
			tracking_edge=1
		case 9:
			forward_distance=2.3
			turn_angle=-90
			check_fish=0
			tracking_edge=1
		case 10:
			forward_distance=2.0
			turn_angle=0
			check_fish=0
			tracking_edge=0
		case 11:
			forward_distance=0
			turn_angle=0
			check_fish=0
			tracking_edge=0

	return [forward_distance, turn_angle, tracking_edge, check_fish]

'''
	function returns a set of instructions to navigate from the current point to the dock and back
	IDs are not the same as the previous function and are specific to the location of each fish
'''
def get_return_path_by_fishID(step):
	return