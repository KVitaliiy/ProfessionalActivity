#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

def degree_rotation(angle):

	motorA = LargeMotor('outA')
	timeStart = time.time()
	motorA.position = 0
	timeNow = time.time() - timeStart
	tp = time.time()
	tpend = 0
	tetamax = 0

	data = open('degree_rotation_' + "180" + '_.txt', 'w')

	while (timeNow < 10):
		tp = time.time()
		if (abs(angle - motorA.position) < 0.05*angle) and (tpend == 0):
			tpend = tp
		if tpend != 0 and not(abs(angle - motorA.position) < 0.05*angle):
			tpend = 0
		if motorA.position < angle:
			voltage = 100
		elif motorA.position == angle:
			voltage = 0
		elif motorA.position > angle:
			voltage = -100
		motorA.run_direct(duty_cycle_sp = voltage)
		timeNow = time.time() - timeStart
		data.write(str(motorA.position))
		data.write('\t' + str(round(timeNow,3)) + '\n')
		if tetamax < motorA.position:
			tetamax = motorA.position


	data.write("Est" + str(angle - motorA.position) + "\n")
	data.write("Maxteta" + str(tetamax) + "\n")
	data.write("Pererg" + str((tetamax - motorA.position)/motorA.position*100) + "%")
	data.write("tp = " + str(tpend))
	data.close()
	motorA.stop(stop_action = 'brake')


degree_rotation(180)