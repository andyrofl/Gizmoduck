#!/usr/bin/env pybricks-micropython

# Modules to Import
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import UltrasonicSensor, TouchSensor, LightSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects to Build
left = Motor(Port.A)
right = Motor(Port.B)
robot_drive = DriveBase(left, right, 41, 102) #outisdes: 124 insides: 80 avg 102
straight_controller = TouchSensor(Port.S2)
go_right_controller = UltrasonicSensor(Port.S3) #Ultrasonic goes on the left side and indicates movement to right is needed
go_left_controller = LightSensor(Port.S1)				#Light sensor goes on the right side and indicates movement to left is needed

# Variables and Constants
robot_drive.settings(900, 200, 80, 50) #speed mm/s, acceleration mm/s^2, turn rate deg/s, turn acceleration deg/s^2

# Main Code
for count in range(50):
    if straight_controller.pressed() == True: #0-1 true-false
        robot_drive.straight(300) #go forward 10 cm
    elif go_left_controller.ambient() < 45: #35 is ambient and hitting something
        robot_drive.turn(-70) #left 45 degrees
    elif go_right_controller.distance() < 400: #0-175ish, 255 is either really far away or inside of it.
        robot_drive.turn(70) #right 45
    else:
        wait(2500) #wait 1 second
