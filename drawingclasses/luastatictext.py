#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import pygame
import pygame_gui

from math import pi, sin, cos
from .math_tool import rotation_transformation as rot

from .vectproduct import vect_product, tup_norm, tup_sum, tup_dif, tup_tim
from .parse_dct import lua2pil_dct, pil2lua_dct
from .luagraph import LuaGraph


class LuaStaticText(LuaGraph) :

    def __init__ (self, draw_area) :

        LuaGraph.__init__(self)

        self.draw_area = draw_area
        self.grid_step = 1

        self.name = "static_text"

        self.input_remaning = 1
        self.text_h = 0

        self.dct = {
            "kind" : 'static_text',
            "from" : (0,0),
            "text": 'default',
            "color" : (0,0,0),
            "rotation_angle" : 0,
            "font_size" : 12,
            "font" : 'Comic Sans MS',
            "bold" : False,
            "italic" : False,
            "alpha" : 1}

    def draw(self, position) :

        g = self.grid_step
        self.pos = (position[0][0]//g*g,
                    position[0][1]//g*g)

        self.myfont = pygame.font.SysFont(self.dct['font'],
                                     self.dct['font_size'])
        textsurface = self.myfont.render(self.dct['text'],
                                    False,
                                    self.dct['color'])

        _, h = textsurface.get_size()
        p = tup_sum(self.pos,(0,-h))

        self.dct['from'] = (0,h)
        self.pos = [int(p[0]), int(p[1])]

    def update(self) :

        p = tup_sum(self.pos, self.dct['from'])
        g = self.grid_step
        p = (int(p[0])//g*g, int(p[1])//g*g)
        self.myfont = pygame.font.SysFont(self.dct['font'],
                                     self.dct['font_size'])
        textsurface = self.myfont.render(self.dct['text'],
                                    False,
                                    self.dct['color'])
        #textsurface.fill(pygame.Color('#7777770f'))
        self.surface = pygame.transform.rotate(textsurface,
                                                self.dct['rotation_angle'])
        #self.surface = self.surface.convert_alpha()
        self.mask = pygame.mask.from_surface(self.surface)

        A = self.dct['rotation_angle']
        tw, th = textsurface.get_size()
        sw, sh = self.surface.get_size()

        if A >= 270 :
            x,_ = rot((0,th*(1-0.8)), A)
            _,y = rot((0,th*0.8), A)
        elif A >= 180 and A < 270 :
            x1,_ = rot((0,th*0.8),A)
            x = -(sw + x1)
            y = 0
        elif A >= 90 and A < 180 :
            x = -sw
            _,y1 = rot((0,th*0.8), A)
            y = + (sh + y1)
        elif A < 90 :
            x,_ = rot((0,th),A)
            x = -x
            y = sh

        x, y = int(x) , int(y)
        #print(g)
        #x = x//g*g
        #y = y//g*g

        self.dct['from'] = (-x,y)
        p = tup_sum(p,(x,-y))
        #print(p)
        #print(-x,y)
        self.pos = [int(p[0]), int(p[1])]

