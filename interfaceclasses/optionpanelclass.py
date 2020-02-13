#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from .interface_object_position import *

class OptionPanel:
    def __init__(self, manager, window_surface):
        self.manager = manager
        self.parent = window_surface

        # box paramters :
        box_height = OP_BOX_HEIGHT
        box_number = OP_BOX_NUMBER
        self.box_number = box_number

        box_label_pos = [(1, 1+(box_height+1) * n) for n in range(box_number)]
        box_label_width = OP_LABEL_BOX_WIDTH
        box_label_rects = [(pos, (box_label_width, box_height)) for pos in box_label_pos]

        box_entry_pos = [(box_label_width, (box_height+1) * n-2) for n in range(box_number)]
        box_entry_width = OP_ENTRY_BOX_WIDTH
        box_entry_rects = [(pos, (box_entry_width, box_height)) for pos in box_entry_pos]

        # box cpntainer
        self.pos = OP_PANEL_POS
        rect_size = (box_label_width + box_entry_width,
                     (box_height+1) * box_number)

        self.surface = pygame.Surface(rect_size)
        self.surface.fill(OP_PANEL_BACKGROUND_COLOR)
        rect = pygame.Rect(self.pos,rect_size)
        container = pygame_gui.core.ui_container.UIContainer(
                                                 rect,
                                                 manager)
        self.labels = []
        for i, rect in enumerate(box_label_rects) :
            new_label = pygame_gui.elements.UILabel(
                relative_rect = pygame.Rect(rect),
                text=str(i),
                manager = manager,
                container = container,
                object_id='label_test')
            self.labels.append(new_label)

        self.entrys = []
        for i, rect in enumerate(box_entry_rects) :
            new_entry = pygame_gui.elements.UITextEntryLine(
                relative_rect = pygame.Rect(rect),
                manager = manager,
                container = container,
                object_id='label_test')
            self.entrys.append(new_entry)

    def update_position(self, dct) :

        name = [b.text for b in self.labels]
        position_keys = ["center","from","to"]

        for key in position_keys :
            if key in dct :
                ind = name.index(key)
                self.entrys[ind].set_text(str(dct[key]))

    def update_size(self, dct) :

        name = [b.text for b in self.labels]
        position_keys = ["width","height","radius"]

        for key in position_keys :
            if key in dct :
                ind = name.index(key)
                self.entrys[ind].set_text(str(dct[key]))

    def update_lua_dct(self, dct) :

        #print('update!!!!!!!!!!!!!!!!')

        nb_box = range(self.box_number)
        temp = zip(nb_box, self.labels, self.entrys)
        for i, label, entry in temp:
            label.set_text("")
            entry.set_text("")

        temp = zip(list(dct.keys()),self.labels)
        for k, label in temp :
            label.set_text(k)

        temp = zip(list(dct.values()),self.entrys)
        for v, entry in temp :
            entry.set_text(str(v))

    def get_new_entry(self, element) :

        ind = self.entrys.index(element)

        name = self.labels[ind].text
        value = self.entrys[ind].get_text()

        return name, value

    def blit(self) :

        self.parent.blit(self.surface, self.pos)

