#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def tup_max(tup) :
    max0 = max([pt[0] for pt in tup])
    max1 = max([pt[1] for pt in tup])
    return (max0, max1)

def tup_min(tup) :
    min0 = min([pt[0] for pt in tup])
    min1 = min([pt[1] for pt in tup])
    return (min0, min1)

def vect_product(u,v) :

    w = ((u[1]*v[2] - u[2]*v[1]),
         (u[2]*v[0] - u[0]*v[2]),
         (u[0]*v[1] - u[1]*v[0]))

    return w

def tup_tim(a,u) :
    return tuple([a*ux for ux in u])

def tup_sum(u,v) :
    return tuple([ux + vx for ux, vx in zip(u,v)])

def tup_dif(u,v) :
    return tuple([ux - vx for ux, vx in zip(u,v)])

def tup_abs(u) :
    return tuple([abs(ux) for ux in u])

def tup_norm(u) :
    return (sum(tuple([ux**2 for ux in u])))**0.5

