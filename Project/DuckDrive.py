#!/usr/bin/env pybricks-micropython
#imports
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port
import DuckEyes

#CONSTANTS
BLOCKS_TO_MM = 300.2 #25.4MM * 13 INCHES
MIDPOINT_LIGHT = 44.5 #midpoint of light range for IR sensor
WHEEL_DIAMETER = 41 #42.86
AXLE_TRACK = 106 #5 inches end to end, 3.25 inside edges
STRAIGHT_SPEED = 150
STRAIGHT_ACCELERATION = 40
TURN_RATE = 100
TURN_ACCELERATION = 25

#variables and objects --initialization
brick = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.B)
driver = DriveBase(left, right, WHEEL_DIAMETER, AXLE_TRACK)
driver.settings(STRAIGHT_SPEED, STRAIGHT_ACCELERATION, TURN_RATE, TURN_ACCELERATION)
current = StopWatch()
#data = DataLog('Observation','Time', 'Distance', 'Drive Speed', 'Angle', 'Turn Rate')

def convert_blocks_to_MM(blocks):
	return blocks * BLOCKS_TO_MM 
'''
	function moves robot forward a specified number of "blocks" accounting for 
'''
def move_forward_by_blocks(number_of_blocks, tracking_edge):
	#CONTINUE FORWARD UNTIL LIGHT SENSORS AGREE THAT THE CORRECT NUMBER OF BLOCKS HAVE PASSED. DATA LOG THE MOTORS MOVEMENT VALUE TO CROSS CHECK
	return

def rotate_degrees_unchecked(angle_unchecked):
	driver.turn(angle_unchecked)

def move_forward_unchecked(distance_unchecked):
	driver.straight(convert_blocks_to_MM(distance_unchecked))
