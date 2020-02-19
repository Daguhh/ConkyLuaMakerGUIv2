#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Class that implement draw of rectangles (for bar and line)
It use pygame.draw
methods :
    - draw 
    - update
    - resize
"""

import pygame

from .math_tools import PositionMathTool as pmt
from .math_tools import PositionValueObject as pval


class BarNLine:
    def __init__(self):
        
        self.input_remaning = 2

    def draw(self, positions):

        self.dct["from"] = pval(positions[0])
        self.dct["to"] = pval(positions[1])

        h = self.dct[self.thickness_name] / 2
        f = pval(positions[0])  # self.dct['from']
        t = pval(positions[1])  # self.dct['to']
        p = pval((0, 0))
        of = pval((1, 1)) * self.dct[self.thickness_name]
        # of = (of,of)

        f = f + p
        t = t + p

        p = pmt.min(f, t)
        f = f - p + of
        t = t - p + of
        p = p - of

        self._pos = p  # .get()
        self.dct["from"] = f  # .get()
        self.dct["to"] = t  # .get()

    def update(self):

        h = self.dct[self.thickness_name] / 2
        f = pval(self.dct["from"])
        t = pval(self.dct["to"])
        p = self._pos
        of = pval((1, 1)) * self.dct[self.thickness_name] * 1
        # of = (of,of)

        f = f + p
        t = t + p

        g = self.grid_step

        f = pmt.discretize(f, g)
        t = pmt.discretize(t, g)

        p = pmt.min(f, t)
        f = f - p + of
        t = t - p + of

        self._pos = p - of
        self.dct["from"] = f  # .get()
        self.dct["to"] = t  # .get()

        dif = t - f
        norm = dif.norm()
        if norm != 0:
            ratio = h / norm
        else:
            ratio = 1
        w_p = ratio * dif ^ (0, 0, 1)
        w_m = ratio * dif ^ (0, 0, -1)

        c0 = f + w_m
        c1 = f + w_p
        c2 = t + w_p
        c3 = t + w_m

        corners = [c0, c1, c2, c3]
        poly = [c.get() for c in corners]
        rect = pmt.max(corners).get()

        self.surface = pygame.Surface(rect, pygame.SRCALPHA)
        self.surface.fill(pygame.Color("#77777720"))
        self.shape = pygame.draw.polygon(self.surface, self.dct[self.color_name], poly)
        self.mask = pygame.mask.from_surface(self.surface)

    def resize(self, new_mouse_pos):

        if (
            self.dct["from"] != new_mouse_pos - self._pos
        ):  # tup_dif(new_mouse_pos,self._pos) :
            self.dct["to"] = (
                new_mouse_pos - self._pos
            )  # tup_dif(new_mouse_pos,self._pos)
