#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lists CWD - Usage: ls"""

def func(root, *args, **kwargs):
    import os
    for item in os.listdir(root["cwd"]):
        root["tkconsole"].insert("end", item)
        if os.path.isdir(f"{root['cwd']}/{item}"):
            root["tkconsole"].insert("end", f"{''.join([' ' for ch in range(30) if len(item) + ch < 30])}(dir)", sep="")
        else:
            root["tkconsole"].insert("end", f"{''.join([' ' for ch in range(30) if len(item) + ch < 30])}(file)", sep="")
