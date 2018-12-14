# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
	d=b*b-4*a*c
	if(d<0):
		return
	elif(d>0):
		return  ((-b)+math.sqrt(d))/(2*a),((-b)-math.sqrt(d))/(2*a)
	else:
		return ((-b)+math.sqrt(d))/(2*a)
print(quadratic(2,3,1))
print(quadratic(1,2,3))
print(quadratic(3,2,1))
print(quadratic(4,4,1))