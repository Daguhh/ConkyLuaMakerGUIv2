#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui
from math import pi


from .parse_dct import lua2pil_dct, pil2lua_dct
from .vectproduct import vect_product, tup_norm, tup_sum, tup_dif, tup_tim

from .luagraph import LuaGraph


class LuaEllipseGraph(LuaGraph) :
    def __init__(self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 1

        self.name = "ellipse_graph"

        self.input_remaning = 2

        self.dct = {
            "kind" : 'ellipse_graph',
            "center" : (0,0),
            "radius" : 10,
            "conky_value" : 'cpu cpu0',
            "width" : 1,
            "height" : 1,
            "max_value" : 100,
            "critical_threshold": 90,
            "background_color" : (255,255,255),
            "background_alpha" : 1,
            "background_thickness" : 8,
            "bar_color" : (255,255,255),
            "bar_alpha" : 1,
            "bar_thickness" : 8,
            "change_color_on_critical" : False,
            "change_alpha_on_critical" : False ,
            "change_thickness_on_critical" : False,
            "background_color_critical" : (255,255,255),
            "background_alpha_critical" : 1,
            "background_thickness_critical" : 10,
            "bar_color_critical" : (255,255,255),
            "bar_alpha_critical" : 1,
            "bar_thickness_critical" : 10,
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

        self.pos = (c[0]-r, c[1]-r)
        c = (r,r)

        self.dct['center'] = c
        self.dct['radius'] = r
        self.dct['width'] = r
        self.dct['height'] = r

    def update(self) :

        c = self.dct['center']
        p = self.pos

        w = self.dct['width'] + self.dct['bar_thickness']/2
        h = self.dct['height'] + self.dct['bar_thickness']/2

        c = tup_sum(c,p)
        g = self.grid_step
        c = (c[0]//g*g, c[1]//g*g)
        p = tup_dif(c,(w,h))
        self.pos = (int(p[0]), int(p[1]))
        c = (w,h)
        self.dct['center'] = c

        rect = pygame.Rect((0,0),(2*w,2*h))
        self.surface = pygame.Surface((2*w,2*h), pygame.SRCALPHA)

        start_angle = self.dct['end_angle']*pi/180
        end_angle = self.dct['start_angle']*pi/180
        if start_angle > end_angle :
            start_angle ,end_angle = end_angle, start_angle

        pygame.draw.arc(self.surface,
                        self.dct['bar_color'],
                        rect,
                        start_angle,
                        end_angle,
                        self.dct['bar_thickness'])

        self.mask = pygame.mask.from_surface(self.surface)

