#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Draw static text
"""

from .luaplot import LuaGraph, LuaTexts


class LuaStaticText(LuaGraph, LuaTexts):
    def __init__(self, draw_area):

        LuaGraph.__init__(self, draw_area)
        LuaTexts.__init__(self)

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
