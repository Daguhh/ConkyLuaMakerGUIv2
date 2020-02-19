#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement ring objects
"""

from math import pi

import pygame

from .parse_dct import lua2pil_dct, pil2lua_dct
from .math_tools import PositionMathTool as pmt
from .math_tools import PositionValueObject as pval


class LuaRings:
    def __init__(self):

        self.input_remaning = 2

    def draw(self, positions):

        center = pval(positions[0])
        to = pval(positions[1])
        r = (center - to).norm()

        self._pos = center - (r, r)
        self.dct["center"] = pval((r, r))
        self.dct["radius"] = r

    def update(self):

        c = self.dct["center"]
        r = self.dct["radius"] + self.dct[self.thickness_name] / 2
        p = self._pos

        c = c + p
        g = self.grid_step
        c = pmt.discretize(c, g)
        self._pos = c - (r, r)
        self.dct["center"] = pval((r, r))

        rect = pygame.Rect((0, 0), (2 * r, 2 * r))
        self.surface = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA)
        self.surface.fill(pygame.Color("#77777720"))

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
        radius_vect = new_mouse_pos - center
        self.dct["radius"] = radius_vect.norm()
