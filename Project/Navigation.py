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

TURN_RIGHT = 90
TURN_LEFT = -90
STRAIGHT = 0
ROTATE = 180

'''
Original Navigation Instructions:

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
			tracking_edge=EDGE_RIGHT
		case 2:
			forward_distance=2.2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 3:
			forward_distance=2.3
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 4:
			forward_distance=2.0
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 5:
			forward_distance=0.4
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 6:
			forward_distance=2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 7:
			forward_distance=1.2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 8:
			forward_distance=2
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 9:
			forward_distance=2.3
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 10:
			forward_distance=2.0
			turn_angle=0
			check_fish=0
			tracking_edge=EDGE_CENTER
		case 11:
			forward_distance=0
			turn_angle=0
			check_fish=0
			tracking_edge=EDGE_CENTER

	return [forward_distance, turn_angle, tracking_edge, check_fish]
'''
#The instructions in each step have been reordered, and are meant to be carried out in the order listed

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=0		#1=check fish, 0=do nothing
	match step:
		case 1:
			tracking_edge=EDGE_RIGHT
			forward_distance=.7
			check_fish=0
			turn_angle=TURN_RIGHT
		case 2:
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			check_fish=1
			turn_angle=ROTATE
		case 3:
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			check_fish=0
			turn_angle=TURN_RIGHT
		case 4:
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 5:
			tracking_edge=EDGE_CENTER
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 6:
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			check_fish=1
			turn_angle=ROTATE
		case 7:
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			check_fish=0
			turn_angle=TURN_RIGHT
		case 8:
			tracking_edge=EDGE_CENTER
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 9:
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 10:
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			check_fish=1
			turn_angle=ROTATE
		case 11:
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			check_fish=0
			turn_angle=TURN_RIGHT
		case 12:
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 13:
			tracking_edge=EDGE_CENTER
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 14:
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			check_fish=1
			turn_angle=ROTATE
		case 15:
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			check_fish=0
			turn_angle=TURN_RIGHT
		case 16:
			tracking_edge=EDGE_CENTER
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_RIGHT
		#End of Lake 1 Instructions
		#Begin Lake 2 Instructions
		case 17:
			tracking_edge=EDGE_RIGHT
			forward_distance=2.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 18:
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 19:
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			check_fish=0
			turn_angle=TURN_RIGHT
		case 20:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=1
			turn_angle=ROTATE
		case 21:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 22:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 23:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 24:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=1
			turn_angle=ROTATE
		case 25:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 26:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 27:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 28:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=1
			turn_angle=ROTATE
		case 29:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=0
			turn_angle=TURN_RIGHT
		case 30:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 31:
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_RIGHT
		case 32:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=1
			turn_angle=ROTATE
		case 33:
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			check_fish=0
			turn_angle=TURN_LEFT
		#End of Lake 2 Instructions
		#Begin Lake 3 Instructions
		case 34:
			tracking_edge=EDGE_LEFT
			forward_distance=.6
			check_fish=0
			turn_angle=TURN_LEFT
		case 35:
			tracking_edge=EDGE_LEFT
			forward_distance=3.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 36:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=1
			turn_angle=ROTATE
		case 37:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=0
			turn_angle=TURN_LEFT
		case 38:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 39:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 40:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=1
			turn_angle=ROTATE
		case 41:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=0
			turn_angle=TURN_LEFT
		case 42:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 43:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 44:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=1
			turn_angle=ROTATE
		case 45:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=0
			turn_angle=TURN_LEFT
		case 46:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 47:
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			check_fish=0
			turn_angle=TURN_LEFT
		case 48:
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			check_fish=1
			turn_angle=ROTATE
	return [tracking_edge, forward_distance, check_fish, turn_angle]


