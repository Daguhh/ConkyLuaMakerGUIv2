#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:15:30 2018

@author: david
"""

from LuaObjectClass import LUARingGraph, LUABarGraph, LUAStaticText, LUAVariableText, LUALine, LUAElipsGraph, LUAElips, LUARing



class OptionPanelFunction :
    
    def __init__(self) :
        pass
    
    def draw_lua_object(self, kind) :
        
        # create and append a new object to the object list
        # and wait for user to select point(s) on figure, their number depending on the nb_input necessary to draw figure
        if kind == "static_text" :
            self.Out.list_obj.append(  LUAStaticText(  self.Out.Fig.ab) )
        elif kind == "variable_text" :
            self.Out.list_obj.append(  LUAVariableText(self.Out.Fig.ab) )
        elif kind == "ring_graph" :
            self.Out.list_obj.append(  LUARingGraph(   self.Out.Fig.ab) )
        elif kind == "ellipse_graph" :
            self.Out.list_obj.append(  LUAElipsGraph(  self.Out.Fig.ab) )
        elif kind == "bar_graph" :
            self.Out.list_obj.append(  LUABarGraph(    self.Out.Fig.ab) )
        elif kind == "line" :
            self.Out.list_obj.append(  LUALine(        self.Out.Fig.ab) )
        elif kind == "ellipse" :
            self.Out.list_obj.append(  LUAElips(        self.Out.Fig.ab) )
        elif kind == "ring" :
            self.Out.list_obj.append(  LUARing(        self.Out.Fig.ab) )

        # initiate and reset graph point values
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        
        # refresh object list frame
        self.Out.Obj.refresh()
        
        
        