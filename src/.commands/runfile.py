#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """Runs targeted file."""

def func(root, *args, **kwargs):
    import os
    root["tkconsole"].insert("end",f"Opening {args[0]}...")
    try:
        os.startfile(args[0]) if os.name == 'nt' else  os.system(args[0])
    except FileNotFoundError:
        root["tkconsole"].insert("end","ERROR: File does not exist or directory\nwith extension was not listed in 'args'")
    root["tkconsole"].insert("end","Done!")
            
