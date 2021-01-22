#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """This lists all files in XV's current set directory."""

def func(root, *args, **kwargs):
    import os
    root["tkconsole"].insert("end","Listing all files in XV's current set directory...\n")
    for item in os.listdir(root["cwd"]):
        try:
            os.chdir(item)
            root["tkconsole"].insert("end", f"Folder: {item}")
            os.chdir("..")
        except NotADirectoryError:
            root["tkconsole"].insert("end", f"File: {item}")
   
            
