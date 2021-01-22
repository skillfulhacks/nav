#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lists CWD - Usage: ls"""

def func(root, *args, **kwargs):
    import os
    for item in os.listdir(root["cwd"]):
        if os.path.isdir(f"{root['cwd']}/{item}"):
            root["tkconsole"].insert("end", f"{item} (dir)")
        else:
            root["tkconsole"].insert("end", f"File: {item}")
