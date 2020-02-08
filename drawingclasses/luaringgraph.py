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

class LuaRingGraph(LuaGraph):
    def __init__(self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 10
        self.name = "ring_graph"

        self.input_remaning = 2

        self.dct = {
            "kind" : 'ring_graph',
            "center" : (0,0),
            "radius" : 1,
            "conky_value" : 'fs_used_perc /home/',
            "max_value" : 100,
            "critical_threshold" : 90,
            "bar_color" : (22,255,255),
            "bar_alpha" : 1,
            "bar_thickness" : 8,
            "background_color" : (255,255,255),
            "background_alpha" : 1,
            "background_thickness" : 8,
            "change_color_on_critical" : False,
            "change_alpha_on_critical" : False,
            "change_thickness_on_critical" : False,
            "background_color_critical" : (0,0,0),
            "background_alpha_critical" : 1,
            "background_thickness_critical" :8,
            "bar_color_critical" : (0,0,0),
            "bar_alpha_critical" : 1,
            "bar_thickness_critical" : 8,
            "start_angle" : 360,
            "end_angle" : 0,
            "graduated" : False,
            "number_graduation" : 10,
            "angle_between_graduation" : 10
        }

    def draw(self, positions) :
        center = positions[0]
        to = positions[1]
        r = int(((center[0]-to[0])**2 + (center[1]-to[1])**2)**0.5)
        self.pos = (center[0]-r, center[1]-r)
        center = (r,r)

        self.dct['center'] = center
        self.dct['radius'] = r


    def update(self) :

        c = self.dct['center']
        r = self.dct['radius']
        p = self.pos

        c = tup_sum(c,p)
        g = self.grid_step
        c = (c[0]//g*g, c[1]//g*g)
        self.pos = tup_dif(c,(r,r))
        c = (r,r)
        self.dct['center'] = c

        rect = pygame.Rect((0,0),(2*r,2*r))
        self.surface = pygame.Surface((2*r,2*r), pygame.SRCALPHA)
        #self.shape = pygame.draw.arc(self.surface,
#        self.surface.fill(pygame.Color('#77777720'))

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

