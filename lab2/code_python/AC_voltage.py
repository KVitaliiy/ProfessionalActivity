#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math

def write_data(w):
	motorA = LargeMotor('outA')
	timeStart = time.time()
	motorA.position = 0
	timeNow = time.time() - timeStart
	voltage = 100

	data = open('data_for__' + str(w) + '_.txt', 'w')

	try:
		while (timeNow < 3):
		motorA.run_direct(duty_cycle_sp = voltage*math.sin(w*timeNow))
		timeNow = time.time() - timeStart
		data.write(str(motorA.position))
		data.write(' '*10 + str(round(timeNow,3)) + '\n')

	finally:
		data.close()
		motorA.stop(stop_action = 'brake')
		time.sleep(1)
values_w = (math.pi,2*math.pi,3*math.pi)
for w in values_w:
	write_data(w)