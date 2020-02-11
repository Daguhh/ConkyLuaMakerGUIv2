#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from .interface_object_position import *

class PreviewPanel:
    def __init__(self, window_surface, manager) :

        self.parent = window_surface
        self.size = PP_SIZE
        self.color = PP_COLOR
        self.pos = PP_POS
        self.grid_size = 20

        self.background = pygame.Surface(self.size, pygame.SRCALPHA)
        self.background.fill(self.color)

        self.rect = self.background.get_rect(topleft=self.pos)

        self._mouse_pos = self.pos
        rect = MP_RECT
        self.mouse_label=pygame_gui.elements.UILabel(
                relative_rect = rect,
                text="mouse_pos",
                manager = manager)

        rect = pygame.Rect((208,610),(300,20))
        self.grid_step_slider = pygame_gui.elements.UIHorizontalSlider(
                rect,
                self.grid_size,
                (1,60),
                manager)

        rect = pygame.Rect((208,630),(300,20))
        self.grid_step_label=pygame_gui.elements.UILabel(
                relative_rect = rect,
                text=str(int(self.grid_step_slider.get_current_value())),
                manager = manager)

        #self.show_grid()

    def set_grid_size(self, grid_size) :

        self.grid_step_slider.current_value=grid_size
        self.grid_step_label.set_text(str(grid_size))

    @property
    def grid_size_as_changed(self) :
        if self.prev_size != self.grid_size :
            self.prev_size == self.grid_size
            return True
        else :
            return False

    def show_grid(self) :
        self.grid_size = int(self.grid_step_slider.get_current_value())

        if self.grid_size >= 2 :

            color = (50,50,50)
            for step in range(0,self.size[0],self.grid_size) :

                pygame.draw.line(self.background,
                                color,
                                (step,0),
                                (step,self.size[0]),
                                1)

            for step in range(0,self.size[1],self.grid_size) :

                pygame.draw.line(self.background,
                                color,
                                (0,step),
                                (self.size[0], step),
                                1)

    @property
    def mouse_pos(self) :
        return self._mouse_pos

    @mouse_pos.setter
    def mouse_pos(self, pos) :
        step = int(self.grid_step_slider.get_current_value())
        self._mouse_pos = ((pos[0] - self.pos[0])//step*step,
                           (pos[1] - self.pos[1])//step*step)
        self.mouse_label.set_text('mouse position = {}'.format(self._mouse_pos))
        #print(self._mouse_pos)

    def blit(self) :

        self.show_grid()
        self.grid_step_label.set_text(str(int(self.grid_step_slider.get_current_value()))),
        self.parent.blit(self.background, self.pos)

    def clear(self) :

        self.background.fill(self.color)
