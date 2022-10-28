#!/usr/bin/env pybricks-micropython

# Modules to Import
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Objects to Build
brick = EV3Brick()
left = Motor(Port.A)
right = Motor(Port.B)
driver = DriveBase(left, right, 100, 22) # You must set this to your robots needs
current = StopWatch()
data = DataLog('Observation','Time', 'Distance', 'Drive Speed', 'Angle', 'Turn Rate')
# Variables initialized
driver.settings(800, 200, 30, 1200)

# Actions
# Action A
driver.straight(750)
data.log('A', current.time(), driver.state())
wait(2000)

brick.speaker.beep(frequency=400, duration=100)
wait(1500)

# Action B
driver.turn(180)
data.log('B', current.time(), driver.state())

brick.speaker.beep(frequency=500, duration=100)
wait(1500)

# Action C
driver.drive(1200, 20)
wait(3000)
driver.stop()
data.log('C', current.time(), driver.state())

brick.speaker.beep(frequency=700, duration=100)
driver.reset()
wait(1500)
current.reset()

# Action D
driver.reset()
for i in range(1,10):
    driver.drive(i*70, 0)
    wait(1500)
    data.log(i, current.time(), driver.state())
brick.speaker.beep(frequency=800, duration=100)
