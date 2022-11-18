#!/usr/bin/env pybricks-micropython
#IMPORT
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color
import Navigation

#initialize sensors
LIGHT_SENSOR_LEFT = LightSensor(Port.S4)
LIGHT_SENSOR_RIGHT = LightSensor(Port.S1)

'''
	this script encapsulates all the data and functions related to the sensor inputs for Gizmoduck
'''

'''
	input: integer tracking_edge correlating to a constant in Navigation
	output: the right sensor when the tracking edge is the right side, otherwise the left sensor
'''
def get_tracking_sensor(tracking_edge):
	if tracking_edge == Navigation.EDGE_RIGHT
		return LIGHT_SENSOR_RIGHT
	return LIGHT_SENSOR_LEFT

'''
	input: integer tracking_edge correlating to a constant in Navigation
	output: the left sensor when the tracking edge is the right side, otherwise the right sensor
'''
def get_counting_sensor(tracking_edge):
	if tracking_edge == Navigation.EDGE_RIGHT
		return LIGHT_SENSOR_LEFT
	return LIGHT_SENSOR_RIGHT

'''
	the function returns a boolean value of true if the target fish is legal to catch, or false if the fish is not legal
'''
def is_target_fish_legal():
	return true

def get_left_level():
	return LIGHT_SENSOR_LEFT.reflection()

def get_right_level():
	return LIGHT_SENSOR_RIGHT.reflection()