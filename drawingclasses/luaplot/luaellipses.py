#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement ellipse draw from pygame.draw
"""

from math import pi, atan, cos, sin

import pygame

from .parse_dct import lua2pil_dct, pil2lua_dct
from .math_tools import PositionMathTool as pmt
from .math_tools import PositionValueObject as pval


class LuaEllipses:
    def __init__(self):

        self.input_remaning = 2

    def draw(self, positions):

        c = pval(positions[0])
        to = pval(positions[1])
        r = (c - to).norm()

        self.dct["width"] = 2*r
        self.dct["height"] = 2*r
        self._pos = c - (r, r)
        self.dct["center"] = pval((r, r))
        self.dct["radius"] = r

    def update(self):

        c = self.dct["center"]
        p = self._pos
        w = self.dct["width"] + self.dct[self.thickness_name]
        h = self.dct["height"] + self.dct[self.thickness_name]

        c = c + p
        g = self.grid_step
        c = pmt.discretize(c, g)
        self._pos = c - (w/2, h/2)
        self.dct["center"] = pval((w/2, h/2))

        rect = pygame.Rect((0, 0), (w, h))
        self.surface = pygame.Surface((w, h), pygame.SRCALPHA)

        start_angle = self.dct["end_angle"] * pi / 180
        end_angle = self.dct["start_angle"] * pi / 180
        if start_angle > end_angle:
            start_angle, end_angle = end_angle, start_angle

        pygame.draw.arc(
            self.surface,
            self.dct[self.color_name],
            rect,
            start_angle,
            end_angle,
            self.dct[self.thickness_name],
        )

        self.mask = pygame.mask.from_surface(self.surface)

    def resize(self, new_mouse_pos):
        center = self.dct["center"] + self._pos
        x, y = (new_mouse_pos - center).get()
        a, b = self.dct["width"], self.dct["height"]
        if a != 0 and x != 0 and b != 0 and y != 0:

            if x >= 0:
                angle = atan((y / x) / (b / a))
            elif x < 0:
                angle = pi + atan((y / x) / (b / a))
            if angle not in (0,90,180,270):
                self.dct["width"] = 2*x / cos(angle)
                self.dct["height"] = 2*y / sin(angle)
