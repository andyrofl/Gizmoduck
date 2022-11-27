#!/usr/bin/env pybricks-micropython
#IMPORT
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color
import Navigation

#initialize sensors
LIGHT_SENSOR_LEFT = LightSensor(Port.S4)
LIGHT_SENSOR_RIGHT = LightSensor(Port.S1)

global IR_left_midpoint
global IR_right_midpoint


'''
	input: a min and max light level for the left and right sensor
	both midpoints have been initialized
'''
def initialize_IR_levels(left_min, left_max, right_min, right_max):
	global IR_left_midpoint
	global IR_right_midpoint
	IR_left_midpoint = (left_min + left_max) /2
	IR_right_midpoint = (right_min + right_max) /2

'''
	input: integer tracking_edge correlating to a constant in Navigation
	output: the right sensor when the tracking edge is the right side, otherwise the left sensor
'''
def get_tracking_sensor(tracking_edge):
	if tracking_edge == Navigation.EDGE_RIGHT:
		return LIGHT_SENSOR_RIGHT
	return LIGHT_SENSOR_LEFT

'''
	input: integer tracking_edge correlating to a constant in Navigation
	output: the left sensor when the tracking edge is the right side, otherwise the right sensor
'''
def get_counting_sensor(tracking_edge):
	if tracking_edge == Navigation.EDGE_RIGHT:
		return LIGHT_SENSOR_LEFT
	return LIGHT_SENSOR_RIGHT

'''
	the function returns a boolean value of true if the target fish is legal to catch, or false if the fish is not legal
'''
def is_target_fish_legal():
	return True

'''
	returns an integer representing the light level of the LEFT IR sensor
'''
def get_left_level():
	return LIGHT_SENSOR_LEFT.reflection()

'''
	returns an integer representing the light level of the RIGHT IR sensor
'''
def get_right_level():
	return LIGHT_SENSOR_RIGHT.reflection()

'''
	input: a LightSensor light_sensor
	return the value of the IR level midpoint for the sensor corresponding to the pointer passed to function
'''
def get_IR_midpoint(light_sensor):
	if light_sensor == LIGHT_SENSOR_LEFT:
		return IR_left_midpoint
	elif light_sensor == LIGHT_SENSOR_RIGHT:
		return IR_right_midpoint
	else:
		print('error logged in DuckEyes: midpoint calculation')
		return 40

'''
	input: a LightSensor corresponding to the edge currently tracking the line
	input: a rotation angle to do at the end of the current operation where positive turns right and negative turns left
	the function returns True when the current tracking sensor will become the counting sensor during the next operation
'''
def is_sensor_swapped(tracking_sensor, angle_rotation):
	if(tracking_sensor == LIGHT_SENSOR_LEFT and angle_rotation <0):
		return True
	elif(tracking_sensor == LIGHT_SENSOR_RIGHT and angle_rotation >0):
		return True
	else:
		return False