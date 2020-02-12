#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from .interface_object_position import *

class MenuButtons :#(ConkyLuaMaker_HelpClass) :
    def __init__(self, manager) :

 #       ConkyLuaMaker_HelpClass.__init__(self)

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

        self.help_text = {"test" : "yghvighighlgihlgfvgbggggg",
                          "actually_link" : "youpi"}

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


#class ConkyLuaMaker_HelpClass:

#    def __init__(self):
#        pass

    def display_help(self):

        self.help_box = pygame_gui.windows.UIMessageWindow(pygame.Rect((500,100),(400, 350)),
                        'Welcome to ConkyLuaMakerGUI',
                        '<font color=normal_text>'
                        '<a href="get_started">Get started</a><br>'
                        '<a href="shortcuts">Shortcuts</a><br>',
                        self.manager)

        self.help_dct = {"back" : '<br>'
                        '<a href="get_started">Get started</a><br>'
                        '<a href="shortcuts">Shortcuts</a><br>'
                        '<br>'
                        '<br>',
                        "get_started" : ''
                        '<a href="back">< Go back</a><br><br>'
                        ' 1) hit a button on left panel to initiate <a href="drawing"> drawing</a> creation<br>'
                        ' 2) interact with drawing area to place objects (1 or 2 left click)<br>'
                        ' 3) rename and edit <a href="select">selected</a> drawing properties on right panel (keybord inputs + enter<br>'
                        ' 4) generate lua conf with top buttons<br>'
                        '<br>'
                        '<br>',
                        "shortcuts" : ''
                        '<a href="back">< Go back</a><br><br>'
                        'You can interact with drawings in the center panel, try to hit it with left mouse button.<br>'
                        'Shortcuts : (no need to hold) <br><br>'
                        'left click =  select<br>'
                        'left click + left ctrl = move<br>'
                        'left click + left maj = resize<br>'
                        '<br>'
                        '<br>',
                         "select" : ''
                        '<a href="back">< Go back</a><br><br>'
                         'ways to select an object :<br>'
                         '  - left mouse button<br>'
                         '  - drop-down panel<br>'
                         '  - newly created object will be selected automatically'
                        '<br>'
                        '<br>',
                        "drawing": ''
                        '<a href="back">< Go back</a><br><br>'
                        'there is 4 drawing types : <br>'
                         '  - ring <br>'
                         '  - ellipse <br>'
                         '  - bar <br>'
                         '  - text <br><br>'
                         'for each their is 2 version :<br>'
                         '  - graph : that can represent a conky value <br>'
                         '  - static : that is just cosmetics <br><br>'
                         'after you choose one drawing by hitting a button,'
                         'select area on the preview panel where you want to draw it :<br>'
                         '  - ring and ellipse : 1st hit = center<br>'
                         '                       2nd hit = radius<br>'
                         '  - bar : 2 hit = start, end<br>'
                         '  - text : 1 hit = left down corner text rectangle position'
                        }


    def display_link(self, name) :
        new_text = self.help_dct[name]
        self.help_box.text_block.html_text = new_text
        self.help_box.rebuild()
