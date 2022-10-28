#!/usr/bin/env pybricks-micropython

# Modules to Import
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects to Build
tester = Motor(Port.A)
current = StopWatch()
data = DataLog('Section','Time', 'Angle')

# Actions
for speed in range(100, 1100, 100):
    tester.run_time(speed, 2000, then=Stop.HOLD, wait=True)
    data.log('A', current.time(), tester.angle())
    wait(300)

tester.run_target(600, 0, then=Stop.HOLD, wait=True)

for angle in range(90, 370, 90):
    tester.run_angle(400, angle, then=Stop.HOLD, wait=True)
    data.log('B', current.time(), tester.angle())
    wait(300)
    tester.run_target(400, angle, then=Stop.HOLD, wait=True)
    wait(1000)
    data.log('C', current.time(), tester.angle())

for angle in range(90, 370, 90):
    tester.reset_angle(0)
    tester.run_angle(400, angle, then=Stop.HOLD, wait=True)
    data.log('D', current.time(), tester.angle())
    wait(300)
    tester.run_target(400, angle, then=Stop.HOLD, wait=True)
    data.log('E', current.time(), tester.angle())
    wait(1000)
