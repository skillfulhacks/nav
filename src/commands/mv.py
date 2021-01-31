#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cuts a File - Usage: mv <src> <dst>"""
imports = ("shutil", "os")
reqcoms = ("cp")

def func(root, display, *args, **kwargs):
    import shutil
    import os
    
    try:
        src = os.path.join(root["cwd"], args[0])
        dst = os.path.join(root["cwd"], args[1])
    except IndexError:
        display.insert("end", "Invalid Arg Usage; cp, <src> <dst>")
        return 0
    try:
        root["imported_commands"]["cp"].func(root, display, src, dst)
        if os.path.isfile(src):
            os.remove(src)
            
        elif os.path.isdir(src):
            shutil.rmtree(src)
            
        display.insert("end", f"Removed {src}")
        
    except IOError as e:
        display.insert("end", e)