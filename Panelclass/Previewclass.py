#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:16:45 2018

@author: david
"""


class PreviewPanelFunction :
    
    def __init__(self) :
        pass
        
    def leave_figure(self, event) :
        self.canvas.mpl_disconnect(self.cid_mouse_pos)

    def enter_figure(self, event):
        self.cid_mouse_pos =  self.f.canvas.mpl_connect('motion_notify_event', self.display_mouse_pos)

    def display_mouse_pos(self, event) :
        # only display if an object is created
#        if self.Out.list_obj==[] : return
#        self.Out.Prop.get_prop_values() # ????????? to delete?
        if event.xdata != None :
            x=int(event.xdata)
            y=int(event.ydata)
            text = 'x= {} y={}'.format(x, y)
            self.xy_pos_aff.set_text(text)
            self.canvas.draw()

    def get_xy(self, event) :

        # append position while there still point needed to draw figure
        if self.nb_input >0 :
            self.xs.append(int(event.xdata))
            self.ys.append(int(event.ydata))
            self.nb_input-=1

        # if get last point : draw the last(newly created) object
        if self.nb_input == 0 :
            self.Out.list_obj[-1].create_graph(self.xs, self.ys)
            self.nb_input-=1
            self.canvas.draw()
            
            