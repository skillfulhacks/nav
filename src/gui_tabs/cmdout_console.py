#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tk_custum_widgets import TKConsole

class CFG:
    tab_name="CMDOUT"
    defualt_side="RIGHT"
    active_on_start=True
    output_tab=None
    reqcoms=()
    reqtabs=()
    
class Tab(TKConsole):
    def __init__(self, root, tkroot): 
        TKConsole.__init__(self, tkroot, width=80, height=30, wrap=tk.NONE, bg="black")
    
    def update(self):
        pass