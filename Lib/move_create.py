#!/usr/bin/python
import os, sys
from wallaby import *

def forward(speed, dist):
	set_create_distance(0)
	create_drive_direct(speed, speed)
  	while get_create_distance() < dist:
		pass
 	create_drive_direct(0,0)
