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
    #%%
    def load_tab(self, name, tab):
        
        # If the Tab is Loaded Exit
        if name in list(self.loaded_tabs.keys()):
            return None
        
        # Check All Requided Tabs
        for reqtab in tab.CFG.reqtabs:
            # The First Value in tab.CFG.reqtabs should be None Becuase of How Loop Tuples Works
             if reqtab == None:
                continue
             # If Requided Tab is Load Continue
             # Else Load the Req Tab
             if reqtab in list(self.loaded_tabs.keys()):
                 continue
             else:
                 self.load_tab(reqtab, self.imported_tabs[reqtab])
        try:
            # Do Sides
            if tab.CFG.defualt_side == "LEFT":
                loaded_tab = tab.Tab(self.__dict__, self.tkinput_frame_tabs)
            elif tab.CFG.defualt_side == "RIGHT":
                loaded_tab = tab.Tab(self.__dict__, self.tkoutput_frame)
        
        except AttributeError:
            # If the Tab is Formated Wrong it Passes
            self.pyconsole.print(f"Tab File {name} is Invalidly Formated", level=2)
            return None
        
        # If the Tab Starts Active
        if tab.CFG.active_on_start: 
            loaded_tab.grid(column=0, row=0, rowspan=100)
            if tab.CFG.defualt_side == "LEFT":
                self.tkinput_frame_tabs.add(loaded_tab, text=tab.CFG.tab_name)
                
            elif tab.CFG.defualt_side == "RIGHT":
                self.tkoutput_frame.add(loaded_tab,     text=tab.CFG.tab_name)
            
        self.loaded_tabs.update({name: loaded_tab})
   
    #%%
    def import_from_dir(self, dir_path, sortlist=None, exclude=[]):
        """Imports a Dir of Files"""
        files = [file.split(".")[0] for file in os.listdir(dir_path) if os.path.isfile(f"{dir_path}/{file}") and file.split(".")[0] not in exclude]
        
        # For Custum Sorting
        if sortlist != None:
            sortedfiles = []
            
            for i, file in enumerate(files):
                for sortkey in reversed(sortlist):
                    if sortkey == file:
                        sortedfiles.insert(0, file)
                        files.pop(i)
                        break
            else:
                sortedfiles.extend(files)
            files = sortedfiles
        imported = {}
        for i, file in enumerate(files):
            try:
                imported.update({file: __import__(file)})
            except FileNotFoundError:
                self.pyconsole.print(f"invalid command {file}!")
        return imported
    
    def __init__(self, yaml_cfg):
        #%% setup
        self.pyconsole = Console()
        self.root_path = os.getcwd()
        self.cwd = self.root_path
        self.cfg = yaml_cfg
        
        # Operating System Type
        self.optype = os.name
        self.slash = "\\" if self.optype == "nt" else "/"

        
        # COMMANDS_DIR AND LIST_OF_COMMANDS
        self.commands_dir = f"{self.root_path}{self.slash}commands"
        self.tabs_dir = f"{self.root_path}{self.slash}gui_tabs"
        
        #%% Importer ###
        # Adds Import Paths to Sys Path. Allowing Imports from Non Standerd Paths
        for plist in self.cfg["startup"]["paths"]:
            for path in plist:
                sys.path.insert(0, path)
    
                
        self.imported_commands = self.import_from_dir(self.commands_dir, self.cfg["commands"]["order"], self.cfg["commands"]["exclude"])
        # Sets run_command to a Custum Var
        try:
            self.run_command = self.imported_commands["run_command"].func
        except KeyError:
            self.pyconsole.print("run_command.py not found exiting", level=3)
            sys.exit()
            
        ## Imports Tabs
        self.imported_tabs = self.import_from_dir(self.tabs_dir, self.cfg["tabs"]["order"], self.cfg["tabs"]["exclude"])
        
        
        #%%##############
        ### GUI START ###
        #################'
        
        self.tkroot = tk.Tk()
        self.tkroot.title("XV File Manager")
        self.tkroot.resizable(False, False)
        
        #%% Input Frame ###
        self.tkinput_frame_tabs = ttk.Notebook(self.tkroot)
        self.tkinput_frame_tabs.grid(row=0, column=0)
        
         #%% Output Frame ###
        self.tkoutput_frame = ttk.Notebook(self.tkroot)
        self.tkoutput_frame.grid(row=0, column=1)
        
        # Loads in Tabs
        self.loaded_tabs = {}
        for name, tab in self.imported_tabs.items():
            self.load_tab(name, tab)
            
        # Mainloop
        self.tkroot.mainloop()
    



#%%
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    XVFiles(YAMLCFG)
