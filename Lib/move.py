from wallaby import *

R = 1
L = 2

#Forward / backward function
def move_line(speed, ticks):
	mrp(R, speed, ticks)
	mrp(L, speed, ticks)
	bmd(R)
	bmd(L)

