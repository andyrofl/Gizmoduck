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


#Unused constants for second set of instructions
'''
FISH1 = 8
FISH2 = 13
FISH3 = 17
FISH4 = 20
FISH5 = 25
FISH6 = 29
FISH7 = 33
FISH8 = 37
FISH9 = 41
FISH10 = 45
FISH11 = 49
FISH12 = 53
'''

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=False	#A true value indicates this step will be circling a lake
	drop_fish=False		#A true value indicates that the fish should be released after moving the specified distance
	
	if (step == 1):
		tracking_edge=EDGE_RIGHT
		forward_distance=5
		turn_angle=STRAIGHT
	elif (step == 2):
		tracking_edge=EDGE_CENTER
		forward_distance=.8
		turn_angle=TURN_RIGHT
	elif (step == 3):
		tracking_edge=EDGE_CENTER
		forward_distance=.8
		turn_angle=STRAIGHT
	elif (step == 4):
		tracking_edge=EDGE_RIGHT
		forward_distance=6
		turn_angle=STRAIGHT
		check_fish=True
	elif (step == 5):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 6):
		tracking_edge=EDGE_RIGHT
		forward_distance=8
		turn_angle=ROTATE
		drop_fish=True
	elif (step == 7):
		tracking_edge=EDGE_LEFT
		forward_distance=2
		turn_angle=TURN_LEFT
	elif (step == 8):
		tracking_edge=EDGE_RIGHT
		forward_distance=8
		turn_angle=STRAIGHT
		check_fish=True
	elif (step == 9):
		tracking_edge=EDGE_RIGHT
		forward_distance=2
		turn_angle=TURN_LEFT
	elif (step == 10):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 11):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=STRAIGHT
	elif (step == 12):
		tracking_edge=EDGE_RIGHT
		forward_distance=8
		turn_angle=STRAIGHT
		check_fish=True
	elif (step == 13):
		tracking_edge=EDGE_CENTER
		forward_distance=1
		turn_angle=STRAIGHT
		drop_fish=True
	return [forward_distance, turn_angle, tracking_edge, check_fish, drop_fish]

#Original Navigation Instructions:
'''
def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid		#True=check fish, False=do nothing   0 do nothing, greater than zero go that distance to be near the fish
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
#Second set of instructions
'''
def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=False		#1=check fish, 0=do nothing
	#check fish will likely indicate whether or not we are now tracking along a lake
	if (step == 1):
		tracking_edge=EDGE_RIGHT
		forward_distance=6
		turn_angle=TURN_RIGHT
	elif (step == 2):
		tracking_edge=EDGE_RIGHT
		forward_distance=2
		turn_angle=TURN_RIGHT
	elif (step == 3):
		tracking_edge=EDGE_RIGHT
		forward_distance=2
		turn_angle=TURN_RIGHT
	elif (step == 4):
		tracking_edge=EDGE_RIGHT
		forward_distance=2
		turn_angle=TURN_LEFT
	elif (step == 5):
		tracking_edge=EDGE_LEFT
		forward_distance=2
		turn_angle=STRAIGHT
	elif (step == 6):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_LEFT
	elif (step == 7):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		turn_angle=TURN_RIGHT
	elif (step == FISH1):
		tracking_edge=EDGE_CENTER
		forward_distance=.4
		check_fish=True
		turn_angle=ROTATE
	elif (step == 9):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_RIGHT
	elif (step == 10):
		tracking_edge=EDGE_CENTER
		forward_distance=1.1
		turn_angle=TURN_RIGHT
	elif (step == 11):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=STRAIGHT
	elif (step == 12):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_RIGHT
	elif (step == FISH2):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=True
		turn_angle=ROTATE
	elif (step == 14):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_RIGHT
	elif (step == 15):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 16):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == FISH3):
		tracking_edge=EDGE_CENTER
		forward_distance=0
		check_fish=True
		turn_angle=TURN_LEFT
	elif (step == 18):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 19):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_RIGHT
	elif (step == FISH4):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		check_fish=True
		turn_angle=ROTATE
	#End of Lake 1 Instructions
	#Begin Lake 2 Instructions
	elif (step == 21):
		tracking_edge=EDGE_CENTER
		forward_distance=.5
		turn_angle=TURN_RIGHT
	elif (step == 22):
		tracking_edge=EDGE_RIGHT
		forward_distance=2
		turn_angle=TURN_RIGHT
	elif (step == 23):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 24):
		tracking_edge=EDGE_CENTER
		forward_distance=.4
		turn_angle=TURN_RIGHT
	elif (step == FISH5):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=True
		turn_angle=ROTATE
	elif (step == 26):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		turn_angle=TURN_RIGHT
	elif (step == 27):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 28):
		tracking_edge=EDGE_CENTER
		forward_distance=.6
		turn_angle=TURN_RIGHT
	elif (step == FISH6):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=True
		turn_angle=ROTATE
	elif (step == 30):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		turn_angle=TURN_RIGHT
	elif (step == 31):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 32):
		tracking_edge=EDGE_CENTER
		forward_distance=.6
		turn_angle=TURN_RIGHT
	elif (step == FISH7):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=True
		turn_angle=ROTATE
	elif (step == 34):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		turn_angle=TURN_RIGHT
	elif (step == 35):
		tracking_edge=EDGE_RIGHT
		forward_distance=1
		turn_angle=TURN_RIGHT
	elif (step == 36):
		tracking_edge=EDGE_CENTER
		forward_distance=.6
		turn_angle=TURN_RIGHT
	elif (step == FISH8):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		check_fish=True
		turn_angle=ROTATE
	elif (step == 38):
		tracking_edge=EDGE_CENTER
		forward_distance=.1
		turn_angle=TURN_LEFT
	#End of Lake 2 Instructions
	#Begin Lake 3 Instructions
	elif (step == 39):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 40):
		tracking_edge=EDGE_LEFT
		forward_distance=3
		turn_angle=TURN_LEFT
	elif (step == FISH9):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=True
		turn_angle=ROTATE
	elif (step == 42):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		turn_angle=TURN_LEFT
	elif (step == 43):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 44):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == FISH10):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=True
		turn_angle=ROTATE
	elif (step == 46):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		turn_angle=TURN_LEFT
	elif (step == 47):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 48):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == FISH11):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=True
		turn_angle=ROTATE
	elif (step == 50):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		turn_angle=TURN_LEFT
	elif (step == 51):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == 52):
		tracking_edge=EDGE_LEFT
		forward_distance=1
		turn_angle=TURN_LEFT
	elif (step == FISH12):
		tracking_edge=EDGE_CENTER
		forward_distance=.3
		check_fish=True
		turn_angle=ROTATE
	#INDEX_DISTANCE = 0, INDEX_ROTATION = 1, INDEX_TRACKING_EDGE = 2, INDEX_FISH = 3
	return [forward_distance, turn_angle, tracking_edge, check_fish]


