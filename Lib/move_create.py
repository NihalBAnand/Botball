#!/usr/bin/python
import os, sys
from wallaby import *

def forward(speed, dist):
	set_create_distance(0)
	create_drive_direct(speed, speed)
  	while get_create_distance() < dist:
		pass
 	create_drive_direct(0,0)

def backward(speed, dist):
	set_create_distance(0)
	create_drive_direct(-speed, -speed)
  	while get_create_distance() > -dist:
		pass
 	create_drive_direct(0,0)
         
 	
def spin_CCW(speed, angle):
	set_create_total_angle(0)
	create_spin_CCW(speed)
	while get_create_total_angle() < angle:
		pass
	create_drive_direct(0,0)
	
def spin_CW(speed, angle):
	set_create_total_angle(0)
	create_spin_CW(speed)
	while get_create_total_angle() > -angle:
		pass
	create_drive_direct(0,0)
            
def drive_to_bump(speed):
	create_drive_direct(speed,speed)
	while get_create_lbump() == 0 and get_create_rbump()==0:
		pass
	create_drive_direct(0,0)
