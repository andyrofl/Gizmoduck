#!/usr/bin/env pybricks-micropython
#define paths to each fish

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
INDEX_FISH = 2

'''
Each step in the instructions is manually entered here
The number of steps +1 must be manually entered after 'while step<'
'''

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	check_fish=0		#1=check fish, 0=do nothing
	if step==1:
		forward_distance=6
		turn_angle=90
		check_fish=0
	elif step==2:
		forward_distance=2
		turn_angle=90
		check_fish=0
	elif step==3:
		forward_distance=6
		turn_angle=0
		check_fish=0
	
	return [forward_distance, turn_angle, check_fish]

'''
given the current line and next line, returns the angle needed to turn from current line to the next on the ultimate direction of the destination.
precondition: logically, current and next lines should intersect.
'''
def get_angle_between_lines(line_current, line_next, line_overnext):
	return 0 #degrees (positive or negative) needed to turn from current line to next line with heading of the one after it
