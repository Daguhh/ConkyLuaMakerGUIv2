#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:15:53 2018

@author: david
"""
import tkinter as tk

        
class ObjectPanelFunction :

    def __init__(self) :
        pass
    
    def duplicate(self) :

        old_obj = self.Out.list_obj[self.obj_pos]

        # copy the kind of object and create new one
        new_kind = old_obj.kind
        self.Out.Opt.draw_lua_object(new_kind)
        new_obj = self.Out.list_obj[-1]
        
        # get properties
        new_obj.properties = old_obj.properties[:]        
        
        # rename
        new_obj.name = "copy of {}".format(old_obj.name)
        self.Out.Prop.set_obj_values()
        self.Out.Obj.refresh()
        
        # make graph
#        self.Out.list_obj.append(new_obj)
        new_obj.make_graph()
        self.Out.Fig.canvas.draw()
        self.Out.Fig.nb_input=-1

    def refresh(self) :

        self.listbox.delete(0, tk.END)
        for obj in self.Out.list_obj[:] :
            self.listbox.insert(tk.END, obj.name)

    def selected(self, event) : # update property

        self.obj_pos = self.listbox.curselection()[0]
        # get property of selected object
        self.Out.Prop.get_prop_values()

    def delete(self) :

        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        obj.graph.remove()
        del self.Out.list_obj[self.Out.Obj.obj_pos]
        self.refresh()
        self.Out.Fig.canvas.draw()
        self.obj_pos = 0

    def rename(self) :

        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        newname = self.newname_entry.get()
        self.newname_entry.set("Enter New Name")
        obj.name = newname
        self.refresh()


