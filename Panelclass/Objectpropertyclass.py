#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:16:17 2018

@author: david
"""

class ObjectPropertyPanelFunction:
    
    def __init__(self):
        pass
    
    def get_prop_values(self) :
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]

        for i in range(25) :
            self.entry_list[i].delete()
            self.label_var[i].set(" ")
        for i in range(len(obj.properties)) :
            self.entry_list[i].s(i, obj.properties[i])
            self.label_var[i].set( str(obj.properties_name[i]) )

    def set_obj_values(self) :
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        props=[]
        for i in range(len(obj.properties)) :
            props.append( self.entry_list[i].get())
        obj.properties = props
        self.get_prop_values()

        obj.graph.remove()
        obj.make_graph()
        self.Out.Fig.canvas.draw()