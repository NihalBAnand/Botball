#!/usr/bin/python
import os, sys
from wallaby import *
from MoveLib import *
THRESH = 3500
sensor_port = 0

def analog_average(port, reads):
	total = 0;
	for reading in range(reads):
		total += analog(port);
	return total / reads;
def analog_median(port, reads):
	data = []
	for read in range(reads):
		data.append(analog(port))
	data = sorted(data)
	return data[round(len(data)/2)]
    
def drive_to_black(speed):
	set_create_distance(0)
	create_drive_direct(-speed, -speed)
  	while analog(sensor_port) < THRESH:
		pass
	create_drive_direct(0,0)
            
def drive_to_white(speed):
	set_create_distance(0)
	create_drive_direct(-speed, -speed)
  	while analog(LEFT_LINE) > THRESH:
		pass
	create_drive_direct(0,0)
            
def back_to_white(speed):
	set_create_distance(0)
	create_drive_direct(speed, speed)
  	while analog(LEFT_LINE) > THRESH:
		pass
	create_drive_direct(0,0)
            
def back_to_black(speed):
	set_create_distance(0)
	create_drive_direct(speed, speed)
  	while analog(sensor_port) < THRESH:
		pass
	create_drive_direct(0,0)
            
            
def drive_to_touch(port, speed):
	create_drive_direct(-speed, -speed)
  	while digital(port) == 0:
		pass
	create_drive_direct(0,0)
            
