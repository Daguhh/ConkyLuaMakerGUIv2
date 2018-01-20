#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import numpy as np
import matplotlib.patches as patches
from LuaObjectClass.unformat_functions import unformat_xy, unformat_color, unformat_font

class LUAStaticText :
    
    def __init__ (self, ax) :
        
        self.kind = "static_text"
        self.name = "static_text"
        self.ax = ax
        self.graph = []
        self.properties = []
        self.properties_name = []
    
        self.create_properties()
        self.nb_input = 1
        
        self.press=None
    
    def connect(self):
        
        'connect to all the events we need'
        self.cidpress = self.graph.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.graph.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.graph.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)
        
    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.graph.axes: return
        
        contains, attrd = self.graph.contains(event)
        if not contains: return
        x0, y0 = self.graph.xy
        self.press = x0, y0, event.xdata, event.ydata
        
    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.graph.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        
        x = int(x0+dx)
        y = int(y0+dy)
        
        self.graph.set_x(x)
        self.graph.set_y(y)
        self.properties[0] = ("{}x={}, y={}{}".format('{',x,y,'}'))
        self.graph.figure.canvas.draw()

    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.graph.figure.canvas.draw()
        
        
    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


    def create_graph(self, x, y) :
        fro =  ("{}x={}, y={}{}".format('{',x[0],y[0],'}'))
        self.properties[0] = fro
        self.make_graph()
  
    def make_graph(self) :
        P = self.properties
        
        fro      = unformat_xy(P[0])
        text     = P[1]
        color    = unformat_color(P[2])
        rotation = 360-int(P[3])
        font     = unformat_font(P[4])
        fontsize = P[5]
#        bold     = P[6]
#        italic   = P[7]
#        alpha    = float(P[8])
        
        self.graph = self.ax.annotate(s = text, 
                                           xy = fro , 
                                           color = color, 
                                           fontsize = fontsize, 
                                           rotation = rotation,
                                           name = font)
#                                           weight = bold,
#                                           style = italic,
#                                           alpha = alpha)
        self.connect()
        
    def create_properties(self) :
        text = "'default text'"
        fro = 0
        text = "'default text'"
        color="0xFFFFFF"
        rotation = 0
        font = "'DejaVu Sans'"
        fontsize = 8
        bold = "normal"
        italic = "normal"
        alpha = 1
        self.properties_name=["from",
                              "text",
                              "color",
                              "rotation_angle",
                              "font",
                              "fontsize"]
#                              "bold",
#                              "italic",
#                              "alpha"]
        self.properties=[fro,
                         text,
                         color,
                         rotation,
                         font,
                         fontsize]
#                         bold,
#                         italic,
#                         alpha]
        
    def generate(self) :
        
        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf
