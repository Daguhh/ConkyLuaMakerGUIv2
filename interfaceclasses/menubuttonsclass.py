#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from .interface_object_position import *

class MenuButtons :
    def __init__(self, manager) :

        self.manager = manager

        menu = pygame_gui.elements.UIButton(
            relative_rect=MB_MENU_RECT,
            text="",#text="Menu",
            manager=self.manager)

        gen = pygame_gui.elements.UIButton(
            relative_rect=MB_GEN_RECT,
            text="Generate luaconf",
            manager=self.manager,
            tool_tip_text = "Generate conky_draw_config.lua"
            "this file can be next reloaded with the 'load button'")

        save = pygame_gui.elements.UIButton(
            relative_rect=MB_SAVE_RECT,
            text="",#text="Save as",
            manager=self.manager)

        load = pygame_gui.elements.UIButton(
            relative_rect=MB_LOAD_RECT,
            text="Load config",
            manager=self.manager,
            tool_tip_text = "load the 'conky_draw_config.lua' file")

        aide = pygame_gui.elements.UIButton(
            relative_rect=MB_HELP_RECT,
            text="?",
            manager=self.manager,
            tool_tip_text = 'display help')

        self.buttons = [menu, gen, save, load, aide]

    def execute(self, ui_element, draw_lst) :
        #print("ohoh")
        ind = self.buttons.index(ui_element)

        if ind == 0 :
            self.menu()
        elif ind == 1 :
            self.gen_luaconf(draw_lst)
        elif ind == 2 :
            self.save2pkl()
        elif ind == 3 :
            self.load()
        elif ind == 4 :
            self.show_help()
        elif ind == 5 :
            pass

    def menu(self):
        pass

    def gen_luaconf(self, draw_lst):
        text="elements = {\n"
        for draw in draw_lst :
            text += '-- {}\n'.format(draw.name)
            text += '{\n'
            dct = pil2lua_dct(draw.dct, draw.pos)
            for k,v in dct.items() :
                text += "{} = {},\n".format(k,v)
            text += "},\n"
        text = text[:-4]
        text += "\n}\n}"
        with open("conky_draw_config.lua", 'w') as f :
            f.write(text)

    def save2pkl(self):
        pass

    def load(self):
        with open("conky_draw_config.lua", 'r') as f :
            text = f.read()

        text = text.split('{\n-- ',1)[1]
        text = text[::-1].split('}\n}\n,',1)[1][::-1]

        text = text.split(',\n},\n--')

        dct_list = []
        name_list = []
        for element in text :

            name, dct_text = element.split('\n{\n')
            dct_lignes = dct_text.split(',\n')
            dct = {}
            for ligne in dct_lignes :
                temp = ligne.split(' = ')
                k, v = temp
                dct[k] = v
            dct_list.append(lua2pil_dct(dct,(0,0)))
            name_list.append(name)

        return dct_list, name_list

    def show_help(self):
        pass


