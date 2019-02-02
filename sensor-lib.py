#!/usr/bin/python
import os, sys
from wallaby import *
from move_wallaby import *

def center_color(channel):
	camera_open_black();
	camera_update();
	x = get_object_center_x(channel, 0);
	while x < 60 or x > 100:
		camera_update();
		x = get_object_center_x(channel, 0);
		if x < 60:
			spin_right(100, 100);
		elif x > 100:
			spin_left(100, 100);
	ao();

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
