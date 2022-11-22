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
import Navigation

#CONSTANTS
BLOCKS_TO_MM = 300.2 #25.4MM * 13 INCHES
MIDPOINT_LIGHT = 44.5 #midpoint of light range for IR sensor
WHEEL_DIAMETER = 41 #42.86
AXLE_TRACK = 115 #5 inches end to end, 3.25 inside edges
STRAIGHT_SPEED = 150
STRAIGHT_ACCELERATION = 40
TURN_RATE = 100
TURN_ACCELERATION = 25
TRACKING_OUTSIDE = True
TRACKING_INSIDE = False

#variables and objects --initialization
brick = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.B)
driver = DriveBase(left, right, WHEEL_DIAMETER, AXLE_TRACK)
driver.settings(STRAIGHT_SPEED, STRAIGHT_ACCELERATION, TURN_RATE, TURN_ACCELERATION)
current = StopWatch()
#data = DataLog('Observation','Time', 'Distance', 'Drive Speed', 'Angle', 'Turn Rate')
y_coordinate = 0
x_coordinate = 0

def convert_blocks_to_MM(blocks):
	return blocks * BLOCKS_TO_MM 
'''
	function moves robot forward a specified number of "blocks" accounting for the need to come up a little short if we are making an interior turn.
	Navigation data in each Gizmoduck loop will handle changing the tracking edge
'''
def move_forward_by_blocks(number_of_blocks, tracking_edge, angle_rotation):
	#CONTINUE FORWARD UNTIL LIGHT SENSORS AGREE THAT THE CORRECT NUMBER OF BLOCKS HAVE PASSED. DATA LOG THE MOTORS MOVEMENT VALUE TO CROSS CHECK
	tracking_sensor = DuckEyes.get_tracking_sensor(tracking_edge)
	counting_sensor = DuckEyes.get_counting_sensor(tracking_edge)
	speed = STRAIGHT_SPEED
	lines_crossed = 0
	turn_rate = 0
	outside = calculate_inside_outside(tracking_edge, angle_rotation)
	toggle_direction = False
	while lines_crossed < number_of_blocks:
		driver.drive(speed, turn_rate)
		#line counting and halting logic
		if(counting_sensor.reflection() < 30): #was 0 clear and like 90 on a line? if it sees a line increment and wait just long enough to:: LOW IS DARK
			lines_crossed+=1
			#increment_coordinates(driver.angle())
			if(lines_crossed == number_of_blocks):
				wait(300)
				driver.stop()
				return False #return false if no undershoot compensation is needed
			elif(lines_crossed == (number_of_blocks-1)):
				speed = speed/2
				if(not outside): #if the inside_outside returned false just cut the last block short and *return the function from here*
					driver.stop() #do we need to halt the drive() function to start straight()?
					driver.straight(convert_blocks_to_MM(0.5))
					driver.stop()
					return True #return true if an undershoot is needed to compensate for inside edge
			wait(100) #wait to continue loop after a sensor has been crossed to prevent it from being counted twice

		#line tracking and adjustment logic
		tracking_reflection = tracking_sensor.reflection() #should also handle a case where light level is too low?
		if(tracking_reflection < 30): #if mostly on black, continue forward. otherwise adjust turn rate incrementally based on tracking edge until mostly on black again. This may need us to reliably overshoot or undershoot rotations every time to work reliably
			turn_rate = 0
			#toggle_direction = not toggle_direction
			print('turn rate set to zero')
		else:
			if(tracking_edge == Navigation.EDGE_RIGHT):
				print('turn rate increased')
				turn_rate += 1
			else:
				print('turn rate decreased')
				turn_rate -= 2
		
			wait(30) #inherently has a 10 second delay before the first turn rate adjustment takes effect but also prevents the rate from ramping up too quickly
	print('it actually made it to this part lol')
	driver.stop()
	return
def rotate_degrees(angle_rotation, undershoot):
	if(undershoot):
		print('undershoot ', angle_rotation)
		driver.turn(angle_rotation-5)
	else:
		print('not undershoot ', angle_rotation)
		driver.turn(angle_rotation)


def rotate_degrees_unchecked(angle_unchecked):
	driver.turn(angle_unchecked)

def move_forward_unchecked(distance_unchecked):
	driver.straight(convert_blocks_to_MM(distance_unchecked))
'''
	input: tracking_edge corresponding to a constant in Navigation. right edge is positive, left is negative, and 0 goes off grid
	input: angle_rotation where a positive sign indicates a right turn and negative indicates a left turn
	if the signs of both input values are the same return that robot is on the outside of the turn, if signs are different we are tracking inside, a value of zero should be handled elsewhere
'''
def calculate_inside_outside(tracking_edge, angle_rotation):
	if(tracking_edge*angle_rotation > 0):
		return TRACKING_OUTSIDE
	elif(tracking_edge*angle_rotation < 0):
		return TRACKING_INSIDE
	else:
		return True
		print('error logged in calculate_inside_outside function, returned ')
'''
	input: angle_rotation, the absolute heading of the DriveBase object
	function modifies either the X or Y coordinate in accordance with the input angle_rotation with the assumption that robot will generally align with one of four cardinal directions
'''
def increment_coordinates(angle_rotation):
	#modulus to round, then cases to incement x or y + or - depending on cardinal direction
	variance = angle_rotation % 90
	if(variance < 50):
		angle_rotation = (angle_rotation % 360) -variance
	elif(variance > 55):
		angle_rotation = (angle_rotation % 360) +(90-variance)
	
	match angle_rotation:
		case 0:
			y_coordinate -=1
		case 90:
			x_coordinate +=1
		case 180:
			y_coordinate +=1
		case 270:
			x_coordinate -=1
		case other:
			print('coordinate increment out of bounds')

def set_x_coordinate(x_initial):
	x_coordinate = x_initial

def set_y_coordinate(y_initial):
	y_coordinate = y_initial