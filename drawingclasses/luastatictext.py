#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

from .luaplot import LuaGraph, LuaTexts


class LuaStaticText(LuaGraph, LuaTexts):
    def __init__(self, draw_area):

        LuaGraph.__init__(self)
        LuaTexts.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 1

        self.input_remaning = 1

        self.text_name = "text"

        self.dct = {
            "kind": "static_text",
            "from": (0, 0),
            "text": "default",
            "color": (0, 0, 0),
            "rotation_angle": 0,
            "font_size": 12,
            "font": "Comic Sans MS",
            "bold": False,
            "italic": False,
            "alpha": 1,
        }
