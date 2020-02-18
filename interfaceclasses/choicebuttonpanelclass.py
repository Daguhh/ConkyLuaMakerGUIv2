#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from .interface_object_position import CBP_HEIGHT, CBP_WIDTH, CBP_OFFSET, CBP_SPACING


class ChoiceButtonPanel:
    def __init__(self, window_surface, manager):

        self.parent = window_surface
        self.manager = manager

        height = CBP_HEIGHT
        width = CBP_WIDTH
        offset = CBP_OFFSET
        spacing = CBP_SPACING

        self.buttons = []  # [circle, dot, bar, bar2, elips]

        button_pos = [(height + spacing) * i for i in range(len(GRAPH_LIST))]
        for i, pos in enumerate(button_pos):

            new_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10, pos + offset), (width, height)),
                text=GRAPH_LIST[i],
                manager=self.manager,
                object_id="button_theme",
            )
            self.buttons.append(new_button)

    def get_name(self, ui_element):
        ind = self.buttons.index(ui_element)
        return GRAPH_LIST[ind]
