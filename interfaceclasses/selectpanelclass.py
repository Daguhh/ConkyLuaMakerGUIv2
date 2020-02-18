#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from .interface_object_position import *

class SelectPanel:
    def __init__(self, manager, window_surface) :

        self.manager = manager
        self.parent = window_surface
        self.drawing_name_list = ["select item"]

        self.current_selection = "select item"
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            self.drawing_name_list,
            self.current_selection,
            SP_DROPDOWN_RECT,
            manager = self.manager)

        self.new_name_entry_box = pygame_gui.elements.UITextEntryLine(
            relative_rect = SP_RENAME_BOX_RECT,
            manager = self.manager)#,
        self.new_name_entry_box.set_text("Enter new name")

        self.delete_button = pygame_gui.elements.UIButton(
                        relative_rect = SP_DELETE_BUTTON_RECT,
                        text="Del",
                        manager=self.manager)
                        #object_id='button_theme')

    def delete(self, ID) :

        self.current_selection = ID
        self.drawing_name_list.remove(ID)
        self._update_list()

    def rename(self, old_ID) :

        new_ID =  self.new_name_entry_box.get_text()
        self.current_selection = new_ID
        self.drawing_name_list[self.drawing_name_list.index(old_ID)] = new_ID
        self._update_list()
        self.new_name_entry_box.set_text("Rename")

        return new_ID

    def add_item_to_list(self, new_ID) :

        self.current_selection = new_ID
        self.drawing_name_list.append(new_ID)
        self._update_list()


    def _update_list(self) :

        self.dropdown.kill()
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            self.drawing_name_list,
            self.current_selection,
            SP_DROPDOWN_RECT,
            self.manager)

    def update_list(self, liste) :
        print('use old_list')

        self.dropdown.kill()
        self.drawing_name_list = liste
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            self.drawing_name_list,
            self.current_selection,
            SP_DROPDOWN_RECT,
            self.manager)

    def get_select_item(self):

        select = self.dropdown.selected_option
        self.current_selection = select
        return select

    def set_select_item(self, draw_name) :
        self.current_selection = draw_name
        self.update_list(self.drawing_name_list)

    def blit(self) :
        self.parent.blit(self.surface, self.pos)