'''
	function returns a set of instructions to navigate from the current point to the dock and back
	IDs are not the same as the previous function and are specific to the location of each fish
'''
def get_return_path_by_fishID(fishID, step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	drop_fish=0
	match fishID:
		case 1:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.2
					drop_fish=0
					turn_angle=TURN_LEFT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 5:
					tracking_edge=EDGE_LEFT
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 6:
					tracking_edge=EDGE_CENTER
					forward_distance=.2
					drop_fish=0
					turn_angle=ROTATE
		case 2:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 2:
					tracking_edge=EDGE_CENTER
					forward_distance=.9
					drop_fish=0
					turn_angle=TURN_LEFT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=2
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 6:
					tracking_edge=EDGE_LEFT
					forward_distance=2
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 7:
					tracking_edge=EDGE_CENTER
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE
		case 3:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.2
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_LEFT
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_LEFT
				case 3:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 5:
					tracking_edge=EDGE_RIGHT
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_LEFT
				case 6:
					tracking_edge=EDGE_CENTER
					forward_distance=.2
					drop_fish=0
					turn_angle=ROTATE
		case 4:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_CENTER
					forward_distance=1.2
					drop_fish=1
					turn_angle=ROTATE
				case 3:
					tracking_edge=EDGE_CENTER
					forward_distance=1.2
					drop_fish=0
					turn_angle=TURN_LEFT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE
		case 5:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_LEFT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 5:
					tracking_edge=EDGE_LEFT
					forward_distance=3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 6:
					tracking_edge=EDGE_CENTER
					forward_distance=1
					drop_fish=0
					turn_angle=ROTATE
		case 6:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=.6
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 4:
					tracking_edge=EDGE_RIGHT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=1
					turn_angle=ROTATE
				case 6:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 7:
					tracking_edge=EDGE_LEFT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_LEFT
					forward_distance=3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 9:
					tracking_edge=EDGE_LEFT
					forward_distance=.6
					drop_fish=0
					turn_angle=TURN_LEFT
				case 10:
					tracking_edge=EDGE_CENTER
					forward_distance=.1
					drop_fish=0
					turn_angle=ROTATE
		case 7:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=2.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 6:
					tracking_edge=EDGE_LEFT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 7:
					tracking_edge=EDGE_LEFT
					forward_distance=2.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.1
					drop_fish=0
					turn_angle=ROTATE
		case 8:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.5
					drop_fish=0
					turn_angle=TURN_LEFT
				case 2:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_LEFT
					forward_distance=2
					drop_fish=0
					turn_angle=TURN_LEFT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 6:
					tracking_edge=EDGE_RIGHT
					forward_distance=2
					drop_fish=0
					turn_angle=TURN_LEFT
				case 7:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.5
					drop_fish=0
					turn_angle=ROTATE
		case 9:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=4.9
					drop_fish=0
					turn_angle=TURN_LEFT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 6:
					tracking_edge=EDGE_LEFT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 7:
					tracking_edge=EDGE_LEFT
					forward_distance=4.9
					drop_fish=0
					turn_angle=TURN_LEFT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE
		case 10:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_RIGHT
					forward_distance=1.1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=6
					drop_fish=0
					turn_angle=TURN_LEFT
				case 4:
					tracking_edge=EDGE_RIGHT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=1
					turn_angle=ROTATE
				case 6:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 7:
					tracking_edge=EDGE_LEFT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_LEFT
					forward_distance=6
					drop_fish=0
					turn_angle=TURN_LEFT
				case 9:
					tracking_edge=EDGE_LEFT
					forward_distance=1.1
					drop_fish=0
					turn_angle=TURN_LEFT
				case 10:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE
		case 11:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 2:
					tracking_edge=EDGE_LEFT
					forward_distance=4.9
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 3:
					tracking_edge=EDGE_LEFT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 6:
					tracking_edge=EDGE_RIGHT
					forward_distance=.4
					drop_fish=0
					turn_angle=TURN_LEFT
				case 7:
					tracking_edge=EDGE_RIGHT
					forward_distance=4.9
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE
		case 12:
			match step:
				case 1:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 2:
					tracking_edge=EDGE_CENTER
					forward_distance=.9
					drop_fish=0
					turn_angle=TURN_LEFT
				case 3:
					tracking_edge=EDGE_RIGHT
					forward_distance=4.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 4:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=1
					turn_angle=ROTATE
				case 5:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=TURN_LEFT
				case 6:
					tracking_edge=EDGE_LEFT
					forward_distance=4.4
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 7:
					tracking_edge=EDGE_CENTER
					forward_distance=1
					drop_fish=0
					turn_angle=TURN_RIGHT
				case 8:
					tracking_edge=EDGE_CENTER
					forward_distance=.3
					drop_fish=0
					turn_angle=ROTATE

	return [forward_distance, turn_angle, tracking_edge, drop_fish]