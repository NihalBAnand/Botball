from wallaby import *

R = 0
L = 3

#Forward / backward function
def move_forward(speed, ticks):
	cmpc(R)
  	cmpc(L)
	mav(L, speed)
  	mav(R, speed)
 	while gmpc(R)< ticks:
		pass
	ao()
def move_back(speed, ticks):
	cmpc(R)
  	cmpc(L)
	mav(L, -speed)
  	mav(R, -speed)
 	while gmpc(R)> -ticks:
		pass
	ao()

def spin_right(speed, ticks):
	cmpc(R)
	cmpc(L)
	mav(L, speed)
	mav(R, -speed)
	while gmpc(L)< ticks:
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

