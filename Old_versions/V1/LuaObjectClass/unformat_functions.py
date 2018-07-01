#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 01:25:02 2018

@author: david
"""

        
def unformat_xy(xy) :
    ind_x = xy.find('x=')
    ind_y = xy.find('y=')
    ind_vir = xy.find(',')
    x = int(xy[ind_x+2:ind_vir])
    y = int(xy[ind_y+2:-1])  
    return (x,y)
    
def unformat_color(color) :
    color = '#' + color[2:]
    return color

def unformat_font(font) :
    font = font[1:-1]
    return font