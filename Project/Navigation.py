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

AVENUE_A = 1
AVENUE_B = 2
AVENUE_C = 3
AVENUE_D = 4
AVENUE_E = 5



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

