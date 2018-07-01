#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:17:06 2018

@author: david
"""
import tkinter as tk


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