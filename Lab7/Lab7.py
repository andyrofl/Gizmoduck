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
straight_controller = TouchSensor(?)
go_right_controller = UltrasonicSensor(?) #ports, gotta figure out where each sensor goes first
go_left_controller = LightSensor(?)

# Variables and Constants
robot_drive.settings(?, ?, ?, ?) #speed mm/s, acceleration mm/s^2, turn rate deg/s, turn acceleration deg/s^2

# Main Code
for count in range(25):
    if straight_controller.pressed() == True: #0-1 true-false
        robot_drive.straight() #back up an inch
    elif go_left_controller.ambient() < 20: #35 is ambient and hitting something
        robot_drive.turn(?) #left like 45 degrees
    elif go_right_controller.distance() < 40: #0-175ish, 255 is either really far away or inside of it.
        robot_drive.turn(?) #right like 45
    else:
        wait(?) #how long wait
