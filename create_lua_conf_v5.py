#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:10:20 2018

@author: david
"""

import tkinter as tk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from LuaObjectClass import LUARingGraph, LUABarGraph, LUAStaticText, LUAVariableText, LUALine, unformat_functions
#plt.use("TkAgg")


class GUITkinter(tk.Frame):
    
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("LUA conf")
        
        self.list_obj=list()
        
        self.Opt =  OptionPanel(self)        
        self.Fig =  PreviewPanel(self)
        subframe = tk.Frame(self, padx=0, pady=0)
        self.Obj =  ObjectPanel(subframe, self)
        self.Prop = ObjectPropertyPanel(subframe, self)
        subframe.pack()                



###########################################################################################################
class OptionPanel() :
    
    def __init__(self,Out) :
        
        self.Out = Out
        frame=tk.LabelFrame(self.Out.master, text="option", padx=5, pady=5)
        tk.Button(frame, text ='ring_graph',        command=self.draw_ring_graph   ).pack(padx=5, pady=5)
        tk.Button(frame, text ='bar_graph',         command=self.draw_bar_graph    ).pack(padx=5, pady=5)
        tk.Button(frame, text ='static_text',       command=self.draw_static_text  ).pack(padx=5, pady=5)
        tk.Button(frame, text ='variable_text',     command=self.draw_variable_text).pack(padx=5, pady=5)
        tk.Button(frame, text ='line',              command=self.draw_line         ).pack(padx=5, pady=5)
        tk.Button(frame, text ='Generate LUA conf', command=self.create_LUA_conf   ).pack(padx=5, pady=5, side=tk.BOTTOM)
        frame.pack(side=tk.LEFT,fill=tk.BOTH)
        
    def draw_ring_graph(self) :
        
        self.Out.list_obj.append( LUARingGraph(self.Out.Fig.ab, "ring_graph") )
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input 
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        self.Out.Obj.get_object_list()
        
    def draw_bar_graph(self) :
        
        self.Out.list_obj.append( LUABarGraph(self.Out.Fig.ab, "bar_graph") )
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input 
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        self.Out.Obj.get_object_list()
        
    def draw_static_text(self) :
        
        self.Out.list_obj.append( LUAStaticText(self.Out.Fig.ab, "static_text") )
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input 
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        self.Out.Obj.get_object_list()
    
    def draw_variable_text(self) :
        
        self.Out.list_obj.append( LUAVariableText(self.Out.Fig.ab, "variable_text") )
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input 
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        self.Out.Obj.get_object_list()
        
    def draw_line(self) :
        
        self.Out.list_obj.append( LUALine(self.Out.Fig.ab, "line") )
        self.Out.Fig.nb_input = self.Out.list_obj[-1].nb_input 
        self.Out.Fig.xs=[]; self.Out.Fig.ys=[]
        self.Out.Obj.get_object_list()
        
    def create_LUA_conf(self) :    
        fichier = open("conky_draw_config.lua", "w")
        
        Lua_conf="elements = {\n"
        for obj in self.Out.list_obj : 
            Lua_conf += obj.generate()
        Lua_conf += "}"
        print(Lua_conf)
        
        fichier.write(Lua_conf)
        fichier.close()
        
        
###########################################################################################################
class ObjectPanel() : 
    
    def __init__(self, frame, Out) :
        
        self.obj_pos = 0
        self.Out = Out
        
        frame=tk.LabelFrame(frame, text="Object created", padx=5, pady=5)
        
        # liste les objets
        subframe1 = tk.Frame(frame, padx=0, pady=0)
        scroll_y = tk.Scrollbar(subframe1, orient="vertical")
        self.listbox = tk.Listbox(subframe1, yscrollcommand=scroll_y.set)
        self.listbox.bind('<<ListboxSelect>>', self.selected)
        scroll_y['command'] = self.listbox.yview
        scroll_y.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.pack()
        subframe1.pack()
        
        # supprime l'object selectionné
        subframe2 = tk.Frame(frame, padx=0, pady=0)
        tk.Button(subframe2, text ='delete', command=self.delete).pack(padx=5, pady=5, side=tk.LEFT)
        subframe2.pack()
        
        # renomme l'object selectionné
        subframe3 = tk.Frame(frame, padx=0, pady=0)
        tk.Button(subframe3, text ='rename', command=self.rename).pack(padx=5, pady=5, side=tk.LEFT)
        self.newname_entry = tk.StringVar()
        self.newname_entry.set("Enter New Name")
        self.entree = tk.Entry(subframe3, textvariable=self.newname_entry)
        self.entree.pack(side=tk.RIGHT)
        subframe3.pack()
        
        frame.pack(side=tk.TOP, fill=tk.BOTH)
        
    def get_object_list(self) : 
        
        self.listbox.delete(0, tk.END)
        for obj in self.Out.list_obj[:] :
            self.listbox.insert(tk.END, obj.name)
        
    def selected(self, event) : # update property
        
        self.obj_pos = self.listbox.curselection()[0]        
        self.Out.Prop.get_prop_values()
        
    def delete(self) :
        
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        obj.graph.remove()
        del self.Out.list_obj[self.Out.Obj.obj_pos]
        self.get_object_list()
        self.Out.Fig.canvas.show()
        self.obj_pos = 0
        
    def rename(self) :
        
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        newname = self.newname_entry.get()
        self.newname_entry.set("Enter New Name")
        obj.name = newname
        self.get_object_list()
        
        
        
        
###########################################################################################################
class ObjectPropertyPanel() :
    
    def __init__(self, frame, Out) :
        
        self.Out = Out
        self.entry_list=list()
        self.label=list()
        self.label_var=list()
        
        frame=tk.LabelFrame(frame, text="Object Property", padx=5, pady=5)
        for i in range(10) :
            subframe = tk.Frame(frame, borderwidth=0, relief=tk.GROOVE)
            self.entry_list.append(MyEntryBox(subframe))
            self.label_var.append(tk.StringVar())
            self.label.append(tk.Label(subframe, textvariable=self.label_var[i]).pack(side=tk.RIGHT))
            subframe.pack(padx=0, pady=0)
        tk.Button(frame, text ='valide', command=self.set_obj_values).pack(padx=5, pady=5)
        frame.pack(fill=tk.BOTH)   

    def get_prop_values(self) :
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        
        for i in range(10) :
            self.entry_list[i].delete()
            self.label_var[i].set(" ")
        for i in range(len(obj.properties)) :
            self.entry_list[i].s(i, obj.properties[i])
            self.label_var[i].set( str(obj.properties_name[i]) )
            
    def set_obj_values(self) :
        obj = self.Out.list_obj[self.Out.Obj.obj_pos]
        
        for i in range(len(obj.properties)) :
            obj.properties[i] = self.entry_list[i].get()
        self.get_prop_values()   
        
        obj.graph.remove()
        obj.make_graph()
        self.Out.Fig.canvas.show()
    


###########################################################################################################
class PreviewPanel() :
    
    def __init__(self, Out) :
                
        self.Out = Out
        self.xs = []
        self.ys = []
        
        self.nb_input=-1
        
        frame=tk.LabelFrame(self.Out.master, text="your conky preview", cursor="cross", padx=5, pady=5)
        frame.bind("<Enter>", self.enter_figure)
        frame.bind("<Leave>", self.leave_figure)
        
        # create figure
        self.f = Figure(figsize=(8, 8), dpi=75, facecolor='darkslategray')
        self.xy_pos_aff = self.f.text(0, 0, 'x= y=', size=16)
        
        # create subplot
        self.ab = self.f.add_subplot(111, facecolor='darkslategray') 
        self.ab.set_xlim(0, 400)
        self.ab.set_ylim(400, 0)
        
        # create canvas
        self.canvas = FigureCanvasTkAgg(self.f, frame)
        
        # get mouse input => create new object
        self.cid =  self.f.canvas.mpl_connect('button_press_event', self.get_xy)
        
        # show
        self.canvas.show()
        self.canvas.get_tk_widget().pack(padx=5, pady=5)
        frame.pack(side=tk.LEFT)
        
    def leave_figure(self, event) :
        self.canvas.mpl_disconnect(self.cid_mouse_pos)
        
    def enter_figure(self, event):
        self.cid_mouse_pos =  self.f.canvas.mpl_connect('motion_notify_event', self.display_mouse_pos)
        
    def display_mouse_pos(self, event) :
        if self.Out.list_obj==[] : return
        self.Out.Prop.get_prop_values()   
        if event.xdata != None :
            text = 'x= {} y={}'.format(int(event.xdata),int(event.ydata))
            self.xy_pos_aff.set_text(text)
            self.canvas.show()
        
    def get_xy(self, event) : 
        
        if self.nb_input >0 :
            self.xs.append(int(event.xdata))
            self.ys.append(int(event.ydata))
            self.nb_input-=1
            
        if self.nb_input == 0 :
            self.Out.list_obj[-1].create_graph(self.xs, self.ys)
            self.nb_input-=1
            self.canvas.show()
            
            
            
    
###########################################################################################################
###########################################################################################################
###########################################################################################################        
class MyEntryBox() :
    
    def __init__(self, master) :
        
        self.text=tk.StringVar()
        self.entree = tk.Entry(master, textvariable=self.text)
        self.entree.pack(side=tk.RIGHT)
        
    def get(self) :
        
        return self.text.get()
        
    def s(self, pos, value) :
        
        self.text.set(value)
        
    def delete(self) :
        self.entree.delete(0,tk.END)
    

root = tk.Tk()
GUITkinter(root).pack()
root.mainloop()




