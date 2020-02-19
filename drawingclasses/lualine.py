#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw simple line
"""

from .luaplot import LuaGraph, BarNLine


class LuaLine(LuaGraph, BarNLine):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        BarNLine.__init__(self)
        
        self.name = "line"
        self.color_name = "color"
        self.thickness_name = "thickness"

        self.dct = {
            "kind": "line",
            "from": (0, 0),
            "to": (1, 1),
            "color": (255, 255, 255),
            "alpha": 1,
            "thickness": 10,
            "graduated": False,
            "number_graduation": 10,
            "space_between_graduation": 1,
        }
