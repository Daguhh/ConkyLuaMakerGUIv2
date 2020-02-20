#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw ring monitor
"""

from .luaplot import LuaGraph, LuaRings


class LuaRingGraph(LuaGraph, LuaRings):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaRings.__init__(self)

        self.name = "ring_graph"
        self.color_name = "bar_color"
        self.thickness_name = "bar_thickness"

        self.dct = {
            "kind": "ring_graph",
            "center": (0, 0),
            "radius": 1,
            "conky_value": "fs_used_perc /home/",
            "max_value": 100,
            "critical_threshold": 90,
            "bar_color": (200, 200, 200),
            "bar_alpha": 1,
            "bar_thickness": 8,
            "background_color": (85, 85, 85),
            "background_alpha": 1,
            "background_thickness": 8,
            "change_color_on_critical": False,
            "change_alpha_on_critical": False,
            "change_thickness_on_critical": False,
            "background_color_critical": (0, 0, 0),
            "background_alpha_critical": 1,
            "background_thickness_critical": 8,
            "bar_color_critical": (0, 0, 0),
            "bar_alpha_critical": 1,
            "bar_thickness_critical": 8,
            "start_angle": 360,
            "end_angle": 0,
            "graduated": False,
            "number_graduation": 10,
            "angle_between_graduation": 10,
        }
