#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#import pygame
#import pygame_gui

from drawingclasses import GRAPH_LIST,\
                           LuaBarGraph,\
                           LuaRingGraph,\
                           LuaStaticText,\
                           LuaLineGraph,\
                           LuaRing,\
                           LuaEllipse,\
                           LuaEllipseGraph,\
                           LuaVariableText


class LuaDrawings :
    """ Save all drawings in a list """
    def __init__(self, draw_area) :
        self.draw_area = draw_area
        self.liste = []

        self.buf = NewObjectBuffer()

        self.an_object_is_moving = False

        self.selected_item = 0

    def create_from_dct(self, dct, name) :

        #print('creating form dict')
        #print(dct['kind'])

        kind = dct['kind']#[1:-1]
        #print(kind)
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
        elif kind ==  'line' :
            drawing = LuaLineGraph(self.draw_area)
        elif kind ==  'static_text' :
            #print('mlmlmlml')
            drawing = LuaStaticText(self.draw_area)

        drawing.name = name
        drawing.dct = dct
        self.liste.append(drawing)

    def create(self, kind) :
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
            drawing = LuaLineGraph(self.draw_area)
        elif kind ==  "static_text" :
            drawing = LuaStaticText(self.draw_area)

        self.buf.set_drawing(drawing)

    def draw_from_buffer(self) :
        #drawing = self.buf.drawing
        #drawing.draw(self.buf.inputs_pos)
        self.buf.draw()
        self.liste.append(self.buf.drawing)
        self.buf.clear()

    def preview_from_buffer(self, mouse_pos) :

        self.buf.draw(mouse_pos)

    def get_dict_from_name(self, name) :
        for i, drawing in enumerate(self.liste) :
            if drawing.name == name :
                self.selected_item = i
                return drawing.get_lua_dct()

    def rename_draw(self, new_name) :

        self.liste[self.selected_item] = new_name

#        return self.liste[0].name


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
        if self.input_remaning == 2 :
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

