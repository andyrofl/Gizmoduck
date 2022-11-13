#!/usr/bin/env pybricks-micropython
import Navigation
from Gizmoduck import Gizmoduck

#initialize for starting location of the right side dock

gizmoduck = Gizmoduck(Navigation.STREET_8, Navigation.AVENUE_D)
gizmoduck.run_expedition()