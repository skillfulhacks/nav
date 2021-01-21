# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import sys

import yaml

import tkinter as tk

from tk_custum_widgets import create_textbox, TKConsole, ScrolledFrame
from console import Console

"""---IMPORTANT VARIABLES---
BACE_PATH <--- The path that this file is placed in
PLATFORM <--- Users platform
SLASH <--- The Slash type used in users paths "\\" or "/""
CWD <--- The set path stands for 'current working directory'
"""

          
class XVFiles():
    def chdir(self, newdir):
        os.chdir(newdir)
        self.cwd = newdir
    def __init__(self, yaml_cfg):
        self.pyconsole = Console()
        self.root_path = os.getcwd()
        self.cwd = self.root_path
        
        # Operating System Type
        self.optype = os.name
        
        self.chdir(f"{self.root_path}/.config")
        self.slash = "\\" if self.optype == "nt" else "/"

        
        # COMMANDS_DIR AND LIST_OF_COMMANDS
        self.commands_dir = f"{self.root_path}{self.slash}.commands"
        
        # Adds Command Dir to Sys Path. Allowing Import from Non Standerd Paths
        sys.path.append(self.commands_dir)
        self.chdir(self.commands_dir)
        
        ### Importer ###
        self.command_files = [command.split(".")[0] for command in os.listdir(self.commands_dir) if os.path.isfile(f"{self.commands_dir}/{command}")]
        self.imported_commands = {}
        for i, command in enumerate(self.command_files):
            try:
                self.imported_commands.update({command: __import__(command)})
                print(self.imported_commands)
            except FileNotFoundError:
                self.pyconsole.print(f"invalid command {command}!")
        
        #################
        ### GUI START ###
        #################
        
        # Create a tkinter screen named self.tkroot
        self.tkroot = tk.Tk()
        self.tkroot.title("XV File Manager")
        self.tkroot.resizable(False, False)
        
        self.tkcommand_frame = ScrolledFrame(self.tkroot)
        self.tkcommand_frame.grid(column=0, row=0)
        
        # Creates Console
        self.tkconsole_frame = tk.Frame(self.tkroot)
        self.tkconsole_frame.grid(column=1, row=0, rowspan=100)
        
        self.tkconsole = TKConsole(self.tkconsole_frame, width=80, height=24, wrap=tk.NONE, font='monospace 10')
        self.tkconsole.pack(side=tk.TOP, fill=tk.X)

        # Create a Entrybox with CWD inserted
        tk.Label(self.tkcommand_frame.interior, text="set directory: ",font="monospace 8").grid(row=0,column=0)
        set_dir_entry = create_textbox(self.tkcommand_frame.interior, [self.root_path], font="monospace 8", width=60)
        set_dir_entry.grid(row=0, column=1, columnspan=3)
        
        tk.Label(self.tkcommand_frame.interior, text="Command",font="monospace 16").grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Label(self.tkcommand_frame.interior, text="Args",font="monospace 16").grid(row=1, column=2, columnspan=2, sticky="ew")

        
        # Main Button Loop
        for i, command in enumerate(self.command_files):
            args_entry = create_textbox(self.tkcommand_frame.interior, [""], font="monospace 8")
            args_entry.grid(row=2 + i, column=3, sticky="ew")
            tk.Button(self.tkcommand_frame.interior,text=f"{command}", font="monospace 9", command=lambda entry=args_entry, x=command:self.run_command(x, entry)
                      ).grid(row=2 + i, column=0, columnspan=3, sticky="nswe")
            
            
        # self.tkroot mainloop
        self.tkroot.mainloop()
    
    def run_command(self, command, entry):
        print(command)        
        
        try:
            self.tkconsole.insert("end", f"\nIN: run_command {command} - ARGS: {entry.get()} \nOUT:\n")
            self.imported_commands[command].func(self.__dict__, *entry.get().split(" "))
        except KeyError:
            self.pyconsole.print(f"Invailed Command {command}", level=2)
    
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    XVFiles(YAMLCFG)
