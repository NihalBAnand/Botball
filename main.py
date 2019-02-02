#!/usr/bin/python
import os, sys
from wallaby import *
from effectors import *
from sensor-lib import *
from move_wallaby import *
def main():
	enable_servos()
	arm_up()
	msleep(1000)
	arm_down()
	claw_open()    
	move_line(1500, 5000)
	spin_left(1500, 500)
	
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();
