#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from .luaplot import LuaGraph, LuaRings


class LuaRingGraph(LuaGraph, LuaRings):
    def __init__(self, draw_area):

        LuaGraph.__init__(self)
        LuaRings.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 1

        self.name = "ring_graph"
        self.input_remaning = 2

        self.color_name = "bar_color"
        self.thickness_name = "bar_thickness"

        self.dct = {
            "kind": "ring_graph",
            "center": (0, 0),
            "radius": 1,
            "conky_value": "fs_used_perc /home/",
            "max_value": 100,
            "critical_threshold": 90,
            "bar_color": (22, 255, 255),
            "bar_alpha": 1,
            "bar_thickness": 8,
            "background_color": (255, 255, 255),
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
