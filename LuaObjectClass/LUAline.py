#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import numpy as np
import matplotlib.patches as patches
from .classproperties import Properties


class MovableObject() :
    def __init__(self) :
        self.press=None
        self.key_pressed = None
        
    def connect(self):

        'connect to all the events we need'
        self.cidkeypress = self.graph.figure.canvas.mpl_connect(
                'key_press_event', self.on_key_press)
        self.cidkeyrelease = self.graph.figure.canvas.mpl_connect(
                'key_release_event', self.on_key_release)
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
        
        if self.key_pressed == "shift" : # move
            new_pos = ("{}x={}, y={}{}".format('{',x,y,'}'))
            setattr(self.props, "fro", new_pos)
            
            self.graph.set_x(x)
            self.graph.set_y(y)
            
        elif self.key_pressed == "control" : # resize
            print("control")
            new_size = abs(int((-y+y0)))
            setattr(self.props, "height", new_size)
            self.graph.set_height(new_size)
            
        self.graph.figure.canvas.draw()

    def on_key_press(self, event) :
        self.key_pressed = event.key
        
    def on_key_release(self, event) :
        self.key_pressed = None

    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.graph.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
        self.rect.figure.canvas.mpl_disconnect(self.cidkeyrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidkeypress)
        
        
class LUALine(MovableObject) :

    def __init__ (self, ax) :
        self.ax = ax
        self.kind = "line"
        self.name = "line"
        self.graph = []

        self.nb_input = 2

        dct = {"fro" : "{x=0, y=0}",
               "to" : "{x=0, y=0}",
               "bar_color": "0x000000",
               "bar_alpha" : 1,
               "bar_thickness": 8,
               "graduated" : 1,
               "number_graduation" : 10,
               "space_between_graduation" : 1,
               }

        MovableObject.__init__(self)
        self.props = Properties(dct)

        self.properties_name = []
        for attribute, value in self.props.__dict__.items() :
            self.properties_name.append(attribute)


    def _set_properties(self, props) :
        for i, name in enumerate(self.properties_name) :
            print(name)
            setattr(self.props, name, props[i])

    def _get_properties(self) :
        props = []
        for name in (self.properties_name) :
            props.append(self.props.uformat(name))
        return props

    properties = property(_get_properties, _set_properties)


    def create_graph(self, x=[0,1], y=[0,1]) :
        self.props.fro = ("{}x={}, y={}{}".format('{',x[0],y[0],'}'))
        self.props.to  = ("{}x={}, y={}{}".format('{',x[1],y[1],'}'))
        self.make_graph()

    def make_graph(self) :

        tan = (self.props.to[1]-self.props.fro[1]) / \
              (self.props.to[0]-self.props.fro[0])
        angle = np.arctan(tan)*180/(np.pi) + \
                180 * ( (self.props.to[0]-self.props.fro[0])<0 )

        width = int(np.sqrt( (self.props.to[1]-self.props.fro[1])**2 + \
                             (self.props.to[0]-self.props.fro[0])**2 ) )

        self.graph = self.ax.add_patch(
            patches.Rectangle( xy     = self.props.fro,
                               width  = width,
                               height = self.props.bar_thickness,
                               angle  = angle,
                               fill   = True,
                               color  = self.props.bar_color,
                               alpha  = self.props.bar_alpha))
        self.connect()

    def generate(self) :

        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            if self.properties_name[i] == "fro" :
                Lua_conf += ( '{}m = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
                continue
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf

