#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from pyassets.tk import TKText

class CFG:
    tab_name="CMDOUT"
    defualt_side="RIGHT"
    active_on_start=True
    output_tab=None
    reqcoms=()
    reqtabs=()
    
class Tab(TKText):
    def __init__(self, root, tkroot): 
        TKText.__init__(self, tkroot, width=80, height=30, wrap=tk.NONE, bg="black")
    
    def update(self):
        pass