 -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import sys

import yaml


import tkinter as tk
from tkinter import ttk
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

class TKConsole(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """A Scrollable Custum Tk Text Widget"""
        tk.Frame.__init__(self, parent)
        self.text = tk.Text(self, *args, **kwargs)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure(xscrollcommand=self.hsb.set)
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.text.pack(side="left", fill="x", expand=True)

        # expose some text methods as methods on this object
        self.insert = self._insert
        self.delete = self.text.delete
        self.mark_set = self.text.mark_set
        self.get = self.text.get
        self.index = self.text.index
        self.search = self.text.search
    
    def _insert(self, pos, text, *args, **kwargs):
        self.text.insert(pos, "\n" + text, *args, **kwargs)
        
        self.text.see("end")
        
class xv_files():
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
        #self.tkroot.geometry('500x400')
        self.tkroot.title("XV File Manager")
        
        self.tkcommand_frame = tk.Frame(self.tkroot)
        self.tkcommand_frame.grid(column=0, row=0)
        
        # Creates Console
        # BTW I dont really know how this works
        self.tkconsole_frame = tk.Frame(self.tkroot)
        self.tkconsole_frame.grid(column=1, row=0, rowspan=100)
        self.tkconsole = TKConsole(self.tkconsole_frame, width=50, height=25, wrap=tk.NONE, font='monospace 10')
        self.tkconsole.pack(side=tk.TOP, fill=tk.X)

        # Create a Entrybox with CWD inserted
        tk.Label(self.tkcommand_frame,text="set directory: ",font="monospace 8").grid(row=0,column=0)
        set_dir_entry = create_textbox(self.tkcommand_frame, [self.root_path], 0, 1, font="monospace 8", width=60)
    
        tk.Label(self.tkcommand_frame,text="Args:",font="monospace 8").grid(row=1,column=0)
        self.tkargs_combobox = create_textbox(self.tkcommand_frame, [""], 1, 1, font="monospace 8", width=60)
        # Main Button Loop
        for i, command in enumerate(self.command_files):
            tk.Label(self.tkcommand_frame,text=command,font="monospace 10",fg="darkblue").grid(row=2 + i,column=0,sticky="nswe")
            tk.Button(self.tkcommand_frame,text=f"Run {command}", font="monospace 9", command=lambda x=command:self.run_command(x)).grid(row=2 + i,column=1 ,sticky="nswe")
            
            
        # self.tkroot mainloop
        self.tkroot.mainloop()
    
    def run_command(self, command):
        print(command)        
        
        try:
            self.tkconsole.insert("end", f"\nRunCommmand {command} - ARGS: {self.tkargs_combobox.get()} \nOUT:")
            self.imported_commands[command].func(self.__dict__, *self.tkargs_combobox.get().split(" "))
        except KeyError:
            self.pyconsole.print(f"Invailed Command {command}", level=2)
    
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    xv_files(YAMLCFG)
