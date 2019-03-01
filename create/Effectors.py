#!/usr/bin/python
import os, sys
from wallaby import *

ARM_PORT = 0
ARM_BACK = 50
ARM_DOWN = 1350
ARM_UP = 600
CLAW_PORT = 1
CLAW_CLOSE = 900
CLAW_OPEN = 1820  

DEFAULT_SPEED = 50

def move_servo_slowly(port, start_pos, end_pos, step):
	if start_pos > end_pos:
		step=-step 
	for pos in range(start_pos, end_pos, step):
		set_servo_position(port, pos)
		msleep(50)
	set_servo_position(port, end_pos)

def arm_up():
	move_servo_slowly(ARM_PORT, get_servo_position(ARM_PORT), ARM_UP, DEFAULT_SPEED)

def arm_down():
	move_servo_slowly(ARM_PORT, get_servo_position(ARM_PORT), ARM_DOWN, DEFAULT_SPEED)

def arm_back():
	set_servo_position(ARM_PORT, ARM_BACK)

def claw_close():
	move_servo_slowly(CLAW_PORT, get_servo_position(CLAW_PORT), CLAW_CLOSE, DEFAULT_SPEED)

def claw_open():
	move_servo_slowly(CLAW_PORT, get_servo_position(CLAW_PORT), CLAW_OPEN, DEFAULT_SPEED)   


