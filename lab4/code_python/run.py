#!/usr/bin/env python3
from ev3dev.ev3 import *
from math import cos, sin, pi, atan2

motorR = LargeMotor('outA')
motorL = LargeMotor('outB')

goal = (7,7) # координаты цели
# test №1: goal[3,0]
# test №2: goal[0,3]
# test №3: goal[3,3]
# test №4: goal[-3,0]
# test №5: goal[0,-3]
# test №6: goal[-3,3]
# test №7: goal[3,-3]
# test №8: goal[-3,-3]

cordrob  = [0,0]

tetta = 0

r = 0.03 # радиус колеса в метрах
b = 0.155 # рассотяние между центрами колес

motorR.position = 0
motorL.position = 0

angleR, angleL = 0,0


Umax = 7 # макимальное напряжение, может быть другим

data = open("test№1.txt", "w+") # название менять на номер теста

Ks = 5 # коэффициент для движения вперед, возможно побольше, но точно меньше, чем для поворота
Kr = 4 # коэффициент для поворота, возможно побольше стоит сделать, но не сильно много

p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # начальное расстояние

while (p > 0.5): # здесь стоит менять точность (0.1), чем дальше едешь, тем меньше точность, к примеру для goal[10,10] while (p > 0 .7)
	
	xprev = cordrob[0]
	yprev = cordrob[1]

	tettaprev = tetta

	prevangleR = angleR
	prevangleL = angleL

	angleR = motorR.position
	angleL = motorL.position

	difangleR = angleR - prevangleR
	difangleL = angleL - prevangleL

	srangle = (difangleR+difangleL)/2

	cordrob[0] = xprev + cos(tetta)*srangle*r # считается x 
	cordrob[1]=  yprev + sin(tetta)*srangle*r # считается y
	tetta = tettaprev + (difangleR - difangleL)*r/b # считается угол на который повернул робот 

	p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # считается расстояние от робота до цели
	asimut = atan2((goal[1]-cordrob[1]), (goal[0]-cordrob[0])) # считается угол между целью и осью Ox 
	a = asimut - tetta # считается угол между желаемым положением робота и текущим положением

	Us = Ks * p # расчет напряжения для движения вперед с помощью пропорционального регулятора
	Ur = Kr * a # расчет напряжения для поворота с помощью П регултора


	# Блок для правого колеса

	if abs(Us + Ur) <= 100: # <= Umax
		UR = Us + Ur 
	elif (Us + Ur) > 0:
		UR = 100
	else: 
		UR = -100

	# блок для левого колеса

	if abs(Us - Ur) <= 100: # <= Umax
		UL = Us - Ur

	elif (Ur + Us) > 0: 
		UL = 100
	else: 
		UL = -100

	# далее подаем напряжение

	motorR.run_direct(duty_cycle_sp = (UR))
	motorL.run_direct(duty_cycle_sp = (UL))

	# запись угла, на который надо повернуться и координат, здесь слежует удалить a, когда пройдет все тесты
	data.write(str(a) + '\t' + str(cordrob[0]) +  '\t' + str(cordrob[1]) + '\n')

data.close()
motorR.stop(stop_action = 'brake')
motorL.stop(stop_action = 'brake')