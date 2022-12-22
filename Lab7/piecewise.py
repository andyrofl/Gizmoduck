#piecewise function script
import math

#range -5.0 to 5.0, values are scaled by 10 for readability
for iterator in range(-50, 55, 5):
	x = iterator/10
	y=0
	if(x>= -5 and x <=0):
		y=(x**2)- 2
	elif(x<1):
		y=(2*x)-2
	elif(x<=5):
		y=math.sqrt(x-1)

	if(x >=-5 and x<0):
		print('X:', round(x,2), ' Y:', round(y,2))
	elif(x >=0 and x<=5):
		print('X: ', round(x,2), ' Y:', round(y,2))
	else:
		print('Y undefined for X value')