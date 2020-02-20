#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw variable text that show a conky value
"""
from .luaplot import LuaGraph, LuaTexts


class LuaVariableText(LuaGraph, LuaTexts):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaTexts.__init__(self)

        self.text_name = "conky_value"

        self.dct = {
            "kind": "variable_text",
            "from": (0, 0),
            "conky_value": "uptime",
            "color": (200, 200, 200),
            "rotation_angle": 0,
            "font": "Comic Sans MS",
            "font_size": 12,
            "bold": False,
            "italic": False,
            "alpha": 1,
        }
