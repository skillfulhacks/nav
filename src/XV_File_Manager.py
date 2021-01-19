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

def xv_files(yaml_cfg):
    def create_textbox(root, values, gx, gy, gs="nswe", **kwargs):
        """Creates and Grids A Combobox"""
        box = ttk.Combobox(root, values=values, **kwargs)
        box.grid(row=gx, column=gy, sticky=gs)
        box.set(values[0])
        
        return box
    console = Console()
    BACE_PATH = os.getcwd()
    os.chdir(".config")
    
    PLATFORM = open("PLATFORM.ini","r").read()
    CWD = open("SETDIR.ini","r").read()
    
    if PLATFORM == "Win":
        SLASH = "\\"
    else:
        SLASH = "/"
    
    # COMMANDS_DIR AND LIST_OF_COMMANDS
    COMMANDS_DIR = f"{BACE_PATH}{SLASH}.commands"
    os.chdir(COMMANDS_DIR)
    LIST_OF_COMMANDS = os.listdir(COMMANDS_DIR)
    
    # Create a tkinter screen named gui
    gui = tk.Tk()
    gui.geometry('500x400')
    gui.title("XV File Manager")
    # Create a Entrybox with CWD inserted
    tk.Label(gui,text="set directory: ",font="monospace 8").grid(row=0,column=0)
    set_dir_entry = create_textbox(gui, [CWD], 0, 1, font="monospace 8", width=60)

    # Create list of commandsset_dir_entry
    ROW_NUM = 2
    
    for i ,command in enumerate(LIST_OF_COMMANDS):
        tk.Label(gui,text=command,font="monospace 10",fg="darkblue").grid(row=ROW_NUM,column=i * 3,sticky="nswe")
        tk.Button(gui,text=f"Run {command}",font="monospace 9").grid(row=ROW_NUM,column=i * 4 + 1 ,sticky="nswe")
        
        try:
            os.chdir(f"{COMMANDS_DIR}\{command}")
        except FileNotFoundError:
            console.print(f"invalid command {command}!")
            
        with open("Description","r") as file:
            Description = file.read()
            file.close()
        tk.Label(gui,text=f"Description:\n{Description}",font="monospace 8",fg="gray").grid(row=ROW_NUM+1,column=i * 3,sticky="nswe")
    
    # gui mainloop
    gui.mainloop()
    
    
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    xv_files(YAMLCFG)
