#!/usr/bin/env python3
from ev3dev.ev3 import *
from math import cos, sin, pi, atan2

def calculate_asimut(goal, cordrob):
	if (goal[1]!=cordrob[1] and goal[0]!=cordrob[0]):
		return atan2((goal[1]-cordrob[1]), (goal[0]-cordrob[0]))
	if (goal[0] == cordrob[0]) and (goal[1] > cordrob[1]): 
		return pi/2
	elif (goal[0] == cordrob[0]) and (goal[1] < cordrob[1]): 
		return -pi/2
	if (goal[1] == cordrob[1]) and (goal[0] > cordrob[0]):
		return 0
	elif (goal[1] == cordrob[1]) and (goal[0] < cordrob[0]):
		return pi

def calculate_UR(Us, Ur, Umax):
	if abs(Us + Ur)*100/Umax <= 100:
		return (Us + Ur)*100/Umax
	elif (Us + Ur) > 0:
		return 100
	else: 
		return 100

def calculate_UL(Us, Ur, Umax):
	if abs(Us - Ur)*100/Umax <= 100: # <= Umax
		return (Us-Ur)*100/Umax
	elif (Us - Ur) > 0:
		return 100
	else: 
		return -100

def run(goal, cordrob, tetta): 
	motorR = LargeMotor('outA')
	motorL = LargeMotor('outB')

	r = 0.03 # радиус колеса в метрах
	b = 0.155 # рассотяние между центрами колес в метрах

	motorR.position = 0
	motorL.position = 0

	angleR, angleL = 0,0

	Umax = 7 # макимальное напряжение

	data = open("test1square" + str(i) + ".txt", "w+")

	Ks = 7 # коэффициент для движения вперед
	Kr = 85 # коэффициент для поворота

	asimut = calculate_asimut(goal, cordrob)
		
	p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # начальное расстояние

	while (p > 0.3):
		
		xprev = cordrob[0]
		yprev = cordrob[1]

		tettaprev = tetta

		prevangleR = angleR
		prevangleL = angleL

		angleR = motorR.position * pi/180
		angleL = motorL.position * pi/180

		difangleR = angleR - prevangleR
		difangleL = angleL - prevangleL

		srangle = (difangleR+difangleL)/2

		tetta = tettaprev + (difangleR - difangleL)*r/b # считается угол на который повернул робот/ возможно, нужно раньше считать, чем координаты
		cordrob[0] = xprev + cos(tetta)*srangle*r # считается x
		cordrob[1]=  yprev + sin(tetta)*srangle*r # считается y

		p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # считается расстояние от робота до цели

		a = asimut - tetta # считается угол между желаемым положением робота и текущим положением

		Us = Ks * p # расчет напряжения для движения вперед с помощью пропорционального регулятора
		Ur = Kr * a # расчет напряжения для поворота с помощью П регултора


		# Напряжение для правого колеса

		UR = calculate_UR(Us, Ur, Umax)

		# Напряжение для левого колеса

		UL = calculate_UL(Us, Ur, Umax)

		# далее подаем напряжение

		motorR.run_direct(duty_cycle_sp = (UR))
		motorL.run_direct(duty_cycle_sp = (UL))

		# запись угла, на который надо повернуться и координат
		data.write(str(cordrob[0]) +  '\t' + str(cordrob[1]) + '\n')

	data.close()
	motorR.stop(stop_action = 'brake')
	motorL.stop(stop_action = 'brake')	

	return cordrob, tetta

def run_square(first_point, len_side):

	cordrob, tetta = run(first_point, [0,0], 0)
	cordrob, tetta = run((first_point[0] - len_side, first_point[1]), cordrob, tetta)
	cordrob, tetta = run((first_point[0] - len_side, first_point[1] - len_side), cordrob, tetta)
	cordrob, tetta = run((first_point[0], first_point[1] - len_side), cordrob, tetta)
	cordrob, tetta = run(first_point, cordrob, tetta)

if __name__ == "__main__":
	run_square(1,1, 2)