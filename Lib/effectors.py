#!/usr/bin/python
import os, sys
from wallaby import *

ARM_PORT = 0
ARM_UP = 1500
ARM_DOWN = 0
    
def move_servo_slowly(port, start_pos, end_pos, step):
	if start_pos > end_pos:
		step=-step
	for pos in range(start_pos, end_pos, step):
  		set_servo_position(port, pos)
   		msleep(50)
	set_servo_position(port, end_pos)

def arm_up():
	move_servo_slowly(ARM_PORT, ARM_DOWN, ARM_UP, 10)
        
def arm_down():
	move_servo_slowly(ARM_PORT, ARM_UP, ARM_DOWN, 10)
        
