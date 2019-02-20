#!/usr/bin/python
import os, sys
from wallaby import *
from effectors import *
from move_wallaby import *
from sensors import *

def right_building():
	spin_right(900, 95)
    #setting down firetruck
 	move_forward(900, 2300)
   	arm_down()
 	claw_open()
   	arm_up()
   	claw_close()
   	move_back(900, 6700)
  	for num in range(1,5):
        #get fireman
  		move_forward(900, 1550)
  		spin_left(900,900)
  		drive_to_black(900)
  		move_back(900, 200)
 		claw_open()
 		arm_down()
  		move_forward(900, 700)
		claw_close()
 		spin_right(900, 700)
 		move_forward(900, 2500)
 		claw_open()
		arm_up()
		claw_close()
 		spin_left(900, 200) 
  		move_back(900, 4500)
		spin_right(900, 250)
 		move_back(900, 1500)
	#get last fireman
	move_forward(900, 1550)
  	spin_left(900,900)
  	drive_to_black(900)
  	move_back(900, 200)
 	claw_open()
 	arm_down()
  	move_forward(900, 600)
	claw_close()
	spin_right(900, 600)
	move_forward(1500, 2500)