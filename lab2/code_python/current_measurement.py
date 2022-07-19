#!/usr/bin/env python3
from ev3dev.ev3 import*
import time

def current_measumerent(volt):
	motorA = LargeMotor('outA')
	timeStart = time.time()
	timeNow = time.time() - timeStart
	try:
		while (timeNow < 8):
		motorA.run_direct(duty_cycle_sp = 100)
		timeNow = time.time() - timeStart

	finally:
		motorA.stop(stop_action = 'brake')
		time.sleep(1)

for volt in range(10,101,10):
	current_measumerent(volt)