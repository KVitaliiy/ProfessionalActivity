#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import time
from math import pi

# initialization coefficient

k1 = -284.01564943464314
k2 = -7.1422658838740904
k3 = -45.15236978817198

# initialization motors

motorR = LargeMotor('outA')
motorL = LargeMotor('outD')


motorR.position = 0
motorL.position = 0

TimeStart = time()
currentTime = time()

# initialization gyro sensors

Gyrosensor_for_angle = GyroSensor('in3')
Gyrosensor_for_rate = GyroSensor('in1')
start_angle = Gyrosensor_for_angle.angle * pi / 180
start_rate = -Gyrosensor_for_rate.rate * pi / 180
# initialization file

dataOutput = open("data_of_6labs.txt","w+")

# start

while currentTime - TimeStart < 10:

    angleR = motorR.position * pi / 180
    angleL = motorL.position * pi / 180
    difAngleTetta = (motorR.speed + motorL.speed)/2 * pi / 180

    MeanAngle = Gyrosensor_for_angle.angle * pi / 180 - start_angle
    MeanRotationAngle = -(Gyrosensor_for_rate.rate * pi / 180 - start_rate)


    ErrDifAngleTetta = -difAngleTetta
    ErrAngle = -MeanAngle
    ErrRotate = - MeanRotationAngle

    u = ErrAngle*k1 + ErrDifAngleTetta*k2 + ErrRotate*k3

    if u >= 100:
        u = 100
    if u <= - 100:
        u = -100

    motorR.run_direct(duty_cycle_sp=(int(u)))
    motorL.run_direct(duty_cycle_sp=(int(u)))
    dataOutput.write(str(u) + "\t" + str(MeanAngle) + "\t" + str(MeanRotationAngle) + "\t" + str(difAngleTetta) + "\t" + str(currentTime - TimeStart) + "\n")

dataOutput.close()
motorR.stop(stop_action='brake')
motorL.stop(stop_action='brake')