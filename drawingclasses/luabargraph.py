#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw bar monitor
"""

from .luaplot import LuaGraph, BarNLine


class LuaBarGraph(LuaGraph, BarNLine):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        BarNLine.__init__(self)

        self.name = "bar_graph"
        self.color_name = "bar_color"
        self.thickness_name = "bar_thickness"

        self.dct = {
            "kind": "bar_graph",
            "from": (0, 0),
            "to": (1, 1),
            "conky_value": "cpu cpu0",
            "max_value": 100,
            "critical_threshold": 90,
            "background_color": (85, 85, 85),
            "background_alpha": 1,
            "background_thickness": 8,
            "bar_color": (200, 200, 200),
            "bar_alpha": 1,
            "change_thickness_on_critical": False,
            "bar_thickness": 15,
            "change_color_on_critical": False,
            "background_color_critical": (85, 85, 85),
            "change_alpha_on_critical": False,
            "background_alpha_critical": 1,
            "background_thickness_critical": 8,
            "bar_color_critical": (85, 85, 85),
            "bar_alpha_critical": 1,
            "bar_thickness_critical": 10,
            "graduated": False,
            "number_graduation": 10,
            "space_between_graduation": 2,
        }
