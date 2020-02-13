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

        dct_list = {}
        for element in text :

            name, dct_text = element.split('\n{\n')
            dct_lignes = dct_text.split(',\n')
            dct = {}
            for ligne in dct_lignes :
                temp = ligne.split(' = ')
                k, v = temp
                dct[k] = v
            dct_list[name] = lua2pil_dct(dct,(0,0))
            #dct_list.append(lua2pil_dct(dct,(0,0)))
            #name_list.append(name)

        return dct_list


#class ConkyLuaMaker_HelpClass:

#    def __init__(self):
#        pass

    def display_help(self):

        self.help_box = pygame_gui.windows.UIMessageWindow(pygame.Rect((500,100),(400, 350)),
                        'Welcome to ConkyLuaMakerGUI',
                        '<font color=normal_text>'
                        'Plan : <br>'
                        '<a href="get_started">Get started</a><br>'
                        '  <a href="drawing">Objects to draw</a><br>'
                        '  <a href="select"">Selecting object</a><br>'
                        '  <a href="inputs">Objects draw place</a><br>'
                        '<a href="interact">Interacting with draw</a><br>'
                        '  <a href="shortcuts">Shortcuts</a><br>'
                        '  <a href="slider">Grid size slider</a><br>'
                        '<br>'
                        '<br>',
                        self.manager)

        self.help_dct = {"first" : '<br>'
                                    'Plan : <br>'
                                    '<a href="get_started">Get started</a><br>'
                                    '  <a href="drawing">Objects to draw</a><br>'
                                    '  <a href="select"">Selecting object</a><br>'
                                    '  <a href="inputs">Objects draw place</a><br>'
                                    '<a href="interact">Interacting with draw </a><br>'
                                    '  <a href="shortcuts">Shortcuts</a><br>'
                                    '  <a href="slider">Grid size slider</a><br>'
                                    '<br>',
                         "get_started" : '<br>'
                                    '<a href="first">Go back</a><br><br>'
                                    ' 1) hit a button on left panel to initiate <a href="drawing"> drawing</a> creation<br>'
                                    ' 2) interact with drawing area to place objects (<a href="inputs">1 or 2 left click)</a><br>'
                                    ' 3) rename and edit <a href="select">selected</a> drawing properties on right panel (keybord inputs + enter<br>'
                                    ' 4) generate lua conf with top buttons<br>'
                                    '<br>'
                                    '<br>',
                         "interact" : ''
                                    '<a href="first">First page</a><br><br>'
                                    'You can <a href="shortcuts">interact</a>with the graph using mouse</a> '
                                    'to edit properties such as position, radius, '
                                    'direction, size<br>'
                                    'Objects are placed on a <a href="slider">"magnetic"</a> grid to help you '
                                    'align them more easily. '
                                    'You can change the grid size with the slider',
                         "slider" :''
                                    '<a href="first">First page</a><br>'
                                    '<a href="interact"> < Go back</a><br><br>'
                                    'the "magnetic" grid will force object to stick '
                                    'to grid line intersections. '
                                    'You can see this as if each grid square '
                                    'correspond to a unique position value '
                                    'which is the square top left corner absolute position.<br>'
                                    'Grid size is in fact an intrinsic propertie of each object. '
                                    'As object is created it store and use the value of previously set grid size '
                                    'and moving the slider will only affect the selected object. '
                                    'So if you reselect it after, grid size will return to the stored value by the object<br>'
                                    'Pay attention : changing grid size will probably affect the object placement',
                         "shortcuts" : ''
                                    '<a href="first">First page</a><br>'
                                    '<a href="interact">  Go back</a><br><br>'
                                    'hit, with left mouse button, object on preview area to start interacting<br><br>'
                                    'You can use those shortcuts :<br><br>'
                                    'left click =  select<br>'
                                    'left click + left ctrl = move<br>'
                                    'left click + left maj = resize<br><br>'
                                    '(no need to hold)'
                                    '<br>',
                          "select" : ''
                                    '<a href="first"><< First page</a>><br>'
                                    '<a href="get_started">< Go back</a><br><br>'
                                    'There is 3 ways to select an object :<br>'
                                    '   - select it\'s ID in dropdown menu (top-right)<br>'
                                    '   - left click on the object (preview area)<br>'
                                    '   - a newly created object will be selected automatically<br>'
                                    '<br>after selection property panel will update'
                                    '<br>',
                         "drawing": ''
                                    '<a href="first"><< First page</a><br><br>'
                                    '<a href="get_started">< Go back</a><br><br>'
                                    'there is 4 drawing types : <br>'
                                    '  - ring <br>'
                                    '  - ellipse <br>'
                                    '  - bar <br>'
                                    '  - text <br><br>'
                                    'for each their is 2 version :<br>'
                                    '  - graph : that can represent a conky value <br>'
                                    '  - static : that is just cosmetics <br><br>',
                         "inputs" : ''
                                    '<a href="first"><< First page</a><br><br>'
                                    '<a href="get_started">< Go back</a><br><br>'
                                    'Once you selected an object to create,'
                                    'interact with the previewpanel/draw area to'
                                    'to create it a the place you want :<br>'
                                    '  - ring and ellipse : 1st hit = center<br>'
                                    '                       2nd hit = radius<br>'
                                    '  - bar : 2 hit = start, end<br>'
                                    '  - text : 1 hit = left down corner text rectangle position'
                         }


    def display_link(self, name) :
        new_text = self.help_dct[name]
        self.help_box.text_block.html_text = new_text
        self.help_box.rebuild()
