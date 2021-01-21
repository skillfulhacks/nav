#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(root, *args, **kwargs):
    import os
    root["tkconsole"].insert("end","Listing all files in XV's current set directory:\n")
    for item in os.listdir(root["cwd"]):
        try:
            os.chdir(item)
            root["tkconsole"].insert("end", f"\nFolder: {item}")
            os.chdir("..")
        except NotADirectoryError:
            root["tkconsole"].insert("end", f"\nFile: {item}")
            
doc = """Lists CWD"""
