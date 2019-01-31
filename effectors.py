#!/usr/bin/python
import os, sys
from wallaby import *

ARM_PORT = 1
ARM_UP = 460
ARM_DOWN = 1500
CLAW_PORT = 0
CLAW_CLOSE =1342
CLAW_OPEN = 257
    
    
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

def claw_close():
	move_servo_slowly(CLAW_PORT, CLAW_OPEN, CLAW_CLOSE, 10)
 
def claw_open():
	move_servo_slowly(CLAW_PORT, CLAW_CLOSE, CLAW_OPEN, 10) 
        
