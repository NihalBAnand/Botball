#!/usr/bin/python
import os, sys
from wallaby import *
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
