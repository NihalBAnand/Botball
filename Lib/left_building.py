#!/usr/bin/python
import os, sys
from wallaby import *
from effectors import *
from move_wallaby import *
from sensors import *

def left_building():
	#drop off firetruck   
 	arm_down()
 	claw_open()
  	#go to fire-man #1
  	arm_up()
  	move_back(900, 1990)
  	spin_right(900, 300)
	move_back(900, 2000)
	move_forward(900, 1650)
	spin_left(900,900)
   	drive_to_black(900)
	back_to_white(900)
  	arm_down()
 	move_forward(900, 400)
	#pick up fire-man
   	claw_close()
   	spin_right(500,400)
   	arm_up()
	#drop fire-man #1 on medical thing	
   	drive_to_black(900)
   	move_forward(900, 95)
  	claw_open()  
  	# FIREMAN # 1 SCORED
	move_back(900,2700)
	spin_right(900,350)
	move_back(900,1000)
        
 	#GO GET FIREMAN #2
	move_forward(900, 1650)
	spin_left(900,900)
   	drive_to_black(900)
	back_to_white(900)
  	arm_down()
 	move_forward(900, 575)
	#pick up fire-man
   	claw_close()
   	spin_right(500,400)
	claw_open()
   	arm_up()
 	#GO GET FIREMAN #3
   	move_back(900,2700)
	spin_right(900,300)
	move_back(900,1000) #hit pipe
        

	move_forward(900, 1650)
	spin_left(900,900)
   	drive_to_black(900)
	back_to_white(900)
  	arm_down()
 	move_forward(900, 575)
	#pick up fire-man
   	claw_close()
   	spin_right(500,400)
	claw_open()
   	arm_up()
  	#GO GET FIREMAN #4
   	move_back(900,2700)
	spin_right(900,300)
	move_back(900,1000)
  

	move_forward(900, 1650)
	spin_left(900,900)
   	drive_to_black(900)
	back_to_white(900)
  	arm_down()
 	move_forward(900, 575)
	#pick up fire-man
   	claw_close()
   	spin_right(500,400)
	claw_open()
   	arm_up()
 	#GO GET FIREMAN #5
   	move_back(900,2700)
	spin_right(900,300)
	move_back(900,1000)
        

	move_forward(900, 1650)
	spin_left(900,900)
   	drive_to_black(900)
	back_to_white(900)
  	arm_down()
 	move_forward(900, 575)
	#pick up fire-man
   	claw_close()
   	spin_right(500,400)
	claw_open()
   	arm_up()
  	claw_close()
    #ALL SCORED!!!
	spin_right(900,500)
	move_forward(900,300)
	arm_down()
	spin_left(200 , 300)
    
  	#reset position
   	arm_up()        
  	spin_left(900, 300)
   	move_back(900, 2500)
  	spin_right(900, 200)
   	move_back(900, 2000)#hit pipe to realign
   	move_forward(1400, 1750)
  	spin_right(900, 900)
   	drive_to_black(900)
 	claw_open()
 	arm_down()
 	move_forward(1500, 1000)
  	claw_close()
  	arm_up()
   	spin_left(1500, 800)
  	move_forward(1500, 200)
  	drive_to_black(1400)
 	drive_to_white(1400)
  	move_forward(1400, 1200)
  	claw_open()
  	#set_servo_position(ARM_PORT,1275)