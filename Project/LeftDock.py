#!/usr/bin/env pybricks-micropython
import Navigation
from Gizmoduck import Gizmoduck

#initialize for starting location of the left side dock

gizmoduck = Gizmoduck(Navigation.STREET_8, Navigation.AVENUE_B)
gizmoduck.run_expedition()