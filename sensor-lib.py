#!/usr/bin/python
import os, sys
from wallaby import *
def analog_average(port, reads):
	total = 0;
	for reading in range(reads):
		total += analog(port);
	return total / reads;
