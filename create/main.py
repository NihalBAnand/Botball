#!/usr/bin/python
import os, sys
from wallaby import *
from MoveLib import *
from SensorLib import *
from Effectors import *

RED = 0;
speed = 100
create_connect()
enable_servos()
arm_up()
claw_open()
spin_left(speed, 90)
move_forward(speed, 200)#hit pipe
#get group medical supplies
move_back(speed, 75)

spin_left(speed, 190)
arm_down()
move_forward(speed, 185)

claw_close() #grabbed 1st pile!
set_servo_position(ARM_PORT, ARM_DOWN - 50)
spin_right(speed, 160)
set_servo_position(ARM_PORT, ARM_DOWN)
msleep(1000)
claw_open()
spin_left(speed, 5)
    
#======================GO SCORE PILE 2============
arm_up() ##SCORED FIRST PILE!!
spin_left(speed, 110)
arm_down()
move_forward(speed, 210)
    
claw_close()
spin_right(speed, 145)
claw_open()##scored pile 2
#====================GO SCORE PILE 3
arm_up()
spin_right(speed, 100)
arm_down()
move_forward(speed, 150)
claw_close()
spin_left(speed, 90)
claw_open()
arm_up()
#go score pile 4================================================
spin_right(speed, 83)# spin to face pile 4 
arm_down()
move_forward(speed, 340)
claw_close()
spin_left(speed, 110)
claw_open()
arm_up()
#spin to face water pile
spin_right(speed, 182)
arm_down()
move_forward(speed, 100)
claw_close()
"""
move_back(speed, 50)
spin_right(speed, 90)
"""


    


