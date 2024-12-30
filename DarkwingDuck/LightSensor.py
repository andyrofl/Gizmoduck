#! /usr/bin/env python

from machine import ADC

class LightSensor:
	minimum_reflectance = 0
	maximum_reflectance = 0


	'''
		input: the pin assignment of the port
	'''
	def __init__(self, port, min_reflectance, max_reflectance):
		self.sensor_pin = ADC(port)
		self.set_min_max_reflectance(min_reflectance, max_reflectance)


	def set_min_max_reflectance(self, minimum_reflectance, maximum_reflectance):
		self.minimum_reflectance = minimum_reflectance
		self.maximum_reflectance = maximum_reflectance
	

	'''
		input: none
		output: the reflectance value of the sensor ranging from 0 to 100
	'''
	def reflection(self):
		current_reflectance = self.sensor_pin.read_u16()
		return int((current_reflectance-self.minimum_reflectance)/self.maximum_reflectance*100)
    