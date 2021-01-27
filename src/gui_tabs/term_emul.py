#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tk_custum_widgets import TKConsole
import tkinter as tk

class CFG:
    tab_name="CLI Emul"
    defualt_side="LEFT"
    active_on_start=True
    output_tab="cmdout_console"
    reqcoms=(None, "run_command")
    reqtabs=(None, "cmdout_console")

class Tab(tk.Frame):
    def __init__(self, root, tkroot): 
        self.root = root
        def tkinputconsole_keyevents(event):
            if event.keysym == "Return":
                self.tkinputconsole_row += 1
                raw_command = self.tkinputconsole_bottom.get(f"{self.tkinputconsole_row}.0", f"{self.tkinputconsole_row}.1000")
                
                root["run_command"](root, root["loaded_tabs"][CFG.output_tab], raw_command.split(" ")[0] if isinstance(raw_command.split(" "), list) 
                                 else raw_command, 
                                 raw_command.split(" ")[1:] if isinstance(raw_command.split(" "), list) 
                                 else [])
            else:
                pass
        
        # Frame
        tk.Frame.__init__(self, tkroot)
        
        # Vars
        self.tkinputconsole_row = 0
        
        # Right (User Input)
        self.tkinputconsole_bottom = TKConsole(self, width=80, height=12, wrap=tk.NONE, font='monospace 10', bg="black", fg="white")
        self.tkinputconsole_bottom.grid(column=0, row=51, rowspan=50)
        self.tkinputconsole_bottom.bind("<Key>", tkinputconsole_keyevents)
        
        # Left
        self.tkinputconsole_top = TKConsole(self, width=80, height=12, wrap=tk.NONE, font='monospace 10', bg="black", fg="white")
        self.tkinputconsole_top.grid(column=0, row=0, rowspan=50)
        self.update()
        
    def update(self):
        self.tkinputconsole_top.config(state="normal")
        self.tkinputconsole_top.delete("1.0", "end")
        self.tkinputconsole_top.insert("end", f"""/-----------------------------<CLI Emulater>-----------------------------------\\
|   
|   PATH: {self.root["cwd"]}
|                                                                              
|                                                                              
|                                                                              
|                                                                              
|
|                                                                              
|                                                                              
|                                                                              
\\------------------------------------------------------------------------------/""", sep="")
        self.tkinputconsole_top.config(state="disabled")