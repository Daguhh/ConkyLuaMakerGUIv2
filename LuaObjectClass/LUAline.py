#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:43:37 2018

@author: david
"""

import numpy as np
import matplotlib.patches as patches
from LuaObjectClass.unformat_functions import unformat_xy, unformat_color

class LUALine :
    
    def __init__ (self, ax) :
                
#        self.fig = figure
        self.kind = "line"
        self.name = "line"
        self.ax = ax
        self.graph = []
        self.properties = []
        self.properties_name = []
   
        self.create_properties()
        self.nb_input = 2
     
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
        (x1, y1) = unformat_xy(self.properties[1])
        self.press = x0, y0, x1, y1, event.xdata, event.ydata
        
    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.graph.axes: return
        x0, y0, x1, y1, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        fro_x = int(x0+dx)
        fro_y = int(y0+dy)
        to_x = int(x1+dy)
        to_y = int(y1+dy)
        self.graph.set_x(fro_x)
        self.graph.set_y(fro_y)
        self.properties[0] = ("{}x={}, y={}{}".format('{',fro_x,fro_y,'}'))
        self.properties[1] = ("{}x={}, y={}{}".format('{',to_x,to_y,'}'))
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
        to = ("{}x={}, y={}{}".format('{',x[1],y[1],'}'))
        self.properties[0] = fro
        self.properties[1] = to
        
        self.make_graph()
        
    
    def make_graph(self) :
        P = self.properties
    
        fro      = unformat_xy(P[0])
        to       = unformat_xy(P[1])
        thickness= int(P[2])
        color    = unformat_color(P[3])
        alpha    = float(P[4])
        
        tan = (to[1]-fro[1]) / (to[0]-fro[0])
        angle = np.arctan(tan)*180/(np.pi) + \
                180 * ( (to[0]-fro[0])<0 )
                
        width = int(np.sqrt( (to[1]-fro[1])**2 + (to[0]-fro[0])**2 ))
        
        self.graph = self.ax.add_patch(patches.Rectangle((fro[0], fro[1]),
                                                    width,
                                                    thickness,
                                                    angle=angle,
                                                    fill=True,
                                                    color=color,
                                                    alpha=alpha)) 
        self.connect()

    def create_properties(self) :

        fro=0
        to=0
        color="0xFFFFFF"
        thickness=2
        alpha = 1
        self.properties_name = ["from",
                                "to",
                                "thickness",
                                "color",
                                "alpha"] 
        self.properties = [fro, 
                           to, 
                           thickness,
                           color,
                           alpha]
          
        
    def generate(self) :
        
        Lua_conf= ('-- {}\n{}\nkind = \'{}\',\n'.format(self.name,'{',self.kind))
        for i in range(len(self.properties_name)) :
            Lua_conf += ( '{} = {}, \n'.format(self.properties_name[i], self.properties[i] ) )
        Lua_conf += ('{}\n'.format('},'))
        return Lua_conf

