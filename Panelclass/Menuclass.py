#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:13:55 2018

@author: david
"""
import tkinter as tk
from tkinter import colorchooser
import pickle
from tkinter import messagebox

CONKY_PROPERTY_DCT = {
        "conky_size" : (400, 400),
        "figure_size" : (8, 8),
        "grid_step" : 5,
        "text_size_corr" : 1,
        "figure_size_corr" : 1,
        }
        
DEFAULT_PROPERTY_DCT = {
        "background_color" : "#000000",
        "bar_color" : "#000000",
        "bar_thickness" : 10,
        "bar_alpha" : 1,
        "bar_background_color" : "#000000",
        "bar_background_thickness" : 10,
        "bar_baackground_alpha" : 1,
        }

        
class MenuBarFunction:
    
    def __init__(self):
        pass
        
    def save(self):

        with open("Lua_conf_save.pkl", 'wb') as output :
            pickle.dump(self.Out.list_obj, output, pickle.HIGHEST_PROTOCOL)


    def load(self) :
        with open("Lua_conf_save.pkl", 'rb') as in_put :
            liste = pickle.load(in_put)
            for obj in liste :
                old_obj = obj

                # copy the kind of object and create new one
                new_kind = old_obj.kind
                self.Out.Opt.draw_lua_object(new_kind)
                new_obj = self.Out.list_obj[-1]

                # rename
                new_obj.name = format(old_obj.name)
                self.Out.Obj.refresh()

                # get properties
                new_obj.props = old_obj.props
                
                # make graph
                new_obj.make_graph()
                self.Out.Fig.canvas.draw()
                self.Out.Fig.nb_input=-1


    def save_and_generate(self):
        self.save()

        fichier = open("conky_draw_config.lua", "w")

        Lua_conf="elements = {\n"
        for obj in self.Out.list_obj :
            Lua_conf += obj.generate()

        Lua_conf += "}"
        print(Lua_conf)

        fichier.write(Lua_conf)
        fichier.close()


    def color_tool(self) :
        (triple, hexstr) = colorchooser.askcolor()

