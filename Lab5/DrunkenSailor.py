#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects to Build
light = LightSensor(Port.S1)
left = Motor(Port.B)
right = Motor(Port.C)
watch = StopWatch()
data = DataLog('time',  'light', 'midpoint')

# Variables
low = 55	#highest value measured
high = 34	#lowest value measured
midpoint = (high + low) / 2
timer = watch.time()

# Actions
for cycle in range(20):
	light_level = light.reflection()
	timer = watch.time()
	data.log(timer, light_level, midpoint)
	# If the reflected light is too high turn left
	while light_level > midpoint:
		eft.run(50)
		right.run(500)
		light_level = light.reflection()
	# If the reflected light is too low turn right
	while light_level < midpoint:
		left.run(500)
		right.run(50)
		light_level = light.reflection() 

left.stop()
right.stop()