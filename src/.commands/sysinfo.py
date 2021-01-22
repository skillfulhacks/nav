#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(root, *args, **kwargs):
    import platform as pf
    root["tkconsole"].insert("end","Listing divice info...")
    root["tkconsole"].insert("end",f"Current OS:   {pf.system()}\nProcessor:   {pf.processor()}\nMachine:   {pf.machine()}\nArchitecture:   {pf.architecture()}\nNetwork:   {pf.node()}")
    root["tkconsole"].insert("end","Done!")
            
__doc__ = """Lists divice info."""
