#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui

from vectproduct import vect_product, tup_norm, tup_sum, tup_dif, tup_tim
from .parse_dct import lua2pil_dct, pil2lua_dct
from .luagraph import LuaGraph


class LuaLineGraph(LuaGraph):

    def __init__ (self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.name = "line"
        self.grid_step = 1

        self.input_remaning = 2

        self.dct = {"kind" : 'line',
                    "from" : (0,0),
                    "to" : (1,1),
                    "color" : (255,255,255),
                    "alpha" : 1,
                    "thickness" : 10,
                    "graduated" : False,
                    "number_graduation" : 10,
                    "space_between_graduation" : 1}

    def draw(self, positions) :

        self.dct['from'] = positions[0]
        self.dct['to'] = positions[1]

        h = self.dct['thickness']/2
        f = self.dct['from']
        t = self.dct['to']
        p = (0,0)
        of = self.dct['thickness']*1

        f = tup_sum(f,p)
        t = tup_sum(t,p)

        p = (min(f[0], t[0]), min(f[1],t[1]))
        f = (f[0] - p[0] + of, f[1] - p[1] + of)
        t = (t[0] - p[0] + of, t[1] - p[1] + of)

        rect = (max(f[0],t[0])+2*of,
                max(f[1],t[1])+2*of)

        self.pos = (p[0]-of, p[1]-of)
        self.dct['from'] = f
        self.dct['to']  = t

    def update(self) :

        h = self.dct['thickness']/2
        f = self.dct['from']
        t = self.dct['to']
        p = self.pos
        of = self.dct['thickness']*1

        f = tup_sum(f,p)
        t = tup_sum(t,p)

        g = self.grid_step
        f = (f[0]//g*g, f[1]//g*g)
        t = (t[0]//g*g, t[1]//g*g)

        p = (min(f[0], t[0]), min(f[1],t[1]))
        f = (f[0] - p[0] + of, f[1] - p[1] + of)
        t = (t[0] - p[0] + of, t[1] - p[1] + of)

        rect = (max(f[0],t[0])+2*of,
                max(f[1],t[1])+2*of)

        self.pos = (p[0]-of, p[1]-of)
        self.dct['from'] = f
        self.dct['to']  = t

        dif = tup_dif(t,f)
        norm = tup_norm(dif)
        ratio = h/norm
        w_p = tup_tim(ratio , vect_product((dif[0],dif[1],0), (0,0,1)))
        w_m = tup_tim(ratio , vect_product((dif[0],dif[1],0), (0,0,-1)))

        poly = (tup_sum(f,w_m),
                tup_sum(f,w_p),
                tup_sum(t,w_p),
                tup_sum(t,w_m))

        self.surface = pygame.Surface(rect, pygame.SRCALPHA)
        self.surface.fill(pygame.Color('#77777720'))
        #self.parent.fill(pygame.Color('#77777777'))
        self.shape = pygame.draw.polygon(self.surface,
                                      self.dct['color'],
                                      poly)
        self.mask = pygame.mask.from_surface(self.surface)

