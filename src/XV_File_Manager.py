# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import os
import yaml

from console import Console
"""---IMPORTANT VARIABLES---
BACE_PATH <--- The path that this file is placed in
PLATFORM <--- Users platform
SLASH <--- The Slash type used in users paths "\\" or "/""
CWD <--- The set path stands for 'current working directory'
"""
def create_textbox(root, values, gx, gy, gs="nswe", **kwargs):
        """Creates and Grids A Combobox"""
        box = ttk.Combobox(root, values=values, **kwargs)
        box.grid(row=gx, column=gy, sticky=gs)
        box.set(values[0])
        
        return box



    
class xv_files():
    def chdir(self, newdir):
        os.chdir(newdir)
        self.cwd = newdir
    def __init__(self, yaml_cfg):
        self.console = Console()
        self.root_path = os.getcwd()
        self.cwd = self.root_path
        
        self.optype = os.name
        
        self.chdir(f"{self.root_path}/.config")
        self.slash = "\\" if self.optype == "nt" else "/"

        
        # COMMANDS_DIR AND LIST_OF_COMMANDS
        self.commands_dir = f"{self.root_path}{self.slash}.commands"
        self.chdir(self.commands_dir)
        self.all_commands = os.listdir(self.commands_dir)
        
        # Create a tkinter screen named self.tkroot
        self.tkroot = tk.Tk()
        self.tkroot.geometry('500x400')
        self.tkroot.title("XV File Manager")
        
        # Create a Entrybox with CWD inserted
        tk.Label(self.tkroot,text="set directory: ",font="monospace 8").grid(row=0,column=0)
        set_dir_entry = create_textbox(self.tkroot, [self.cwd], 0, 1, font="monospace 8", width=60)
    
        # Create list of commandsset_dir_entry
        ROW_NUM = 2
        
        for i ,command in enumerate(self.all_commands):
            tk.Label(self.tkroot,text=command,font="monospace 10",fg="darkblue").grid(row=ROW_NUM,column=i * 3,sticky="nswe")
            tk.Button(self.tkroot,text=f"Run {command}",font="monospace 9").grid(row=ROW_NUM,column=i * 4 + 1 ,sticky="nswe")
            
            try:
                os.chdir(f"{self.commands_dir}\{command}")
            except FileNotFoundError:
                self.console.print(f"invalid command {command}!")
                        
        # self.tkroot mainloop
        self.tkroot.mainloop()
    
    
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    xv_files(YAMLCFG)
