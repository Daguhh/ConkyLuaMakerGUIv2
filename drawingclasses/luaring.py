#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw static ring
"""

from .luaplot import LuaGraph, LuaRings


class LuaRing(LuaGraph, LuaRings):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaRings.__init__(self)

        self.name = "ring"
        self.color_name = "color"
        self.thickness_name = "thickness"

        self.dct = {
            "kind": "ring",
            "center": (0, 0),
            "radius": 1,
            "color": (255, 255, 255),
            "alpha": 1,
            "thickness": 8,
            "start_angle": 360,
            "end_angle": 0,
            "graduated": False,
            "number_graduation": 10,
            "angle_between_graduation": 10,
        }
