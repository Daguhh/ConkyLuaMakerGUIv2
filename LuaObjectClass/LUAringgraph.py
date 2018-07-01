#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import numpy as np
import matplotlib.patches as patches
from .classproperties import Properties

#######################################################""
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
        
        x0, y0 = self.graph.center
        
        # remove circle interior picking
        event_radius = np.sqrt((event.xdata-x0)**2 + (event.ydata-y0)**2)
        if self.props.radius - self.props.bar_thickness > event_radius : return
        
        # remove out angle picking
        tan = (event.ydata-y0) / (event.xdata-x0)
        event_angle = np.arctan(tan)*180/(np.pi) + \
                180 * ( (event.xdata-x0)<0 )
        min_angle = self.graph.theta1
        max_angle = self.graph.theta2
        if  event_angle<min_angle and event_angle>max_angle : return
        
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
            setattr(self.props, "center", new_pos)
            
            new_pos = (x, y)
            setattr(self.graph, "center", new_pos)
            
        elif self.key_pressed == "control" : # resize
            print("control")
            new_size = 2*np.sqrt((x-x0)**2+(y-y0)**2)
            setattr(self.props, "radius", new_size)
            setattr(self.graph,  "width" , new_size)
            setattr(self.graph,  "height" , new_size)
            
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
        
        
        #######################################################################"
        
class LUARingGraph(MovableObject) :
    
    def __init__ (self, ax) :
        self.ax = ax
        self.kind = "ring_graph"
        self.name = "ring_graph"
        self.graph = []
        
        self.nb_input = 2
        
        
        dct = {
        "center" : "{x=1, y=1}",
        "radius" : 1,
        "conky_value" : "'cpu cpu0'",
        "max_value" : 100,
        "critical_threshold" : 90,
        "bar_color" : "0x000000",
        "bar_alpha" : 1,
        "bar_thickness" : 8,
        "start_angle" : 0,
        "end_angle" : 360,
        "background_color" : "0xFFFFFF",
        "background_alpha" : 1,
        "background_thickness" : 8,
        "change_color_on_critical" : 0,
        "change_alpha_on_critical" : 0,
        "change_thickness_on_critical" : 0,
        "background_color_critical" : "0x000000",
        "background_alpha_critical" : 1,
        "background_thickness_critical" :8,
        "bar_color_critical" : "0x000000",
        "bar_alpha_critical" : 1,
        "bar_thickness_critical" : 8
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
        
        self.props.center = ("{}x={}, y={}{}".format('{',x[0],y[0],'}'))
        self.props.radius = int(np.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2))        
        self.make_graph()
        
    
    def make_graph(self) :
      
        if self.props.start_angle > self.props.end_angle:
            self.props.start_angle, self.props.end_angle = self.props.end_angle, self.props.start_angle
    
        self.graph = self.ax.add_patch(patches.Arc(  
                                            xy        = self.props.center,
                                            width     = 2*self.props.radius,
                                            height    = 2*self.props.radius,
                                            angle     = 0,
                                            theta1    = self.props.start_angle,
                                            theta2    = self.props.end_angle,
                                            linewidth = self.props.bar_thickness,
                                            color     = self.props.bar_color,
                                            picker    = True,
                                            alpha     = self.props.bar_alpha)
                                            )
        self.connect()
        
        
    def generate(self) :
        
        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf




   
###############################################################################

