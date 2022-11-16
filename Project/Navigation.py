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



'''
returns a matrix of [line][length] of indeterminate depth
'''
def get_path_by_ID(path_id):
	return #matrix of [line][length]

'''
given the current line and next line, returns the angle needed to turn from current line to the next on the ultimate direction of the destination.
precondition: logically, current and next lines should intersect.
'''
def get_angle_between_lines(line_current, line_next, line_overnext):
	return 0 #degrees (positive or negative) needed to turn from current line to next line with heading of the one after it

'''
Variables are defined here
'''
step=1
#keeps track of the step of the instructions that we are on

forward_distance=0
#number of blocks to move forward

turn_angle=0
#Degrees to turn from the direction robot is facing (0 is forward)

check_fish=0
#1=check fish, 0=do nothing

#Each step in the instructions is manually entered here
while step>0:
	if step=1:
		forward_distance=6
		turn_angle=-90
		check_fish=0
		step=+1
	elif step=2:
		forward_distance=2
		turn_angle=-90
		check_fish=0
		step=+1
	elif step=3:
		forward_distance=6
		turn_angle=0
		check_fish=0
		step=+1
	else step=0
	#something here to run driving functions with the three variables (all except step) and then return for the next step
	