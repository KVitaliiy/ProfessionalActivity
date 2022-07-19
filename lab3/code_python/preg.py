#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
from math import cos, sin, pi, atan

motorR = LargeMotor('outA')
motorL = LargeMotor('outB')

goal = [1,1]

timeStart = time.time()

cordrob  = [0,0]

tetta = 0

r = 0.03
b = 0.0155

motorR.position = 0
motorL.position = 0

angleR, angleL = 0,0

timeNow = time.time() - timeStart


Ks = 1
Kr = 1

while (p < 0.1):
	
	xprev = cordrob[0]
	yprev = cordrob[1]

	tettaprev = tetta

	prevangleR = angleR
	prevangleL = angleL
	angleR = motorR.position
	angleL = motorL.position
	srangle = (angleL+angleR)/2

	cordrob[0] = xprev + cos(tetta)*srangle*r
	cordrob[1]=  yprev + sin(tetta)*srangle*r
	tetta = tettaprev + (angleR - angleR)*r/b

	p = ((goal[0] - cordrob[0])**2 + (goal[1] + goal[1])**2)**0.5
	asimut = atan((goal[1]-cordrob[1])/(goal[0]-cordrob[0]))
	a = asimut - tetta

	Us = Ks * p
	Ur = Kr*a

	if abs(Ur + Us) <= 100:
		UR = Ur + Us
	elif : UR = 100

	if abs(Ur - Us) <= 100:
		UL = Ur - Us
	elif : UL = 100

	motorR.run_direct(duty_cycle_sp = UR)
	motorL.run_direct(duty_cycle_sp = UR)

	data.write(str(cordrob[0]) +  '\t' + str(cordrob[1])'\n')

data.close()
motorA.stop(stop_action = 'brake')
time.sleep(3)
