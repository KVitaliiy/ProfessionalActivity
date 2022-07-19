#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

def degree_rotation(angle):
	motorA = LargeMotor('outA')
	timeStart = time.time()
	motorA.position = 0
	timeNow = time.time() - timeStart
	data = open('data_for_voltage_' + "kp=1.0;ki=0.001;kd=21.0" + '_.txt', 'w')
	kp = 1.0
	ki = 0.001
	kd = 21.0
	e = 0
	integral = 0
	derivative = 0
	tp = time.time()
	tpend = 0
	tetamax = 0
	try:
		while (timeNow < 10):
			tp = time.time()
			preve = e
			e = angle - motorA.position
			integral += e
			derivative = e - preve

			if (abs(angle - motorA.position) < 0.05*angle) and (tpend == 0):
				tpend = tp - timeStart
			if tpend != 0 and not(abs(angle - motorA.position) < 0.05*angle):
				tpend = 0

			if  kp*e + ki*integral + kd*derivative > 100:
				voltage = 100
			elif kp*e + ki*integral + kd*derivative < -100:
				voltage = -100
			else: voltage = kp*e + ki*integral + kd*derivative

			motorA.run_direct(duty_cycle_sp = voltage)
			timeNow = time.time() - timeStart
			data.write(str(motorA.position))
			data.write('\t' + str(round(timeNow,3)) + '\n')

			if tetamax < motorA.position:
				tetamax = motorA.position
			teta = motorA.position
	finally:
		data.write("Est" + str(angle - teta) + "\n")
		data.write("Tetamax" + str(tetamax) + "\n")
		data.write("Perereg" + str((tetamax - teta)/(teta)*100) + "%\n")
		data.write("tp = " + str(tpend))
		data.close()
		motorA.stop(stop_action = 'brake')
		time.sleep(3)

degree_rotation(180)