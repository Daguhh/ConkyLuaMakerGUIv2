#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import numpy as np
import matplotlib.patches as patches
from LuaObjectClass.unformat_functions import unformat_xy, unformat_color


class LUARingGraph :
    
    def __init__ (self, ax, kind) :
        
        self.kind = kind
        self.name = kind
        self.ax = ax
        self.graph = []
        self.properties = []
        self.properties_name = []
        
        self.create_properties()
        self.nb_input = 2
        
    
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
        
        x0, y0 = self.graph.center
        
        # remove circle interior picking
        event_radius = np.sqrt((event.xdata-x0)**2 + (event.ydata-y0)**2)
        arc_radius = int(self.properties[1])
        arc_thickness = int(self.properties[7])
        if arc_radius - arc_thickness > event_radius : return
        
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
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        x = int(x0+dx)
        y = int(y0+dy)
        self.properties[0] = ("{}x={}, y={}{}".format('{',x,y,'}'))
        self.graph.center = (x, y)
        

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
        
        center = ("{}x={}, y={}{}".format('{',x[0],y[0],'}'))
        radius = int(np.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2))
        self.properties[0] = center
        self.properties[1] = radius
        
        self.make_graph()
        
    
    def make_graph(self) :
        P = self.properties
        
        center             = unformat_xy(P[0])
        diameter           = 2*int(P[1])
        max_value          = int(P[3])
        critical_threshold = int(P[4])
        bar_color          = unformat_color(P[5])
        bar_alpha          = P[6]
        bar_thickness      = int(P[7])
        
        start_angle        = int(P[8]) 
        end_angle          = int(P[9]) 
        if start_angle > end_angle:
            start_angle, end_angle = end_angle, start_angle
    
        self.graph = self.ax.add_patch(patches.Arc(xy=center,
                                            width = diameter,
                                            height= diameter,
                                            angle=0,
                                            theta1=start_angle,
                                            theta2=end_angle,
                                            linewidth = bar_thickness,
                                            color = bar_color,
                                            picker = True))
#        print(dir(self.graph))
        self.connect()
        
    def create_properties(self):

        center=(0.2,0.2)
        radius = 30
        conky_value = "'cpu cpu0'"
        max_value = 100
        critical_threshold = 90
        
        bar_color = "0x000000"
        bar_alpha = 1
        bar_thickness = 8
        
        start_angle = 0
        end_angle = 360
        
        background_color = "0xFFFFFF"
        background_alpha = 1
        background_thickness = 8 
        
        change_color_on_critical = "y"
        change_alpha_on_critical = "n"
        change_thickness_on_critical = "n"
        
        background_color_critical = "0x000000"
        bakcground_alpha_critical = 1
        background_thickness_critical =8
        
        bar_color_critical = "0x000000"
        bar_alpha_critical = 1
        bar_thickness_critical = 8
        
        
        self.properties_name = ["center",
                                "radius",
                                "conky_value",
                                "max_value",
                                "critical_threshold",
                                "bar_color",
                                "bar_alpha",
                                "bar_thickness",
                                "start_angle",
                                "end_angle"]
        self.properties = [center,
                           radius,
                           conky_value,
                           max_value,
                           critical_threshold,
                           bar_color,
                           bar_alpha,
                           bar_thickness,
                           start_angle,
                           end_angle]
        
        
    def generate(self) :
        
        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf

###############################################################################

