#!/usr/bin/python
import os, sys
from wallaby import *
from move_wallaby import *

LEFT_LINE = 0
THRESH = 1650
    
def drive_to_black(speed):
	mav(R, speed)
  	mav(L, speed)
  	while analog(LEFT_LINE) < THRESH:
		pass
  	ao()
            
def drive_to_white(speed):
	mav(R, speed)
  	mav(L, speed)
  	while analog(LEFT_LINE) > THRESH:
		pass
  	ao()
            
def back_to_white(speed):
	mav(R, -speed)
  	mav(L, -speed)
  	while analog(LEFT_LINE) > THRESH:
		pass
  	ao()
            
def back_to_black(speed):
	mav(R, -speed)
  	mav(L, -speed)
  	while analog(LEFT_LINE) < THRESH:
		pass
  	ao()         