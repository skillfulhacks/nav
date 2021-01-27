#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tk_custum_widgets import create_textbox, ScrolledFrame

class CFG:
    tab_name="Commands"
    defualt_side="LEFT"
    active_on_start=True
    output_tab="cmdout_console"
    reqcoms=(None, "run_command")
    reqtabs=(None, "cmdout_console")
    
class Tab(ScrolledFrame):
    def __init__(self, root, tkroot): 
        ScrolledFrame.__init__(self, tkroot)
        self.root = root
        
        # Create a Entrybox with CWD inserted
        tk.Label(self.interior, text="set directory: ",font="monospace 8").grid(row=0,column=0)
        self.set_dir_entry = create_textbox(self.interior, [root["cwd"]], font="monospace 8", width=60, state="readonly")
        self.set_dir_entry.grid(row=0, column=1, columnspan=3)
        
        tk.Label(self.interior, text="Command",font="monospace 16").grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Label(self.interior, text="Args",font="monospace 16").grid(row=1, column=2, columnspan=2, sticky="ew")

        # Main Button Loop
        for i, command in enumerate(root["imported_commands"].keys()):
            try:
                if root["imported_commands"][command].INTERNAL:
                    continue
            except AttributeError:
                pass
            args_entry = create_textbox(self.interior, [""], font="monospace 8")
            args_entry.grid(row=2 + i, column=3, sticky="ew")
            tk.Button(self.interior,text=f"{command}", font="monospace 9 bold", 
                      command=lambda consoleout=root["loaded_tabs"][CFG.output_tab], entry=args_entry, x=command: root["run_command"](root, consoleout, x, entry.get().split(" "))
                      ).grid(row=2 + i, column=0, columnspan=3, sticky="nswe")
    
    def update(self):
        """Updates the self.set_dir_entry When a Command is run"""
        self.set_dir_entry.set(self.root["cwd"])