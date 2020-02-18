#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

from .luaplot import LuaGraph, BarNLine

class LuaLine(LuaGraph, BarNLine):

    def __init__ (self, draw_area) :

        LuaGraph.__init__(self)
        BarNLine.__init__(self)

        self.draw_area = draw_area
        self.name = "line"
        
        self.grid_step = 1
        self.input_remaning = 2
        
        self.color_name = "color"
        self.thickness_name = "thickness"

        self.dct = {"kind" : 'line',
                    "from" : (0,0),
                    "to" : (1,1),
                    "color" : (255,255,255),
                    "alpha" : 1,
                    "thickness" : 10,
                    "graduated" : False,
                    "number_graduation" : 10,
                    "space_between_graduation" : 1}
                
