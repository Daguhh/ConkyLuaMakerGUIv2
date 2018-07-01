#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:17:53 2018

@author: david
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Panelclass import MenuBarFunction, OptionPanelFunction, ObjectPanelFunction, ObjectPropertyPanelFunction, PreviewPanelFunction
from Panelclass import MyEntryBox


FIG_SIZE_X = 600
FIG_SIZE_Y = 600
FIG_DIM_X = 12
FIG_DIM_Y = 12
TEXT_SIZE_CORR = 1
FIGURE_SIZE_CORR = 1

class GUITkinter(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("LUA conf")

        # activate infos on commands
        self.show_hint = 0
        
        # list of lua figures created
        self.list_obj=list()

        # create the different panel of the GUI
        self.Menu = MenuBar(self)
        self.Opt  = OptionPanel(self)
        self.Fig  = PreviewPanel(self)
        subframe  = tk.Frame(self, padx=0, pady=0)
        self.Obj    =  ObjectPanel(subframe, self)
        self.Prop   =  ObjectPropertyPanel(subframe, self)
        subframe.pack()
        
class MenuBar(MenuBarFunction) :

    def __init__(self, Out) :
        
        self.Out = Out
        master = Out.master
        menubar = tk.Menu(master)
        submenu1 = tk.Menu(master)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Load", command=self.load)
        menu1.add_command(label="Save", command=self.save)
        menu1.add_command(label="Save & generate", command=self.save_and_generate)
        menu1.add_separator()
        menu1.add_command(label="Quit", command=master.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = tk.Menu(menubar, tearoff=0)
#        menu2.add_command(label="Background", command=self.set_background_color)
#        menu2.add_command(label="Gird step", command=self.set_grid_step)
#        menu2.add_command(label="Conky size", command=self.set_conky_size)
        menu2.add_separator()
#        submenu1.add_command(label="bar_color", command=self.alert)
#        submenu1.add_command(label="bar_alpha", command=self.alert)
#        submenu1.add_command(label="bar_thickness", command=self.alert)
#        submenu1.add_command(label="background_color", command=self.alert)
#        submenu1.add_command(label="background_alpha", command=self.alert)
#        submenu1.add_command(label="background_thickness", command=self.alert)
        menu2.add_cascade(label="Change default values", menu = submenu1)
        menubar.add_cascade(label="Edit", menu=menu2)

        menu3 = tk.Menu(menubar, tearoff=0)
        menu3.add_command(label="Color generator", command=self.color_tool)
#        menu3.add_command(label="Add an offset", command=self.alert)
#        menu3.add_command(label="Coller", command=self.alert)
        menubar.add_cascade(label="Tool", menu=menu3)

        master.config(menu=menubar)
        
class OptionPanel(OptionPanelFunction):

    def __init__(self, Out) :

        self.Out = Out
        frame=tk.LabelFrame(self.Out.master, text="option", padx=5, pady=5)
        tk.Button(frame, text ='ring_graph',        command=lambda :self.draw_lua_object("ring_graph"   )).pack(padx=5, pady=5)
        tk.Button(frame, text ='ellipse_graph',     command=lambda :self.draw_lua_object("ellipse_graph"  )).pack(padx=5, pady=5)
        tk.Button(frame, text ='bar_graph',         command=lambda :self.draw_lua_object("bar_graph"    )).pack(padx=5, pady=5)
        tk.Button(frame, text ='static_text',       command=lambda :self.draw_lua_object("static_text"  )).pack(padx=5, pady=5)
        tk.Button(frame, text ='variable_text',     command=lambda :self.draw_lua_object("variable_text")).pack(padx=5, pady=5)
        tk.Button(frame, text ='line',              command=lambda :self.draw_lua_object("line"         )).pack(padx=5, pady=5)
        tk.Button(frame, text ='ring',              command=lambda :self.draw_lua_object("ring"         )).pack(padx=5, pady=5)
        tk.Button(frame, text ='ellipse',           command=lambda :self.draw_lua_object("ellipse"        )).pack(padx=5, pady=5)

#        tk.Button(frame, text ='Generate LUA conf', command=self.create_LUA_conf ).pack(padx=5, pady=5, side=tk.BOTTOM)
        frame.pack(side=tk.LEFT,fill=tk.BOTH)


class PreviewPanel(PreviewPanelFunction) :
    # give a preview of the conky with matplotlib (may be some differences)
    def __init__(self, Out) :

        self.Out = Out
        self.xs = []
        self.ys = []
        self.coarse = 1
        self.nb_input=-1
        
        master = Out.master

        frame=tk.LabelFrame(master, text="your conky preview", cursor="cross", padx=5, pady=5)
        frame.bind("<Enter>", self.enter_figure)
        frame.bind("<Leave>", self.leave_figure)

        # create figure
        self.f = Figure(figsize=(FIG_DIM_X, FIG_DIM_Y), dpi=75, facecolor='darkslategray')
        self.xy_pos_aff = self.f.text(0, 0, 'x= y=', size=16)

        # create subplot
        self.ab = self.f.add_subplot(111, facecolor='darkslategray')
        self.ab.set_xlim(0, FIG_SIZE_X)
        self.ab.set_ylim(FIG_SIZE_Y, 0)

        # create canvas
        self.canvas = FigureCanvasTkAgg(self.f, frame)

        # get mouse input => create new object
        self.cid =  self.f.canvas.mpl_connect('button_press_event', self.get_xy)

        # show
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=5, pady=5)
        frame.pack(side=tk.LEFT)
        
class ObjectPanel(ObjectPanelFunction):

    def __init__(self, frame, Out):

        self.obj_pos = 0
        self.Out = Out

        frame=tk.LabelFrame(frame, text="Object created", padx=5, pady=5)

        # list of all objects
        subframe1 = tk.Frame(frame, padx=0, pady=0)
        scroll_y = tk.Scrollbar(subframe1, orient="vertical")
        self.listbox = tk.Listbox(subframe1, yscrollcommand=scroll_y.set)
        self.listbox.bind('<<ListboxSelect>>', self.selected)
        scroll_y['command'] = self.listbox.yview
        scroll_y.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.pack()
        subframe1.pack()

        # delete object selected
        subframe2 = tk.Frame(frame, padx=0, pady=0)
        tk.Button(subframe2, text ='delete', command=self.delete).pack(padx=5, pady=5, side=tk.LEFT)
        tk.Button(subframe2, text ='duplicate', command=self.duplicate).pack(padx=5, pady=5, side=tk.LEFT)
        subframe2.pack()

        # rename object selected
        subframe3 = tk.Frame(frame, padx=0, pady=0)
        tk.Button(subframe3, text ='rename', command=self.rename).pack(padx=5, pady=5, side=tk.LEFT)
        self.newname_entry = tk.StringVar()
        self.newname_entry.set("Enter New Name")
        self.entree = tk.Entry(subframe3, textvariable=self.newname_entry)
        self.entree.pack(side=tk.RIGHT)
        subframe3.pack()

        frame.pack(side=tk.TOP, fill=tk.BOTH)
        
class ObjectPropertyPanel(ObjectPropertyPanelFunction) :
    # list properties of the selected object
    def __init__(self, frame, Out) :

        self.Out = Out
        self.entry_list=list()
        self.label=list()
        self.label_var=list()

        frame=tk.LabelFrame(frame, text="Object Property", padx=5, pady=5)
        for i in range(25) :
            subframe = tk.Frame(frame, borderwidth=0, relief=tk.GROOVE)
            self.entry_list.append(MyEntryBox(subframe))
            self.label_var.append(tk.StringVar())
            self.label.append(tk.Label(subframe, textvariable=self.label_var[i]).pack(side=tk.RIGHT))

            subframe.pack(padx=0, pady=0, fill=tk.X)
        tk.Button(frame, text ='valide', command=self.set_obj_values).pack(padx=5, pady=5)
        frame.pack(fill=tk.BOTH)
        
        
        
root = tk.Tk()
GUITkinter(root).pack()
root.mainloop()
