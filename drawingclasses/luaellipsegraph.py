#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw monitor ellipse
"""

from .luaplot import LuaGraph, LuaEllipses


class LuaEllipseGraph(LuaGraph, LuaEllipses):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaEllipses.__init__(self)

        self.name = "ellipse_graph"
        self.color_name = "bar_color"
        self.thickness_name = "bar_thickness"

        self.dct = {
            "kind": "ellipse_graph",
            "center": (0, 0),
            "radius": 10,
            "conky_value": "cpu cpu0",
            "width": 1,
            "height": 1,
            "max_value": 100,
            "critical_threshold": 90,
            "background_color": (85, 85, 85),
            "background_alpha": 1,
            "background_thickness": 8,
            "bar_color": (200, 200, 200),
            "bar_alpha": 1,
            "bar_thickness": 8,
            "change_color_on_critical": False,
            "change_alpha_on_critical": False,
            "change_thickness_on_critical": False,
            "background_color_critical": (85, 85, 85),
            "background_alpha_critical": 1,
            "background_thickness_critical": 10,
            "bar_color_critical": (85, 85, 85),
            "bar_alpha_critical": 1,
            "bar_thickness_critical": 10,
            "start_angle": 360,
            "end_angle": 0,
            "graduated": False,
            "number_graduation": 10,
            "angle_between_graduation": 10,
        }
