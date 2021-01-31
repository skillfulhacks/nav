#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import os
from pyassets.tk import TKListbox, create_combobox

class CFG:
    tab_name="File GUI"
    defualt_side="LEFT"
    active_on_start=True
    output_tab="cmdout_console"
    reqcoms=(None, "run_command")
    reqtabs=(None, "cmdout_console")
    
class Tab(tk.Frame):
    def __init__(self, root, tkroot):
        
        def delete_recursion(path, index, delete_pos):
            # Looks At All Files in The Path
            for i, item in enumerate(path):
                # If File is a Opened Dir run delete_recursion agian on it
                if self.meta_data[i + index + 1]["opened"] == True:
                    delete_recursion(os.listdir(os.path.join(root["cwd"], self.meta_data[i + index + 1]["path"])), i + index + 1, delete_pos)
                # Add item to Que
                delete_pos.append(i + index + 1)
                
        def get_dir_items(event):
            index = self.box.curselection()[0]
            index_meta_data = self.meta_data[index]
            # Pass if Path is File
            if os.path.isfile(os.path.join(root["cwd"], index_meta_data['path'])):
                pass
            else:
                if index_meta_data["opened"] == False:
                    try:
                        for i, item in enumerate(os.listdir(os.path.join(root["cwd"], index_meta_data['path']))):
                            self.meta_data.insert(i + index + 1, {"path": os.path.join(index_meta_data['path'], item),
                                                                  "indent_level": f"{index_meta_data['indent_level']}  ",
                                                                  "opened": False
                                                                  
                                                                  })
                            if os.path.isdir(os.path.join(root["cwd"], self.meta_data[i + index + 1]["path"])):
                                self.box.insert(i + index + 1, f"{index_meta_data['indent_level']}> {item}")
                            else:
                                self.box.insert(i + index + 1, f"{index_meta_data['indent_level']}  {item}")
                        index_meta_data["opened"] = True
                    except PermissionError as e:
                        root["loaded_tabs"][CFG.output_tab].insert("end", e)
                        
                    
                elif index_meta_data["opened"] == True:
                    delete_pos = []
                    delete_recursion(os.listdir(os.path.join(root["cwd"], index_meta_data['path'])), index, delete_pos)
                    # Delete Que
                    for pos in reversed(sorted(delete_pos)):
                        self.meta_data.pop(pos)
                        self.box.delete(pos)
                        
                    index_meta_data["opened"] = False
        
        def cd(new_dir):
            if os.path.isdir(os.path.join(root["cwd"], new_dir)):
                root["cwd"] = os.path.join(root["cwd"], new_dir)
                self.current_dir.set(os.path.join(root["cwd"], new_dir))
                self.update()
        tk.Frame.__init__(self, tkroot)
        self.root = root
        self.last_cwd = None
        # Current Dir Textbox
        self.past_dirs = [self.root["cwd"]]
        self.current_dir = create_combobox(self, self.past_dirs, width=40)
        self.current_dir.grid(column=0, row=0, rowspan=2, columnspan=2)
        
        
        tk.Button(self, text="Change Dir", command=lambda: cd(self.current_dir.get())).grid(column=2, row=0, rowspan=1, columnspan=1, sticky="ew")
        tk.Button(self, text="Up Level"  , command=lambda: cd(os.path.dirname(root["cwd"]))).grid(column=3, row=0, rowspan=1, columnspan=1, sticky="ew")
        tk.Button(self, text="Goto Dir"  , command=lambda: cd(self.meta_data[self.box.curselection()[0]]["path"])).grid(column=2, row=1, rowspan=1, columnspan=1, sticky="ew")
        tk.Button(self, text="Open File" , command=lambda: root["run_command"](root, # Root Standed In Any Command
                                                                               root["loaded_tabs"][CFG.output_tab],  # Display Standerd in Any Command
                                                                               "cat",  # Cat Command Name
                                                                               os.path.join(root["cwd"], self.meta_data[self.box.curselection()[0]]["path"])) # Path to File
                  ).grid(column=3, row=1, rowspan=1, columnspan=1, sticky="ew")
        # File GUI
        self.box = TKListbox(self, width=80, height=24)
        self.box.grid(column=0, row=2, rowspan=8, columnspan=4)
        # Update
        self.update()
        
        self.box.bind('<ButtonRelease-1>', get_dir_items)

        
    def update(self):
        if self.root["cwd"] not in self.past_dirs:
            self.past_dirs.append(self.root["cwd"])
            self.current_dir["values"] = self.past_dirs
            self.current_dir.set(self.past_dirs[-1])
        
        if self.root["cwd"] != self.last_cwd:
            self.box.delete(0, "end")
            self.meta_data = []
            
            for i, item in enumerate(os.listdir(self.root["cwd"])):
                self.box.insert(i, item)
                self.meta_data.insert(i, {
                    "path": item,
                    "indent_level": "  ",
                    "opened": False
                    })
            self.last_cwd = self.root["cwd"]