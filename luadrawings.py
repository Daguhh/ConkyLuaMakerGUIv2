#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#import pygame
#import pygame_gui

from drawingclasses import GRAPH_LIST,\
                           LuaBarGraph,\
                           LuaRingGraph,\
                           LuaStaticText,\
                           LuaLine,\
                           LuaRing,\
                           LuaEllipse,\
                           LuaEllipseGraph,\
                           LuaVariableText


class LuaDrawings :
    """ Save all drawings in a list """
    def __init__(self, draw_area) :
        self.draw_area = draw_area
        #self.liste = []

        self.buf = NewObjectBuffer()

        self.an_object_is_moving = False
        self.an_object_is_resizing = False

        self._selected_item_ID = 0

        self.objects = {}

        self.id_gen = self.gen_id()

    @property
    def selected_draw(self) :
        return self.objects[self._selected_item_ID]

    @property
    def selected_item_ID(self) :
        return self._selected_item_ID

    @selected_item_ID.setter
    def selected_item_ID(self, ID) :
        print('--------------- SETTING ID------------------------')
        print('id = ',ID)
        self._selected_item_ID = ID

    def _get_draw_class(self, kind) :

        if kind == 'ring_graph' :
            drawing = LuaRingGraph(self.draw_area)
        elif kind == 'ellipse_graph' :
            drawing = LuaEllipseGraph(self.draw_area)
        elif kind == 'bar_graph' :
            drawing = LuaBarGraph(self.draw_area)
        elif kind == 'variable_text' :
            drawing = LuaVariableText(self.draw_area)
        elif kind == 'ring' :
            drawing = LuaRing(self.draw_area)
        elif kind == 'ellipse' :
            drawing = LuaEllipse(self.draw_area)
        elif kind ==  "line" :
            drawing = LuaLine(self.draw_area)
        elif kind ==  "static_text" :
            drawing = LuaStaticText(self.draw_area)

        return drawing

    def create_from_dct(self, dct, name) :

        kind = dct['kind']#[1:-1]
        drawing = self._get_draw_class(kind)
        drawing.dct = dct

        self.objects[name] = drawing

    def create(self, kind) :

        drawing = self._get_draw_class(kind)

        self.buf.set_drawing(drawing)

    def draw_from_buffer(self) :

        self.buf.draw()
        name = self.buf.drawing.dct['kind'] + self.id_gen.__next__()
        self.objects[name] = self.buf.drawing
        self.buf.clear()
        self.selected_item_ID = name

    def preview_from_buffer(self, mouse_pos) :

        self.buf.draw(mouse_pos)

    def get_dict_from_name(self, item_name) :
        for name, drawing in enumerate(self.objects) :
            if name == item_name :
                self.selected_item = name
                return drawing.get_lua_dct()

    def rename_draw(self, new_ID) :

        self.objects[new_ID] = self.objects.pop(self.selected_item_ID)
        self.selected_item_ID = new_ID

    def delete_selected_item(self) :

        del(self.objects[self.selected_item_ID])
        try :
            self.selected_item_ID = list(self.objects.keys())[-1]
        except :
            print("no drawings to select")
            self.selected_item_ID = 0

    def gen_id(self) :
        i = 0
        while True :
            i += 1
            yield '_#{}'.format(i)


class NewObjectBuffer :
    def __init__(self) :
        self.waiting_inputs = False
        self.input_remaning = 0
        self.inputs_pos = []
        self.drawing = None

    def set_drawing(self, drawing) :

        self.drawing = drawing
        self.waiting_inputs = True
        self.input_remaning = drawing.input_remaning

    def add_input(self, pos) :
        self.input_remaning -=1
        self.inputs_pos.append(pos)
        if self.input_remaning == 0 :
            self.waiting_inputs = False

    def draw(self, mouse_pos=(0,0)) :

        #if not self.inputs_pos == 0 :
        if self.input_remaning >= 2 :
            pass
        elif self.input_remaning == 1 :
            fake_inputs = self.inputs_pos.copy()
            fake_inputs.append(mouse_pos)
            #print('fake : ',fake_inputs)
            self.drawing.draw(fake_inputs)
        else :
            self.drawing.draw(self.inputs_pos)

    def is_empty(self) :
        if self.waiting_inputs == False and self.inputs_pos :
            return False
        else :
            return True

    def clear(self) :
        self.waiting_inputs = False
        self.input_remaning = 0
        self.inputs_pos = []
        self.drawing = None

