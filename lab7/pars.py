import numpy as np
from math import cos, sin, pi

a1 = 0.003
a2 = 0.16
a3 = 0.1
d1 = 0.173

h = a2 + a3 + d1

#d2 = 
#d3 = 

#a = [a1, a2, a3]
#alpha = [alpha1, alpha2, alpha3]
#d = [d1, d2, d3]
#tetta = [tetta1, tetta2, tetta3]

start_coords = [0, 0, h, 1]

tetts = [-45.0 * pi / 180, 117.14354649698804 * pi / 180, 117.69202155261765 * pi / 180]


def get_coord(start_coords, tetts):

	tetta1 = tetts[0]
	tetta2 = tetts[1]
	tetta3 = tetts[2]

	t01 = np.array([[cos(tetta1), 0, sin(tetta1), a1 * cos(tetta1)], 
			   [sin(tetta1), 0, -cos(tetta1), a1 * sin(tetta1)],
			   [0, 1, 0, d1],
			   [0, 0, 0, 1]])
	print(t01)

	t02 = np.array([[cos(tetta2), -sin(tetta2), 0, a2 * cos(tetta2)], 
				   [sin(tetta2), cos(tetta2), 0, a2 * sin(tetta2)],
				   [0, 0, 1, 0],
				   [0, 0, 0, 1]])
	print(t02)
	t03 = np.array([[cos(tetta3), -sin(tetta3), 0, a3 * cos(tetta3)],
				   [sin(tetta3), cos(tetta3), 0, a3 * sin(tetta3)],
				   [0, 0, 1, 0],
				   [0, 0, 0, 1]])
	print(t03)
	#mp = t02.dot(t03)
	#mp = t01.dot(mp)
	mp = t01.dot(t02)
	mp = mp.dot(t03)
	#mp = np.linalg.inv(mp)
	print(mp)
	result = mp.dot(start_coords)
	print(result)
	return result

a = get_coord(start_coords,tetts)