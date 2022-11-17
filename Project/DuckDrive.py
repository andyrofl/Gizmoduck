#!/usr/bin/env pybricks-micropython
#imports
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
#have to import duckeyes to be able to check rotation and movement?

#CONSTANTS
BLOCKS_TO_MM = 300.2 #25.4MM * 13 INCHES *bullshitscale
MIDPOINT_LIGHT = 44.5 #midpoint of light range for IR sensor
WHEEL_DIAMETER = 44
AXLE_TRACK = 104 #5 inches end to end, 3.25 inside edges
STRAIGHT_SPEED = 200
STRAIGHT_ACCELERATION = 50
TURN_RATE = 120
TURN_ACCELERATION = 30

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

def move_forward_by_blocks(number_of_blocks, sensor_following, sensor_counting):
	#CONTINUE FORWARD UNTIL LIGHT SENSORS AGREE THAT THE CORRECT NUMBER OF BLOCKS HAVE PASSED. DATA LOG THE MOTORS MOVEMENT VALUE TO CROSS CHECK
	return

def rotate_degrees_unchecked(angle_unchecked):
	driver.turn(angle_unchecked)

def move_forward_unchecked(distance_unchecked):
	driver.straight(convert_blocks_to_MM(distance_unchecked))
