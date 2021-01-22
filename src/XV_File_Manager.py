# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import sys

import yaml

import tkinter as tk
from tkinter import ttk

from tk_custum_widgets import TKConsole
from console import Console

     
class XVFiles():
    def chdir(self, newdir):
        os.chdir(newdir)
        self.cwd = newdir
    def __init__(self, yaml_cfg):
        #%% setup
        self.pyconsole = Console()
        self.update_funcs = []
        self.root_path = os.getcwd()
        self.cwd = self.root_path
        
        # Operating System Type
        self.optype = os.name
        
        self.chdir(f"{self.root_path}/.config")
        self.slash = "\\" if self.optype == "nt" else "/"

        
        # COMMANDS_DIR AND LIST_OF_COMMANDS
        self.commands_dir = f"{self.root_path}{self.slash}.commands"
        self.tabs_dir = f"{self.root_path}{self.slash}gui_tabs"
        # Adds Command Dir to Sys Path. Allowing Import from Non Standerd Paths
        sys.path.append(self.commands_dir)
        sys.path.append(self.tabs_dir)
        
        self.chdir(self.commands_dir)
        
        #%% Importer ###
        self.command_files = [command.split(".")[0] for command in os.listdir(self.commands_dir) if os.path.isfile(f"{self.commands_dir}/{command}")]
        self.imported_commands = {}
        for i, command in enumerate(self.command_files):
            try:
                self.imported_commands.update({command: __import__(command)})
            except FileNotFoundError:
                self.pyconsole.print(f"invalid command {command}!")
                
        #! Sets run_command to the imported run_command
        try:
            self.run_command = self.imported_commands["run_command"].func
        except KeyError:
            self.pyconsole.print("run_command.py not found exiting", level=3)
            sys.exit()
        
        ## Imports Tabs
        self.tabs_files = [tab.split(".")[0] for tab in sorted(os.listdir(self.tabs_dir)) if os.path.isfile(f"{self.tabs_dir}/{tab}")]
        self.imported_tabs = {}
        for i, tab in enumerate(self.tabs_files):
            try:
                self.imported_tabs.update({tab: __import__(tab)})
                print(self.imported_tabs)
            except FileNotFoundError:
                self.pyconsole.print(f"invalid tab {tab}!")
        
        #%% Create a tkinter screen named self.tkroot
        #################
        ### GUI START ###
        #################
        
        self.tkroot = tk.Tk()
        self.tkroot.title("XV File Manager")
        self.tkroot.resizable(False, False)
        
        #%% Input Frame ###
        self.tkinput_frame_tabs = ttk.Notebook(self.tkroot)
        self.tkinput_frame_tabs.grid(row=0, column=0)
        
        # Loads in Tabs
        for key, item in self.imported_tabs.items():
            loaded_tab = item.Tab(self.__dict__, self.tkinput_frame_tabs)
            loaded_tab.grid(column=0, row=0, rowspan=100)
            self.tkinput_frame_tabs.add(loaded_tab, text=item.NAME)

        #%% Output Frame ###
        self.tkoutput_frame = ttk.Frame(self.tkroot)
        self.tkoutput_frame.grid(row=0, column=1)
            
        # Creates Console
        self.tkconsole_frame = tk.Frame(self.tkoutput_frame)
        self.tkconsole_frame.grid(column=1, row=0, rowspan=100)
        
        self.tkconsole = TKConsole(self.tkconsole_frame, width=80, height=24, wrap=tk.NONE, font='monospace 10', bg="black")
        self.tkconsole.grid(column=0, row=0, rowspan=100)
        
        # Mainloop
        self.tkroot.mainloop()

    #%%
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    XVFiles(YAMLCFG)
