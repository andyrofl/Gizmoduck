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
straight_controller = TouchSensor(?))
go_right_controller = UltrasonicSensor(?)
go_left_controller = LightSensor(?)

# Variables and Constants
robot_drive.settings(?, ?, ?, ?)

# Main Code
for count in range(25):
    if straight_controller.pressed() == True:
        robot_drive.straight(-25.4) #back up an inch
    elif go_left_controller.ambient() < 35: #35 is ambient and hitting something
        robot_drive.turn(?)
    elif go_right_controller.distance() < ?:
        robot_drive.turn(?)
    else:
        wait(?)
