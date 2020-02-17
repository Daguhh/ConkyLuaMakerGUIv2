#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui

from .vectproduct import vect_product, tup_norm, tup_sum, tup_dif, tup_tim, tup_max, tup_min
from .parse_dct import lua2pil_dct, pil2lua_dct

from .luagraph import LuaGraph

class LuaBarGraph(LuaGraph):

    def __init__ (self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.name = "bar_graph"

        self.input_remaning = 2
        self.grid_step = 1

        self.mod_resize = "to"
        self.mod_thickness = "bar_thickness"

        self.dct = {"kind" : 'bar_graph',
                    "from" : (0,0),
                    "to" : (1,1),
                    "conky_value" : 'cpu cpu0',
                    "max_value" : 100,
                    "critical_threshold" : 90,
                    "background_color" : (0,0,0),
                    "background_alpha" : 1,
                    "background_thickness": 8,
                    "bar_color": (0,0,0),
                    "bar_alpha" : 1,
                    "change_thickness_on_critical" : False,
                    "bar_thickness": 15,
                    "change_color_on_critical" : False,
                    "background_color_critical" : (0,0,0),
                    "change_alpha_on_critical" : False,
                    "background_alpha_critical" : 1,
                    "background_thickness_critical" : 8,
                    "bar_color_critical" : (0,0,0),
                    "bar_alpha_critical" : 1,
                    "bar_thickness_critical" : 10,
                    "graduated" : False,
                    "number_graduation" : 10,
                    "space_between_graduation" : 2}


    def draw(self, positions) :

        self.dct['from'] = positions[0]
        self.dct['to'] = positions[1]

        h = self.dct['bar_thickness']/2
        f = self.dct['from']
        t = self.dct['to']
        p = (0,0)
        of = self.dct['bar_thickness']*1


        f = tup_sum(f,p)
        t = tup_sum(t,p)

        p = (min(f[0], t[0]), min(f[1],t[1]))
        f = (f[0] - p[0] + of, f[1] - p[1] + of)
        t = (t[0] - p[0] + of, t[1] - p[1] + of)

        self.pos = (p[0]-of, p[1]-of)
        self.dct['from'] = f
        self.dct['to']  = t

    def update(self) :

        h = self.dct['bar_thickness']/2
        f = self.dct['from']
        t = self.dct['to']
        p = self.pos
        of = self.dct['bar_thickness']*1

        f = tup_sum(f,p)
        t = tup_sum(t,p)

        g = self.grid_step
        f = (f[0]//g*g, f[1]//g*g)
        t = (t[0]//g*g, t[1]//g*g)

        p = (min(f[0], t[0]), min(f[1],t[1]))
        f = (f[0] - p[0] + of, f[1] - p[1] + of)
        t = (t[0] - p[0] + of, t[1] - p[1] + of)

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

        rect = tup_max(poly)

        self.surface = pygame.Surface(rect, pygame.SRCALPHA)
        self.surface.fill(pygame.Color('#77777720'))
        self.shape = pygame.draw.polygon(self.surface,
                                      self.dct['bar_color'],
                                      poly)
        self.mask = pygame.mask.from_surface(self.surface)

    def resize(self, new_mouse_pos) :

        if self.dct['from'] != tup_dif(new_mouse_pos,self.pos) :
#            print('choose a non-zero value for line size')
#        else :
            self.dct['to'] = tup_dif(new_mouse_pos,self.pos)
