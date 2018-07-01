#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:10:20 2018

@author: david
"""

class Properties :
    def __init__(self, dct) :
        for k, v in dct.items():
            print(k)
            setattr(self, k, v)

    def __setattr__(self, name, value) :
        if name in INT_LIST     : value = int(value)
        elif name in FLOAT_LIST : value = float(value)
        elif name in TEXT_LIST  : value = str(value)
        elif name in TUPLE_LIST : value = unformat_xy(value)
        elif name in COLOR_LIST : value = "#" + value[2:]
        elif name in BOOL_LIST :
            if value == "y" :  value = 1
            else : value  = 0
        self.__dict__[name] = value

    def uformat(self, name) :
        value = self.__dict__[name]
        if name in INT_LIST     : pass
        elif name in FLOAT_LIST : pass
        elif name in TEXT_LIST  : pass
        elif name in TUPLE_LIST : value = format_xy(value)
        elif name in COLOR_LIST : value = "0x" + value[1:]
        elif name in BOOL_LIST  :
            if value == 1 :  value = "true"
            else : value  = "false"
        elif name in STYLISTIK_LIST : value = " "
        return value

global INT_LIST
INT_LIST = ["radius",
            "max_value",
            "critical_threshold",
            "bar_thickness",
            "background_thickness",
            "background_thickness_critical",
            "bar_thickness_critical",
            "start_angle",
            "end_angle",
            "fontsize",
            "rotation"]
global FLOAT_LIST
FLOAT_LIST = ["bar_alpha",
              "background_alpha",
              "background_alpha_critical"]
global TEXT_LIST
TEXT_LIST = ["conky_value",
             "text",
             "font"]
global TUPLE_LIST
TUPLE_LIST = ["center",
              "fro",
              "to"]
global COLOR_LIST
COLOR_LIST = ["bar_color",
              "color",
              "background_color",
              "background_color_critical",
              "bar_color_critical"]
global BOOL_LIST
BOOL_LIST = ["change_color_on_critical",
             "change_alpha_on_critical",
             "change_thickness_on_critical"]
             
STYLISTIK_LIST = ["bold",
                  "italic"]


def unformat_xy(xy) :
    ind_x = xy.find('x=')
    ind_y = xy.find('y=')
    ind_vir = xy.find(',')
    x = int(xy[ind_x+2:ind_vir])
    y = int(xy[ind_y+2:-1])
    return (x,y)

def format_xy(center) :
    x = center[0]
    y = center[1]
    center = ("{}x={}, y={}{}".format('{',x,y,'}'))
    return center

