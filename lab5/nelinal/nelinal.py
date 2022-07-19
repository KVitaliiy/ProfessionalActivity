#!/usr/bin/env python3
from ev3dev.ev3 import *
from math import cos, sin, pi, atan2, tanh
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

    # sensor = sensor.lego.UltrasonicSensor(address=None, name_pattern=’sensor*’, name_exact=False, **kwargs)

    # test №1: goal[3,0]
    # test №2: goal[0,3]
    # test №3: goal[3,3]
    # test №4: goal[-3,0]
    # test №5: goal[0,-3]
    # test №6: goal[-3,3]
    # test №7: goal[3,-3]
    # test №8: goal[-3,-3]

    r = 0.028 # радиус колеса в метрах
    b = 0.155 # рассотяние между центрами колес

    motorR.position = 0
    motorL.position = 0

    angleR, angleL = 0,0



    Umax = 7 # макимальное напряжение, может быть другим

    data = open("goal(" + str(goal[0]) + ", " + str(goal[1] + ")"), "w+")

    if (goal[1]!=0 and goal[0]!=0):
        asimut = atan2((goal[1]-cordrob[1]), (goal[0]-cordrob[0]))

    if (goal[0] == 0) and (goal[1] > 0): 
        asimut = pi/2
    elif (goal[0] == 0) and (goal[1] < 0): 
        asimut = -pi/2

    if (goal[1] == 0) and (goal[0] > 0 ):
        asimut = 0
    elif (goal[1] == 0) and (goal[0] < 0):
        asimut = pi
        
        
    p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # начальное расстояние
    prevp = p

    intp = 0 # интеграл оставшейся длины
    derivativep = 0
    ip = 0.1
    dp = 20

    a = asimut - tetta
    preva = a

    inta = 0
    derivativea = 0
    ia = 0.1
    da = 20

    baseSpeed, control = 0, 0 # линейная и угловая скорость

    xprev = cordrob[0]
    yprev = cordrob[1]

    tettaprev = tetta

    prevangleR = 0
    prevangleL = 0

    k_dist = 20

    k_w = 20
    previousTime = time()

    while (p > 0.05):

        currentTime = time()
        dt = currentTime - previousTime
        previousTime = currentTime


        angleR = motorR.position * pi/180
        angleL = motorL.position * pi/180

        prevangleR = angleR
        prevangleL = angleL

        difangleR = angleR - prevangleR
        difangleL = angleL - prevangleL

        srangle = (difangleR+difangleL)/2

        tetta = tettaprev + (difangleR - difangleL)*r/b # считается угол на который повернул робот

        tettaprev = tetta

        cordrob[0] = xprev + cos(tetta)*srangle*r # считается x
        cordrob[1]=  yprev + sin(tetta)*srangle*r # считается y

        xprev = cordrob[0]
        yprev = cordrob[1]

        p = ((goal[0] - cordrob[0])**2 + (goal[1] - cordrob[1])**2)**0.5 # считается расстояние от робота до цели

        intp += p * dt

        derivativep = (p - prevp)/dt

        if (intp > 1):
            intp = 1

        prevp = p


        a = asimut - tetta # считается угол между желаемым положением робота и текущим положением
        inta += a*dt
        if inta > 1:
            inta = 1
        derivativea = (a - preva)/dt
        preva = a

        if (abs(a) > pi):
            a = a - signum(a) * 2 * pi # для кратчайшего угла


        baseSpeedinvolt = Umax * tanh(p) * cos(a) + ip * intp + dp * derivativep
        baseSpeedinpercent = baseSpeedinvolt*100/Umax
        if (abs(baseSpeedinpercent) > 70):
            baseSpeedinpercent = signum(baseSpeedinpercent) * 70;

        controlinvolt = k_w * a + sin(a) * baseSpeedinvolt / p + ia * inta + da * derivativea
        controlinpercent = controlinvolt*100/Umax
        if (abs(controlinpercent) > 30):
            controlinpercent = signum(controlinpercent)*30

        # Блок для правого колеса

        UR = int(baseSpeed + control)

        # блок для левого колеса

        UL = int(baseSpeed - control)

        # далее подаем напряжение

        motorR.run_direct(duty_cycle_sp = (UR))
        motorL.run_direct(duty_cycle_sp = (UL))

        # запись угла, на который надо повернуться и координат
        data.write(str(cordrob[0]) +  '\t' + str(cordrob[1]) + '\n')

    data.close()
    motorR.stop(stop_action = 'brake')
    motorL.stop(stop_action = 'brake')

    return cordrob, tetta

run_square([1,1], 2, [0, 0], 0)