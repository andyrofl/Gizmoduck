#! /usr/bin/env python

from machine import PWM, Pin
import time

class DriveBase:
	#motor_pin_left = PWM(Pin(15))
	#motor_pin_right = PWM(Pin(7))
	#direction_pin_left = Pin()
	#direction_pin_right = Pin()
	SPEED = 0
	TURN_RATE = 0
	distance_travelled = 0

	#magic numbers
	ANGLE_MULTIPLIER = 0.3 
	STRAIGHT_MULTIPLIER = 0.05
	SPEED_TO_DUTY_MULTIPIER = 0.5

	#intitialize object
	def __init__(self, motor_pin_left, motor_pin_right, wheel_diameter, axle_track):
		self.motor_pin_left = PWM(Pin(motor_pin_left, Pin.OUT), freq=1000)
		self.motor_pin_right = PWM(Pin(motor_pin_right, Pin.OUT), freq=1000)
		self.direction_pin_left = Pin(8, Pin.OUT)
		self.direction_pin_left.value(1)
		self.direction_pin_right = Pin(14, Pin.OUT)
		self.direction_pin_right.value(1)
		self.mode_pin = Pin(10, Pin.OUT)
		self.mode_pin.value(1)

	#define speed and turn rate
	def settings(self, straight_speed, turn_rate):
		self.SPEED = straight_speed*self.SPEED_TO_DUTY_MULTIPIER
		self.TURN_RATE = turn_rate

	#drive at the input speed with the turn_rate input
	#drive should only take a positive speed, a negative value will be converted to positive
	def drive(self, speed, turn_rate):
		if(speed < 0):
			speed = -speed
		#if turn rate is positive we want to turn towards the right, so the left motor should move faster than the right motor, if it is negative we want the opposite to be true
		#may need to cap turn rate
		pwm_left = int((speed +turn_rate)*630) #655
		pwm_right = int((speed -turn_rate)*630)

		#print('current pwm values: left', pwm_left, ' and right ', pwm_right)

		#keep both pwm values between 0 and 100, check if the range is 0-255
		#if(pwm_left >65535):
		#	pwm_left = 65535
		#elif(pwm_left < 0):
		#	pwm_left = 0

		#if(pwm_right >65535):
		#	pwm_right = 65535
		#elif(pwm_right < 0):
		#	pwm_right = 0
		
		#set both pins to the calculated duty cycle
		self.motor_pin_left.duty_u16(pwm_left)
		self.motor_pin_right.duty_u16(pwm_right)
		print('motor left current duty cycle:', self.motor_pin_left.duty_u16(), 'right duty cycle', self.motor_pin_right.duty_u16())
		#time.sleep(1)
		#use turn rate to determine relative set speed for left and right motors
		#set the output to both pins based on this calculation
		return
	
	#return the distance travelled since the DriveBase was last stopped
	def distance(self):
		return self.distance_travelled

	#stop motors and reset distance
	def stop(self):
		self.motor_pin_left.duty_u16(0)
		self.motor_pin_left.duty_u16(0)
		self.distance_travelled = 0
		return

	#drive the specified distance straight
	def straight(self, distance):
		if(distance > 0):
			self.direction_pin_left.value(1)
			self.direction_pin_right.value(1)
		elif(distance < 0):
			self.direction_pin_left.value(0)
			self.direction_pin_right.value(0)
			
		time_to_move = distance * self.STRAIGHT_MULTIPLIER
		#set both motors to move forward at a power level proportional to the set speed for a distance equivalent to the specified distance
		self.motor_pin_left.duty_u16(self.SPEED)
		self.motor_pin_left.duty_u16(self.SPEED)
		time.sleep(time_to_move)
		self.stop()
		return
	
	#takes an input parameter of degrees to turn and runs the left and right motors for a short time to approximately rotate that distance
	def turn(self, angle):
		time_to_rotate = angle * self.ANGLE_MULTIPLIER

		if(angle > 0):
			self.direction_pin_left.value(1)
			self.direction_pin_right.value(0)
		elif(angle < 0):
			self.direction_pin_left.value(1)
			self.direction_pin_right.value(0)
		#if angle is positive, set left to drive forward and right to drive backwards, otherwise set the other way
		#time.sleep for angle time a magic number that runs for about the right amount of time per degree desired
		time.sleep(time_to_rotate)
		return