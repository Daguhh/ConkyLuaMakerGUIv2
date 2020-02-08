#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pygame_gui

from drawingclasses import GRAPH_LIST
from drawingclasses import lua2pil_dct, pil2lua_dct

from interface_object_position import *

class ChoiceButtonPanel:
    def __init__(self, window_surface, manager) :

        self.parent = window_surface
        self.manager = manager

        height = CBP_HEIGHT
        width = CBP_WIDTH
        offset = CBP_OFFSET
        spacing = CBP_SPACING

        self.buttons = [] #[circle, dot, bar, bar2, elips]

        button_pos = [(height + spacing)*i for i in range(len(GRAPH_LIST))]
        for i, pos in enumerate (button_pos) :

            new_button = pygame_gui.elements.UIButton(
                         relative_rect=pygame.Rect((10, pos+offset), (width, height)),
                         text=GRAPH_LIST[i],
                         manager=self.manager,
                         object_id='button_theme')
            self.buttons.append(new_button)

    def get_name(self, ui_element) :
        ind = self.buttons.index(ui_element)
        return GRAPH_LIST[ind]

class PreviewPanel:
    def __init__(self, window_surface) :

        self.parent = window_surface
        self.size = PP_SIZE
        self.color = PP_COLOR
        self.pos = PP_POS

        self.background = pygame.Surface(self.size, pygame.SRCALPHA)
        self.background.fill(self.color)

        self.rect = self.background.get_rect(topleft=self.pos)

    def blit(self) :

        self.parent.blit(self.background, self.pos)

    def clear(self) :

        self.background.fill(self.color)


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

        self.is_on=pygame_gui.elements.UILabel(
                relative_rect = SP_LABEL_GRID_SIZE_RECT,
                text="grid size",
                manager = self.manager)

        self.grid_step_entry = pygame_gui.elements.UITextEntryLine(
                relative_rect = SP_ENTRY_GRID_SIZE_RECT,
                manager = self.manager)

    def update_list(self, liste) :

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

        buttons_name = [b.text for b in self.labels]
        if "center" in dct :
            ind = buttons_name.index("center")
            self.entrys[ind].set_text(dct["center"])
        if "from" in dct :
            ind = buttons_name.index("from")
            self.entrys[ind].set_text(dct["from"])
        if "to" in dct :
            ind = buttons_name.index("to")
            self.entrys[ind].set_text(dct["to"])

    def update_lua_dct(self, dct) :

        print('update!!!!!!!!!!!!!!!!')

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


class MousePosPanel:
    def __init__(self, manager):

        rect = MP_RECT
        self.label=pygame_gui.elements.UILabel(
                relative_rect = rect,
                text="mouse_pos",
                manager = manager)

#        rect = pygame.Rect((380,590),(120,25))
#        self.is_on=pygame_gui.elements.UILabel(
#                relative_rect = rect,
#                text="grid size",
#                manager = manager)
#
#        rect = pygame.Rect((500,590),(120,25))
#        self.grid_step_entry = pygame_gui.elements.UITextEntryLine(
#                relative_rect = pygame.Rect(rect),
#                manager = manager)
#
    def update(self,mouse_pos) :
        self.label.set_text('mouse position = {}'.format(mouse_pos))

    def show_is_on(self,on) :
        self.is_on.set_text(on)

