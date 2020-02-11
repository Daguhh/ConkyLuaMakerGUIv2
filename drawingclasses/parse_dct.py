#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:10:20 2018

@author: david
"""



def lua2pil_dct(lua_dct, pos):
    pil_dct = {}
    for k, v in lua_dct.items() :
        #print("A^^^^^^^^^^^^^^^^^^^^^^^^^^^A")
        #print(k,v)
        try :
            if k in INT_LIST     : v = int(v)
            elif k in FLOAT_LIST : v = float(v)
            elif k in TEXT_LIST  : v = v[1:-1]
            elif k in TUPLE_LIST : v = unformat_xy(v, pos)
            elif k in COLOR_LIST : v = lua2pil_color(v)
            elif k in ANGLE_LIST : v = 360 - int(v)
            elif k in KIND_LIST : v = v[1:-1]
            elif k in BOOL_LIST :
                if v == 'true' :  v = True
                else : v  = False

            pil_dct[k] = v

        except TypeError:

            print('type error')
            print('value for {} is a {}'.format(k,type(v)))
            print('value has not been changed\nplease change the it\nor reload object(left click on preview)')
            pil_dct[''] = ''

        except ValueError:

            print('\nvalue error')
            print('value for {} is a {}'.format(k,type(v)))
            print('value has not been changed\nplease change the it\nor reload object(left click on preview)')
            pil_dct[''] = ''
#        else :
#            print('nul!!!!!!!!!!!!!!!')
#        except :
#            print('except')


    return pil_dct

def pil2lua_dct(pil_dct, pos):
    lua_dct={}
    for k, v in pil_dct.items() :
#        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#        print(k,v)
        try :
            if k in INT_LIST     : pass
            elif k in FLOAT_LIST : pass
            elif k in TEXT_LIST  : v = "'{}'".format(v)
            elif k in TUPLE_LIST : v = format_xy(v, pos)
            elif k in COLOR_LIST : v = pil2lua_color(v)
            elif k in ANGLE_LIST : v = 360 - (v)
            elif k in KIND_LIST : v = "'{}'".format(v)
            elif k in BOOL_LIST  :
                if v == True :  v = 'true'
                else : v  = 'false'
        except :
            print('except')

        lua_dct[k] = v

    return lua_dct

global INT_LIST
INT_LIST = ["radius",
            "max_value",
            "critical_threshold",
            "bar_thickness",
            "thickness",
            "background_thickness",
            "background_thickness_critical",
            "bar_thickness_critical",
            "font_size",
            "number_graduation"]
global FLOAT_LIST
FLOAT_LIST = ["alpha",
              "bar_alpha",
              "background_alpha",
              "background_alpha_critical",
              "width",
              "height"]
global TEXT_LIST
TEXT_LIST = ["conky_value",
             "text",
             "font"]
global KIND
KIND_LIST = ["kind"]
global TUPLE_LIST
TUPLE_LIST = ["center",
              "from",
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
global ANGLE_LIST
ANGLE_LIST = ["start_angle",
              "end_angle",
              "rotation",
              "rotation_angle"]

def lua2pil_color(lua_color) :

    lua_color = lua_color[1:-1]
    #print(lua_color)

    ind = [slice(2*n, 2*n+2) for n in range(1,4)]
    pil_color = tuple([int(lua_color[i],16) for i in ind])
    return pil_color

#    gen = [slice(2*x,2*x+2) for x in range(3)]
#    pil_color = tuple([int(lua_color.split('x')[1][s],16) for s in gen])
#    return pil_color

def pil2lua_color(pil_color) :

    lua_color = '0x'+''.join('{:02x}'.format(c) for c in pil_color)
    lua_color = "'{}'".format(lua_color)
    return lua_color

def unformat_xy(xy, pos) :
    ind_x = xy.find('x=')
    ind_y = xy.find('y=')
    ind_vir = xy.find(',')
    x = int(xy[ind_x+2:ind_vir])
    y = int(xy[ind_y+2:-1])
    x = x - pos[0]
    y = y - pos[1]
    return (x,y)

def format_xy(center, pos) :
    x = int(pos[0]+center[0])
    y = int(pos[1]+center[1])
    center = ("{}x={}, y={}{}".format('{',x,y,'}'))
    return center

