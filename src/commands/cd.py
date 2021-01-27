#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Changes CWD - Usage: cd <path>"""

def func(root, display, *args, **kwargs):
    import os
    try:
        path = args[0]
        restore = root["cwd"]
    
        if root["slash"] in (path[0], path[0:1]):
            root["cwd"] = path
        elif path == "..":
            root["cwd"] = f'{root["slash"].join(root["cwd"].split(root["slash"])[:-1])}'
        else:
            root["cwd"] = f'{root["cwd"]}/{path}'
            
        if os.path.isdir(root["cwd"]):
            display.insert("end", f"Path Changed to {root['cwd']}")
        else:
            display.insert("end", f"Unknown Path {root['cwd']}")
            root["cwd"] = restore
    except IndexError:
        root["cwd"] = root["root_path"]
    