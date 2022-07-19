#!/usr/bin/env python3
from ev3dev.ev3 import *
from math import cos, sin, pi, atan2
from time import time

def signum(a):

	if a > 0:
		return 1
	elif a < 0:
		return -1
	else:
		return 0

def run_square(cordtop, length, cordrob, tetta):

	cordrob, tetta = run_points(cordtop, cordrob, tetta)
	cordtop[0] -= length
	cordrob, tetta = run_points(cordtop, cordrob, tetta)
	cordtop[1] -= length
	cordrob, tetta = run_points(cordtop, cordrob, tetta)
	cordtop[0] += length
	cordrob, tetta = run_points(cordtop, cordrob, tetta)
	cordtop[1] += length
	cordrob, tetta  = run_points(cordtop, cordrob, tetta)

	return cordrob, tetta



def run_points(goal, cordrob, tetta):

	motorR = LargeMotor('outA')
	motorL = LargeMotor('outB')

	# test №1: goal[3,0]
	# test №2: goal[0,3]
	# test №3: goal[3,3]
	# test №4: goal[-3,0]
	# test №5: goal[0,-3]
	# test №6: goal[-3,3]
	# test №7: goal[3,-3]
	# test №8: goal[-3,-3]

	r = 0.03 # радиус колеса в метрах
	b = 0.155 # рассотяние между центрами колес

	motorR.position = 0
	motorL.position = 0

	angleR, angleL = 0,0



	Umax = 7 # макимальное напряжение, может быть другим

	data = open(str("(" + goal[0]) + str(goal[1]) +") goal.txt", "w+")

	Ks = 15 # коэффициент для движения вперед, возможно побольше, но точно меньше, чем для поворота
	Kr = 25 # коэффициент для поворота, возможно побольше стоит сделать, но не сильно много


	if (goal[0] != cordrob[0]):
			asimut = atan2((goal[1]-cordrob[1]), (goal[0]-cordrob[0])) # считается угол между целью и осью Ox
		elif (goal[1] > 0):
			asimut = pi/2
		else:
			asimut = -pi/2
		
	p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # начальное расстояние
	prevp = p
	xprev = cordrob[0]
	yprev = cordrob[1]

	tettaprev = tetta
	a = asimut - tetta
	preva = a

	prevangleR = 0
	prevangleL = 0

	integralp = 0
	derivativep = 0
	ip = 5
	dp = 20

	integrala = 0
	derivativea = 0
	ia = 5
	da = 20

	previousTime = time()

	while (p > 0.2):

		currentTime = time()
        dt = currentTime - previousTime
        previousTime = currentTime

		angleR = motorR.position * pi/180
		angleL = motorL.position * pi/180

		difangleR = angleR - prevangleR
		difangleL = angleL - prevangleL

		prevangleR = angleR
		prevangleL = angleL

		srangle = (difangleR+difangleL)/2

		tetta = tettaprev + (difangleR - difangleL)*r/b # считается угол на который повернул робот

		tettaprev = tetta

		cordrob[0] = xprev + cos(tetta)*srangle*r # считается x
		cordrob[1] =  yprev + sin(tetta)*srangle*r # считается y

		xprev = cordrob[0]
		yprev = cordrob[1]

		p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # считается расстояние от робота до цели

		integralp += p*dt

		if integralp > 1:
			integralp = 1

		derivativep = (p - prevp)/dt
		prevp = p

		a = asimut - tetta # считается угол между желаемым положением робота и текущим положением
		integrala += a*dt
		derivativea = (a-preva)/dt
		preva = a
		if (abs(a) > pi):
			a = a - signum(a) * 2 * pi # для кратчайшего угла

		Usinvolt = Ks * p + dp*derivativep + ip*integralp # расчет напряжения для движения вперед с помощью пропорционального регулятора
		Urinvolt= Kr * a + da*derivativea + ia*integrala # расчет напряжения для поворота с помощью П регултора

		Usinpercent = Usinvolt*100/Umax
		Urinpercent = Urinvolt*100/Umax

		if abs(Usinpercent) >= 70:
			Us = 70*signum(Usinpercent)
		if abs(Ur) >= 30:
			Ur = 30*signum(Urinpercent)

		# Блок для правого колеса

		UR = Us + Ur
		UL = Us - Ur

		# далее подаем напряжение

		motorR.run_direct(duty_cycle_sp = (UR))
		motorL.run_direct(duty_cycle_sp = (UL))

		# запись угла, на который надо повернуться и координат, здесь слежует удалить a, когда пройдет все тесты
		data.write(str(cordrob[0]) +  '\t' + str(cordrob[1]) + '\n')

	data.close()
	motorR.stop(stop_action = 'brake')
	motorL.stop(stop_action = 'brake')

	return cordrob, tetta
	
a,b = run_square([1, 1], 2, [0, 0], 0)