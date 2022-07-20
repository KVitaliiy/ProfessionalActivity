import numpy as np
from math import sin, cos, pi

alpha = [pi/2, 0, 0]
tetta = [45.0 / 180 * pi, pi/2 - 117.14354649698804 * pi / 180 , 117.14354649698804 * pi / 180]
a = [0.3, 16, 10]
d = [17.3, 0, 0]

x0 = np.matrix([0, 0, 0, 1]).transpose()

z01Rotate = np.matrix([[cos(tetta[0]), sin(tetta[0]), 0, 0], [-sin(tetta[0]), cos(tetta[0]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
x01Rotate = np.matrix([[1, 0, 0, 0], [0, cos(alpha[0]), sin(alpha[0]), 0], [0, -sin(alpha[0]), cos(alpha[0]), 0], [0, 0, 0, 1]])
offset01x = np.matrix([[1, 0, 0, -a[0]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
offset01z = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d[0]], [0, 0, 0, 1]])

z12Rotate = np.matrix([[cos(tetta[1]), sin(tetta[1]), 0, 0], [-sin(tetta[1]), cos(tetta[1]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
offset12x = np.matrix([[1, 0, 0, a[1]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

z23Rotate = np.matrix([[cos(tetta[2]), sin(tetta[2]), 0, 0], [-sin(tetta[2]), cos(tetta[2]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
offset23x = np.matrix([[1, 0, 0, a[2]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

transition01 = np.matmul(z01Rotate, offset01z)
transition01 = np.matmul(offset01x, transition01)
transition01 = np.matmul(x01Rotate, transition01)

transition01 = np.matmul(z12Rotate, transition01)
transition01 = np.matmul(offset12x, transition01)

transition01 = np.matmul(z23Rotate, transition01)
transition01 = np.matmul(offset23x, transition01)

transition01 = np.linalg.inv(transition01)

x1 = np.matmul(transition01, x0) * (-1)

x = float(x1[0][0])
y = float(x1[1][0])
z = float(x1[2][0])

print(x, y, z)