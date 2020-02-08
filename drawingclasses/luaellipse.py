#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui
from math import pi


from .parse_dct import lua2pil_dct, pil2lua_dct
from vectproduct import vect_product, tup_norm, tup_sum, tup_dif, tup_tim
from .luagraph import LuaGraph


import time

class LuaEllipse(LuaGraph) :
    def __init__(self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 1

        self.name = "ellipse"
        self.input_remaning = 2

        self.dct = {
            "kind" : 'ellipse',
            "center" : (0,0),
            "radius" : 10,
            "height" : 1,
            "width" : 1,
            "color" : (255,255,255),
            "alpha" : 1,
            "thickness" : 8,
            "start_angle" : 360,
            "end_angle" : 0,
            "graduated" : False,
            "number_graduation" : 10,
            "angle_between_graduation" : 10,
        }

    def draw(self, positions) :

        c = positions[0]
        to = positions[1]
        r = int(((c[0]-to[0])**2 + (c[1]-to[1])**2)**0.5)

        self.dct['width'] = r
        self.dct['height'] = r
        self.pos = (c[0]-r, c[1]-r)
        self.dct['center'] = (r,r)
        self.dct['radius'] = r

    def update(self) :

        c = self.dct['center']
        p = self.pos

        w = self.dct['width']
        h = self.dct['height']

        c = tup_sum(c,p)
        g = self.grid_step
        c = (c[0]//g*g, c[1]//g*g)
        p = tup_dif(c,(w,h))
        self.pos = (int(p[0]), int(p[1]))
        c = (w,h)
        self.dct['center'] = c

        rect = pygame.Rect((0,0),(2*w,2*h))
        self.surface = pygame.Surface((2*w,2*h), pygame.SRCALPHA)
        self.surface.fill(pygame.Color('#77777722'))

        start_angle = self.dct['end_angle']*pi/180
        end_angle = self.dct['start_angle']*pi/180
        if start_angle > end_angle :
            start_angle ,end_angle = end_angle, start_angle

        pygame.draw.arc(self.surface,
                        self.dct['color'],
                        rect,
                        start_angle,
                        end_angle,
                        self.dct['thickness'])

        self.mask = pygame.mask.from_surface(self.surface)