def get_return_path_by_fishID(step, return_step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	drop_fish=False
	if (step == FISH1):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=.9
			turn_angle=TURN_LEFT
		elif (return_step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=2
			turn_angle=STRAIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			turn_angle=STRAIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 9):
			tracking_edge=EDGE_CENTER
			forward_distance=1
			turn_angle=TURN_RIGHT
		elif (return_step == 10):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=ROTATE
	elif (step == FISH2):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			turn_angle=STRAIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_LEFT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_RIGHT
		elif (return_step == 6):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=STRAIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_LEFT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			turn_angle=ROTATE
	elif (step == FISH3):
		if (return_step == 1):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=STRAIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_LEFT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=0
			drop_fish=True
			turn_angle=TURN_LEFT
		elif (return_step == 4):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			turn_angle=ROTATE
	elif (step == FISH4):			
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			turn_angle=TURN_LEFT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=STRAIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			turn_angle=STRAIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.2
			turn_angle=ROTATE
	elif (step == FISH5):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.9
			turn_angle=TURN_LEFT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			turn_angle=STRAIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=3
			turn_angle=STRAIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.9
			turn_angle=ROTATE
	elif (step == FISH6):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=TURN_RIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			turn_angle=TURN_LEFT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.6
			turn_angle=TURN_LEFT
		elif (return_step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_LEFT
			forward_distance=3
			turn_angle=STRAIGHT
		elif (return_step == 9):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=TURN_LEFT
		elif (return_step == 10):
			tracking_edge=EDGE_CENTER
			forward_distance=.6
			turn_angle=TURN_LEFT
		elif (return_step == 11):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=ROTATE
	elif (step == FISH7):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			turn_angle=TURN_LEFT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.6
			turn_angle=TURN_LEFT
		elif (return_step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			turn_angle=STRAIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_LEFT
		elif (return_step == 9):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=ROTATE
	elif (step == FISH8):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=TURN_LEFT
		elif (return_step == 2):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			turn_angle=TURN_RIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_LEFT
			forward_distance=2
			turn_angle=STRAIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_LEFT
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_RIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_RIGHT
			forward_distance=3
			turn_angle=TURN_LEFT
		elif (return_step == 8):
			tracking_edge=EDGE_RIGHT
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 9):
			tracking_edge=EDGE_CENTER
			forward_distance=.1
			turn_angle=ROTATE
	elif (step == FISH9):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=5
			turn_angle=TURN_LEFT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.6
			turn_angle=TURN_LEFT
		elif (return_step == 6):
			tracking_edge=EDGE_LEFT
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=5
			turn_angle=TURN_LEFT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=ROTATE
	elif (step == FISH10):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=TURN_RIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=6
			turn_angle=TURN_LEFT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.6
			turn_angle=TURN_LEFT
		elif (return_step == 7):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_LEFT
			forward_distance=6
			turn_angle=TURN_LEFT
		elif (return_step == 10):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			turn_angle=TURN_LEFT
		elif (return_step == 11):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=ROTATE
	elif (step == FISH11):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 2):
			tracking_edge=EDGE_LEFT
			forward_distance=5
			turn_angle=TURN_RIGHT
		elif (return_step == 3):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_LEFT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.4
			turn_angle=TURN_RIGHT
		elif (return_step == 6):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=TURN_LEFT
		elif (return_step == 7):
			tracking_edge=EDGE_RIGHT
			forward_distance=5
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=ROTATE
	elif (step == FISH12):
		if (return_step == 1):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_RIGHT
		elif (return_step == 2):
			tracking_edge=EDGE_RIGHT
			forward_distance=1
			turn_angle=TURN_LEFT
		elif (return_step == 3):
			tracking_edge=EDGE_RIGHT
			forward_distance=4
			turn_angle=STRAIGHT
		elif (return_step == 4):
			tracking_edge=EDGE_CENTER
			forward_distance=.5
			turn_angle=TURN_RIGHT
		elif (return_step == 5):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			drop_fish=True
			turn_angle=ROTATE
		elif (return_step == 6):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=TURN_LEFT
		elif (return_step == 7):
			tracking_edge=EDGE_LEFT
			forward_distance=5
			turn_angle=TURN_RIGHT
		elif (return_step == 8):
			tracking_edge=EDGE_LEFT
			forward_distance=1
			turn_angle=TURN_LEFT
		elif (return_step == 9):
			tracking_edge=EDGE_CENTER
			forward_distance=.3
			turn_angle=ROTATE

	return [forward_distance, turn_angle, tracking_edge, drop_fish]
'''