#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Create an object to store position in tuple like format : (x,y)
It permit to perform several mathematical operation :
    - add 
    - sub 
    - mul
    - div
    - get norm, max, min, rotate
    - vectorial product
"""

from math import pi, cos, sin


class PositionValueObject:
    def __init__(self, tup):
        self._tup = tup

    def __repr__(self):
        return str(self._tup)

    def __getitem__(self, index=[0, 1]):
        if index == None:
            return self._tup
        else:
            return self._tup[index]

    def __setitem__(self, index=[0, 1], val=(0, 0)):
        tup = self._tup
        if isinstance(index, int):
            tup = (
                val * (index == 0) + tup[0] * (index != 0),
                val * (index == 1) + tup[1] * (index != 1),
            )
        else:
            tup = val
        self._tup = tup

    def __add__(self, v):
        u = self._tup
        tup = tuple([ux + vx for ux, vx in zip(u, v)])
        return PositionValueObject(tup)

    def __radd__(self, v):
        u = self._tup
        tup = tuple([ux + vx for ux, vx in zip(u, v)])
        return PositionValueObject(tup)

    def __sub__(self, v):
        u = self._tup
        tup = tuple([ux - vx for ux, vx in zip(u, v)])
        return PositionValueObject(tup)

    def __rsub__(self, v):
        u = self._tup
        tup = tuple([vx - ux for ux, vx in zip(u, v)])
        return PositionValueObject(tup)

    def __mul__(self, times):
        tup = (self._tup[0] * times, self._tup[1] * times)
        return PositionValueObject(tup)

    def __rmul__(self, times):
        tup = (self._tup[0] * times, self._tup[1] * times)
        return PositionValueObject(tup)

    def __xor__(self, v):

        u = tuple(self._tup) + (0,)
        v = tuple(v) + (0,)

        w = (
            (u[1] * v[2] - u[2] * v[1]),
            (u[2] * v[0] - u[0] * v[2]),
            (u[0] * v[1] - u[1] * v[0]),
        )

        return PositionValueObject(w)

    def __abs__(self):
        tup = self._tup
        tup = abs(tup[0]), abs(tup[1])
        return PositionValueObject(tup)

    def get(self):
        return self._tup

    def norm(self):
        tup = self._tup
        return (sum(tuple([ux ** 2 for ux in tup]))) ** 0.5

    def __truediv__(self, val):
        tup = self._tup
        tup = tuple([u / val for u in tup])
        return PositionValueObject(tup)


class PositionMathTool:
    def __init__(self):
        pass

    def max(*tup):
        tup = tup[0]
        x = max([t[0] for t in tup])
        y = max([t[1] for t in tup])
        return PositionValueObject((x, y))

    def min(*tup):
        tup = tup
        x = min([t[0] for t in tup])
        y = min([t[1] for t in tup])
        return PositionValueObject((x, y))

    def discretize(tup, step):
        tup = (tup[0] // step * step, tup[1] // step * step)
        return PositionValueObject(tup)

    def rot(vect, theta):
        A = theta * pi / 180
        x = vect[0]
        y = vect[1]
        r = ((cos(A), sin(A)), -sin(A) + cos(A))
        new_x = x * cos(A) + y * sin(A)
        new_y = -x * sin(A) + y * cos(A)
        return (new_x, new_y)


if __name__ == "__main__":

    a = PositionValueObject((10, 10, 10))

    a = a + (1, 1, 5)
