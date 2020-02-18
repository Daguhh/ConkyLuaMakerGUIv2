#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from .luaplot import LuaGraph, BarNLine


class LuaBarGraph(LuaGraph, BarNLine):
    def __init__(self, draw_area):

        LuaGraph.__init__(self)
        BarNLine.__init__(self)

        self.draw_area = draw_area
        self.name = "bar_graph"

        self.input_remaning = 2
        self.grid_step = 1

        self.color_name = "bar_color"
        self.thickness_name = "bar_thickness"

        self.dct = {
            "kind": "bar_graph",
            "from": (0, 0),
            "to": (1, 1),
            "conky_value": "cpu cpu0",
            "max_value": 100,
            "critical_threshold": 90,
            "background_color": (0, 0, 0),
            "background_alpha": 1,
            "background_thickness": 8,
            "bar_color": (0, 0, 0),
            "bar_alpha": 1,
            "change_thickness_on_critical": False,
            "bar_thickness": 15,
            "change_color_on_critical": False,
            "background_color_critical": (0, 0, 0),
            "change_alpha_on_critical": False,
            "background_alpha_critical": 1,
            "background_thickness_critical": 8,
            "bar_color_critical": (0, 0, 0),
            "bar_alpha_critical": 1,
            "bar_thickness_critical": 10,
            "graduated": False,
            "number_graduation": 10,
            "space_between_graduation": 2,
        }
