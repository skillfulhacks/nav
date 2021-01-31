#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Runs a xvs(XVSript) file - Usage: rm_env_var <path|@command> [sep="\n"] [display=cmdout_console]"""
imports = ("os")
reqcoms = ("run_command")

def func(root, display, *args, **kwargs):
    import os
    try:
        display = kwargs["out_con"]
    except KeyError:
        display = "cmdout_console"
        
    path = args[0]
    
    if path[0] == "@":
        # WIP
        pass
    else:
        try:
            with open(os.path.join(root["cwd"], path), "r") as f:
                file = f.read()
        except IsADirectoryError:
            display.insert("end", f"{os.path.join(root['cwd'], path)} Is a Directory")
            return 0
        except FileNotFoundError:
            display.insert("end", f"No File {os.path.join(root['cwd'], path)} Found")
        
        
        header = file.split("@START")[0]
        
        for line in header.split("@"):
            
            if line.startswith("SEP"):
                line_sep =  line.split("=")[1].replace("\n", "")
                
                
        body = file.split("@START")[1]
        code_lines = body.split("@END")[0] if isinstance(file.split("@END"), list) else body
        
        # Line Separator
        try:
            line_sep = kwargs["sep"]
        except KeyError:
            try:
                line_sep = line_sep
            except UnboundLocalError:
                line_sep = "\n"
        if line_sep == "\\n": line_sep = "\n"
        
        # Run
        for line in code_lines.split(line_sep):
            if line != "":
                root["run_command"](root, 
                                      root["loaded_tabs"][display], 
                                      line.split(" ")[0] if isinstance(line.split(" "), list) else line, 
                                      line.split(" ")[1:] if isinstance(line.split(" "), list) else [],
                                      do_run_info=0)
        
        