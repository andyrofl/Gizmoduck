#!/usr/bin/env pybricks-micropython
import Navigation

'''
this script contains functions and data relating the the operation of the grabbing mechanism for Gizmoduck
'''
#Tuneables
BUCKET_SPEED = 360 #Degrees/second the motor will turn at
RAISED_ANGLE = 60 #Angle at which the bucket/plow assembly is raised
LOWERED_ANGLE = 0 #Angle at which the bucket/plow assembly is lowered

#Variables
bucket = Motor(Port.C)
'''
	this function grabs a fish and returns the success of the operation
	precondition: there is not a fish currently being held
'''
def grab_fish(check_fish):
	if(check_fish=True):
		bucket.run_target(BUCKET_SPEED, RAISED_ANGLE, then=Stop.HOLD, wait=True)
		print('bucket raised')
	return

'''
	this function releases the currently held fish and returns the success of the operation
	preconditon: there is a fish currently held
'''
def release_fish(drop_fish):
	if(drop_fish=True):
		bucket.run_target(BUCKET_SPEED, LOWERED_ANGLE, then=Stop.HOLD, wait=True)
		print('bucket lowered')
	return