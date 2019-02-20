#!/usr/bin/python
import os, sys
from wallaby import *
from effectors import *
from move_wallaby import *
from sensors import *
from left_building import *
from right_building import *

LEFT = 0
RIGHT = 1
    
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

def main():
	enable_servos()
	arm_up()
	arm_back()
  	claw_open()
  	print "READY!!"
  	msleep(100) 
  	shut_down_in(119.75)
  	drive_to_black(900)
   	spin_left(900,960)	
   	drive_to_black(900)
  	drive_to_white(900)
  	move_forward(900,500)
   	drive_to_black(900)
  	move_back(900,900)
   	arm_down()
	#pick up firetruck
  	claw_firetruck()
   	arm_up()
   	spin_right(900,500)
   	drive_to_black(900)
  	back_to_white(900)
  	camera_open()
 	side = RIGHT
  	for reading in range(0,20):
		camera_update()
 		print ("X: ", get_object_center_x(0,0)," AREA: ", get_object_area(0,0))
 		if get_object_count(0) > 0:
			if get_object_area(0, 0) > 2500:
				side = LEFT
				print "LEFT IS BURNING!!!!"
	if side == LEFT:
		left_building()
 	else:
		right_building()
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
