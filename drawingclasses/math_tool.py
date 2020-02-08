
from math import pi, cos, sin

def rotation_transformation(vect, theta) :
    A = theta*pi/180
    x = vect[0]
    y = vect[1]
    r = ((cos(A), sin(A)), -sin(A) + cos(A))
    new_x = x*cos(A) + y * sin(A)
    new_y = -x*sin(A) + y * cos(A)
    return (new_x, new_y)
