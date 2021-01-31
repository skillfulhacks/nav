#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Changes CWD - Usage: cd <path>"""

def func(root, display, *args, **kwargs):
    import os
    try:
        path = args[0]
        restore = root["cwd"]
        if path == "..":
            root["cwd"] = os.path.dirname(root["cwd"])
        else:
            root["cwd"] = os.path.join(root["cwd"], path)
            
        if os.path.isdir(root["cwd"]):
            display.insert("end", f"Path Changed to {root['cwd']}")
        else:
            display.insert("end", f"Unknown Path {root['cwd']}")
            root["cwd"] = restore
    except IndexError:
        root["cwd"] = root["root_path"]
    