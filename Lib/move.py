from wallaby import *

R = 1
L = 2

#Forward / backward function
def move_line(speed, ticks):
	mrp(R, speed, ticks)
	mrp(L, speed, ticks)
	bmd(R)
	bmd(L)

def spin_right(speed, ticks):
	mrp(L, speed, ticks)
	bmd(L)

def spin_left(speed, ticks):
	mrp(R, speed, ticks)
	bmd(R)

