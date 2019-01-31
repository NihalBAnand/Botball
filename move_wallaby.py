from wallaby import *

R = 1
L = 2

#Forward / backward function
def move_line(speed, ticks):
	cmpc(R)
  	cmpc(L)
	mav(L, speed)
  	mav(R, speed)
 	while gmpc(R)< ticks:
		pass
	ao()

def spin_right(speed, ticks):
	cmpc(R)
	cmpc(L)
	mav(L, speed)
	mav(R, -speed)
	while gmpc(R)< ticks:
		pass
	ao()

def spin_left(speed, ticks):
	cmpc(R)
	cmpc(L)
	mav(L, -speed)
	mav(R, speed)
	while gmpc(R)< ticks:
		pass
	ao()

