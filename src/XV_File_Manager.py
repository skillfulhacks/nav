# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import sys

import yaml

import tkinter as tk
from tkinter import ttk
from pyassets.pyconsole import Console

     
class XVFiles():
    #%%
    def load_tab(self, name, tab):
        
        # If the Tab is Loaded Exit
        if name in list(self.loaded_tabs.keys()):
            return None
        
        # Check All Requided Tabs
        try:
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
        except AttributeError:
            # If the Tab is Formated Wrong it Passes
            self.pyconsole.print(f"Tab File {name} is Invalidly Formated", level=2)
            return None
        loaded_tab = tab.Tab(self.__dict__, self.tkcoreframes[tab.CFG.defualt_side]["obj"])

        # If the Tab Starts Active
        if tab.CFG.active_on_start: 
            loaded_tab.grid(column=0, row=0, rowspan=100)
            self.tkcoreframes[tab.CFG.defualt_side]["obj"].add(loaded_tab, text=tab.CFG.tab_name)

        self.loaded_tabs.update({name: loaded_tab})
        
    #%%
    def import_from_dir(self, dir_path, sortlist=None, exclude=[]):
        """Imports a Dir of Files"""
        files = [file.split(".")[0] for file in os.listdir(dir_path) if os.path.isfile(f"{dir_path}/{file}") and file.split(".")[0] not in exclude]
        
        # For Custum Sorting
        if sortlist != None:
            sortedfiles = []
            
            
            for sortkey in reversed(sortlist):
                for i, file in enumerate(files):
                    if sortkey == file:
                        sortedfiles.insert(0, file)
                        break
            else:
                sortedfiles.extend([file for file in files if file not in sortedfiles])
            files = sortedfiles
        imported = {}
        for i, file in enumerate(files):
            try:
                imported.update({file: __import__(file)})
            except FileNotFoundError:
                self.pyconsole.print(f"invalid command {file}!")
        return imported
    #%%
    def tab_update(self, event):
        for item in self.loaded_tabs.values():
            item.update()

    def __init__(self, yaml_cfg):
        #%% setup
        self.pyconsole = Console()
        self.root_path = os.getcwd()
        self.cwd = self.root_path
        self.cfg = yaml_cfg
        # Envirorment Varables
        self.env_vars = {}
        # Operating System Type
        self.optype = os.name
        #self.slash = "\\" if self.optype == "nt" else "/"

        
        # COMMANDS_DIR AND LIST_OF_COMMANDS
        self.commands_dir = os.path.join(self.root_path, "commands")
        self.tabs_dir = os.path.join(self.root_path, "gui_tabs")
        
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
        self.tkmenu = tk.Menu(self.tkroot)
        self.tkroot.config(menu=self.tkmenu)
        
        #%% Input Frame ###
        self.tkcoreframes = {
            "LEFT": 
                {
                "obj": ttk.Notebook(self.tkroot),
                "gridkwargs": {"row": 0, "column": 0}
                },
            "RIGHT": 
                {
                "obj": ttk.Notebook(self.tkroot),
                "gridkwargs": {"row": 0, "column": 1}
                }
        }
            
        for key, item in self.tkcoreframes.items():
            item["obj"].grid(**item["gridkwargs"])
            item["obj"].bind("<<NotebookTabChanged>>", self.tab_update)

        # Loads in Tabs
        self.loaded_tabs = {}
        for name, tab in self.imported_tabs.items():
            self.load_tab(name, tab)
            
        self.update_menu()
        # Mainloop
        self.tkroot.mainloop()
    

    def update_menu(self):
        #!!! WIP ####
        def run_com(key, menu, event, *args, **kwargs):
            print(key, menu, event)
            if event == "delete":
                self.loaded_tabs[key].grid_forget()
                del self.loaded_tabs[key]
                self.update_menu()
                
        self.tkmenu = tk.Menu(self.tkroot)
        self.tkroot.config(menu=self.tkmenu)
        tab_menu = tk.Menu(self.tkmenu, tearoff=0)
        tab_menu_left = tk.Menu(tab_menu, tearoff=0)
        tab_menu_right = tk.Menu(tab_menu, tearoff=0)
        
        loaded_tabs_cascades = {}
        for key, item in self.loaded_tabs.items():
            
            if self.imported_tabs[key].CFG.defualt_side == "LEFT":
                loaded_tabs_cascades.update({key: tk.Menu(tab_menu_left, tearoff=0)})
                tab_menu_left.add_cascade(label=key, menu=loaded_tabs_cascades[key])
                
            elif self.imported_tabs[key].CFG.defualt_side == "RIGHT":             
                loaded_tabs_cascades.update({key: tk.Menu(tab_menu_right, tearoff=0)})
                tab_menu_right.add_cascade(label=key, menu=loaded_tabs_cascades[key])
        
        for key, item in loaded_tabs_cascades.items():
            item.add_command(label="Delete", command=lambda k=key, it=item, event="delete": run_com(k, it, event))
            
        tab_menu.add_cascade(label="Left", menu=tab_menu_left)
        tab_menu.add_cascade(label="Right", menu=tab_menu_right)
        
        
        self.tkmenu.add_cascade(label="Tabs", menu=tab_menu)

#%%
if __name__ == "__main__":
    with open("xvrc.yaml") as file:
        YAMLCFG = yaml.load(file, Loader=yaml.FullLoader)
    XVFiles(YAMLCFG)