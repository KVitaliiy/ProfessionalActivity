#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import time
from math import pi

uMax = 100
# initialization coefficient

k1 = -364.08600946396876
k2 = -10.201263472048172
k3 = -64.12254061306304

# initialization motors

motorR = LargeMotor('outA')
motorL = LargeMotor('outD')


motorR.position = 0
motorL.position = 0


TimeStart = time()
currentTime = time()

# initialization gyro sensors

Ga = GyroSensor('in2')
Gr = GyroSensor('in3')
Ga.mode = 'GYRO-ANG'
Gr.mode = 'GYRO-RATE'

startangle = -Ga.value() * pi / 180
startrate = Gr.value() * pi / 180
# initialization file

dataOutput = open("data_of_6labs.txt","w+")

# start

while currentTime - TimeStart < 7:

    prevTime = currentTime
    currentTime = time()
    dt = currentTime - prevTime

    difAngleTetta = (motorR.speed + motorL.speed)/2

    MeanAngle = Ga.value() * pi / 180 - startangle
    MeanRotationAngle = -(Gr.value() * pi / 180 - startrate)


    ErrDifAngleTetta = -difAngleTetta
    ErrAngle = -MeanAngle
    ErrRotate = - MeanRotationAngle

    u = ErrAngle*k1 + ErrDifAngleTetta*k2 + ErrRotate*k3

    if u >= uMax:
        u = uMax
    if u <= -uMax:
         u = -uMax

    motorR.run_direct(duty_cycle_sp=(int(u)))
    motorL.run_direct(duty_cycle_sp=(int(u)))
    dataOutput.write(str(u) + "\t" + str(MeanAngle) + "\t" + str(MeanRotationAngle) + "\t" + str(difAngleTetta) + "\t" + str(currentTime-TimeStart) + "\n")
    print(str(MeanAngle) + "\t" + str(MeanRotationAngle) + "\t" + str(u))

dataOutput.close()
motorR.stop(stop_action='brake')
motorL.stop(stop_action='brake')