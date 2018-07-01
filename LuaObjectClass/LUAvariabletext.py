#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

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
            new_size = int((-y+y0))
            setattr(self.props, "fontsize", new_size)
            self.graph.set_fontsize(new_size)
            
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
        
        
class LUAVariableText(MovableObject) :
   
    def __init__ (self, ax) :
        self.ax = ax
        self.kind = "variable_text"
        self.name = "variable_text"
        self.graph = []

        self.nb_input = 1

        dct = {
                "fro" : "{x=0, y=0}",
               "conky_value": "'default'",
               "color" : "0x000000",
               "fontsize" : 12,
               "rotation" : 0,
               "font" : "'default font'",
#               "bold" : 0,
#               "italic" : 0,
               "alpha" : 1,
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
        self.make_graph()

    def make_graph(self) :

        self.graph = self.ax.annotate(s        = self.props.conky_value,
                                      xy       = self.props.fro,
                                      color    = self.props.color,
                                      fontsize = self.props.fontsize,
                                      rotation = self.props.rotation,
                                      name     = self.props.font)
        self.connect()
        
    def generate(self) :

        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            if self.properties_name[i] == "fro" :
                Lua_conf += ( '{}m = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
                continue
            if self.properties_name[i] == "bold" or self.properties_name[i] == "italic" :
                if self.properties[i] == 1:
                    Lua_conf += ( '{}'.format(self.properties_name[i])) 
                    continue
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf
