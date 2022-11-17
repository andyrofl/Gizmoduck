#!/usr/bin/env pybricks-micropython
#imports
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
#have to import duckeyes to be anble to check rotation and movement?

#CONSTANTS
BLOCKS_TO_MM = 300.2 #25.4MM * 13 INCHES *bullshitscale
MIDPOINT_LIGHT = 44.5 #midpoint of light range for IR sensor

#variables and objects --initialization
brick = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.B)
driver = DriveBase(left, right, 22, 100)
current = StopWatch()
data = DataLog('Observation','Time', 'Distance', 'Drive Speed', 'Angle', 'Turn Rate')
driver.settings(200, 70, 800, 800)

def convert_blocks_to_MM(blocks):
	return blocks * BLOCKS_TO_MM 

def move_forward_by_blocks(number_of_blocks):
	#CONTINUE FORWARD UNTIL LIGHT SENSORS AGREE THAT THE CORRECT NUMBER OF BLOCKS HAVE PASSED. DATA LOG THE MOTORS MOVEMENT VALUE TO CROSS CHECK
	return
'''
def rotate_by_degrees(degrees_to_rotate):
	for cycle in range(20):
	light_level = light.reflection()
	timer = watch.time()
	data.log(timer, light_level, midpoint)
	# If the reflected light level is in the acceptable range continue forward
	while light_level >= (midpoint-3) and lightlevel =< (midpoint+3):
		left.run(500)
		right.run(500)
		light_level = light.reflection()
	# If the reflected light is too high turn left 
	while light_level > (midpoint+3):
		eft.run(50)
		right.run(300)
		light_level = light.reflection()
	# If the reflected light is too low turn right
	while light_level < (midpoint-3):
		left.run(300)
		right.run(50)
		light_level = light.reflection() 
'''
def rotate_degrees_unchecked(angle_unchecked):
	driver.turn(angle_unchecked)

def move_forward_unchecked(distance_unchecked):
	driver.straight(convert_blocks_to_MM(distance_unchecked))

'''
upon reaching a target and turning the degree value specified by the instruction, should move forward based on input from the distance sensor to prepare to catch the fish,
		storing the distance and/or rotation values to allow us to backtrack to a known area and continue on with main task.
'''