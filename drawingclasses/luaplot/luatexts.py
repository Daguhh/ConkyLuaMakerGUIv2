#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

from math import pi, sin, cos

import pygame

from .math_tools import PositionMathTool as pmt
from .math_tools import PositionValueObject as pval


class LuaTexts:
    def __init__(self):

        self.input_remaning = 1

    def draw(self, position):

        g = self.grid_step
        self._pos = pval((position[0][0] // g * g, position[0][1] // g * g))

        self.myfont = pygame.font.SysFont(self.dct["font"], self.dct["font_size"])
        textsurface = self.myfont.render(
            self.dct[self.text_name], False, self.dct["color"]
        )

        _, h = textsurface.get_size()
        p = self._pos + (0, -h)
        self.dct["from"] = pval((0, h))
        self._pos = p

    def update(self):

        p = self._pos + self.dct["from"]
        g = self.grid_step
        p = pmt.discretize(p, g)
        self.myfont = pygame.font.SysFont(self.dct["font"], self.dct["font_size"])
        textsurface = self.myfont.render(
            self.dct[self.text_name], False, self.dct["color"]
        )
        self.surface = pygame.transform.rotate(textsurface, self.dct["rotation_angle"])
        self.mask = pygame.mask.from_surface(self.surface)

        A = self.dct["rotation_angle"]
        _, th = textsurface.get_size()
        sw, sh = self.surface.get_size()

        if 270 <= A:
            x, _ = pmt.rot((0, th * (1 - 0.8)), A)
            _, y = pmt.rot((0, th * 0.8), A)
        elif 180 <= A and A < 270:
            x1, _ = pmt.rot((0, th * 0.8), A)
            x = -(sw + x1)
            y = 0
        elif 90 <= A and A < 180:
            x = -sw
            _, y1 = pmt.rot((0, th * 0.8), A)
            y = +(sh + y1)
        elif A < 90:
            x, _ = pmt.rot((0, th), A)
            x = -x
            y = sh

        x, y = int(x), int(y)

        self.dct["from"] = pval((-x, y))
        p = p + (x, -y)
        self.pos = p

    def resize(self, new_mouse_pos):
        vect = new_mouse_pos - self._pos
        norm = vect.norm()
        self.dct["font_size"] = int(norm / 4)
