#!/usr/bin/env python3
from math import atan2, sqrt, acos, pi

from ev3dev.ev3 import *
import time

motorA = LargeMotor('outA')
motorA.position = 0

motorB = LargeMotor('outB')
motorB.position = 0

motorC = LargeMotor('outC')
motorC.position = 0

kp1 = 1
kp2 = 0.5
kp3 = 2
ki1 = 0.005
ki2 = 0.015
ki3 = 0.015

k_1 = 0.33
k_2 = 0.21
k_3 = 0.21

timeStart = time.time()
integral_1 = 0
integral_2 = 0
integral_3 = 0

x = 0
y = 0
z = 0
a1 = 0.3
a2 = 16
a3 = 10
d1 = 17.3

h = a2 + a3 + d1

theta_1 = 0
theta_2 = 90
theta_3 = 0

points = [[10, 10, 25], [-10, -10, 25],  [15, -10, 25], [0, -20, 25], [0, 0, h]]
for i in range(4):
    data = open('test_7_' + str(i) + '.txt', 'w')

    if (i == 0):
        angle1 = 90
        angle2 = 90
        angle3 = 90

    if (i == 1):
        angle1 = 0
        angle2 = 45
        angle3 = 45

    if (i == 2):
        angle1 = 180
        angle2 = 45
        angle3 = 45

    if (i == 3):
        angle1 = 0
        angle2 = 0
        angle3 = 0


    data.write(str(angle1) + " " + str(angle2) + " " + str(angle3) + "\n")

    error_1 = angle1 - theta_1
    error_2 = angle2 - theta_2
    error_3 = angle3 - theta_3

    while error_1**2 + error_2**2 + error_3**2 > 2:
        theta_1 = k_1 * motorC.position
        theta_2 = k_2 * motorB.position
        theta_3 = k_3 * motorA.position

        t = time.time()

        error_1 = angle1 - theta_1
        error_2 = angle2 - theta_2
        error_3 = angle3 - theta_3

        integral_1 = integral_1 + error_1
        integral_2 = integral_2 + error_2
        integral_3 = integral_3 + error_3

        U_1 = kp1 * error_1 + ki1 * integral_1
        U_2 = kp2 * error_2 + ki2 * integral_2
        U_3 = kp3 * error_3 + ki3 * integral_3

        if U_1 > 100:
            U_1 = 100
        if U_1 < -100:
            U_1 = -100

        if U_2 > 100:
            U_2 = 100
        if U_2 < -100:
            U_2 = -100

        if U_3 > 100:
            U_3 = 100
        if U_3 < -100:
            U_3 = -100

        motorA.run_direct(duty_cycle_sp=U_3)
        motorB.run_direct(duty_cycle_sp=U_2)
        motorC.run_direct(duty_cycle_sp=U_1)

        data.write(str(t - timeStart) + " " + str(theta_1) + " " + str(theta_2) + " " + str(theta_3) + "\n")

    motorA.run_direct(duty_cycle_sp=0)
    motorB.run_direct(duty_cycle_sp=0)
    motorC.run_direct(duty_cycle_sp=0)

    data.close()
    time.sleep(2)

motorA.run_direct(duty_cycle_sp=0)
motorA.stop(stop_action='brake')

motorB.run_direct(duty_cycle_sp=0)
motorB.stop(stop_action='brake')

motorC.run_direct(duty_cycle_sp=0)
motorC.stop(stop_action='brake')
