#!/usr/bin/env pybricks-micropython

#CONSTANTS
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
#The instructions in each step have been reordered, and are meant to be carried out in the order listed

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=0		#1=check fish, 0=do nothing
	
	if (step == 1):
		tracking_edge=EDGE_RIGHT
		forward_distance=.7
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 2):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=1
		turn_angle=ROTATE
	elif (step == 3):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 4):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 5):
		tracking_edge=EDGE_CENTER
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 6):
		tracking_edge=EDGE_CENTER
		forward_distance=.2
		check_fish=1
		turn_angle=ROTATE
	elif (step == 7):
		tracking_edge=EDGE_CENTER
		forward_distance=.2
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 8):
		tracking_edge=EDGE_CENTER
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 9):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 10):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=1
		turn_angle=ROTATE
	elif (step == 11):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 12):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 13):
		tracking_edge=EDGE_CENTER
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 14):
		tracking_edge=EDGE_CENTER
		forward_distance=.2
		check_fish=1
		turn_angle=ROTATE
	elif (step == 15):
		tracking_edge=EDGE_CENTER
		forward_distance=.2
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 16):
		tracking_edge=EDGE_CENTER
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_RIGHT
	#End of Lake 1 Instructions
	#Begin Lake 2 Instructions
	elif (step == 17):
		tracking_edge=EDGE_RIGHT
		forward_distance=2.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 18):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 19):
		tracking_edge=EDGE_RIGHT
		forward_distance=.4
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 20):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=1
		turn_angle=ROTATE
	elif (step == 21):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 22):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 23):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 24):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=1
		turn_angle=ROTATE
	elif (step == 25):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 26):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 27):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 28):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=1
		turn_angle=ROTATE
	elif (step == 29):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 30):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 31):
		tracking_edge=EDGE_RIGHT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_RIGHT
	elif (step == 32):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=1
		turn_angle=ROTATE
	elif (step == 33):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=0
		turn_angle=TURN_LEFT
	#End of Lake 2 Instructions
	#Begin Lake 3 Instructions
	elif (step == 34):
		tracking_edge=EDGE_LEFT
		forward_distance=.6
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 35):
		tracking_edge=EDGE_LEFT
		forward_distance=3.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 36):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=1
		turn_angle=ROTATE
	elif (step == 37):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 38):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 39):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 40):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=1
		turn_angle=ROTATE
	elif (step == 41):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 42):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 43):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 44):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=1
		turn_angle=ROTATE
	elif (step == 45):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 46):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 47):
		tracking_edge=EDGE_LEFT
		forward_distance=1.1
		check_fish=0
		turn_angle=TURN_LEFT
	elif (step == 48):
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
	if (fishID == 1):			
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 5):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 2):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=.9
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=2
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 3):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 5):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 4):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=1.2
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=1.2
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 5):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 5):
			tracking_edge=EDGE_LEFT
			forward_distance=3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=1
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 6):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=.6
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 4):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_LEFT
			forward_distance=3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 9):
			tracking_edge=EDGE_LEFT
			forward_distance=.6
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 10):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 7):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=2.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=2.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 8):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 6):
			tracking_edge=EDGE_RIGHT
			forward_distance=2
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 9):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=4.9
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=4.9
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 10):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1.1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=6
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 4):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_LEFT
			forward_distance=6
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 9):
			tracking_edge=EDGE_LEFT
			forward_distance=1.1
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 10):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 11):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 2):
			tracking_edge=EDGE_LEFT
			forward_distance=4.9
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 3):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 6):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 7):
			tracking_edge=EDGE_RIGHT
			forward_distance=4.9
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE
	elif (fishID == 12):
		if (step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=.9
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=4.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=1
			turn_angle=ROTATE
		elif (step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=TURN_LEFT
		elif (step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=4.4
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=1
			drop_fish=0
			turn_angle=TURN_RIGHT
		elif (step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=0
			turn_angle=ROTATE

	return [forward_distance, turn_angle, tracking_edge, drop_fish]