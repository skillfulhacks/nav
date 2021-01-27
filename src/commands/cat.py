#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Displays Text File - Usage: cat <path>"""

def func(root, display, *args, **kwargs):
    import os
    path = os.path.join(root["cwd"], args[0])
    try:
        with open(path, "r") as f:
            file = f.read().split("\n")
    except IsADirectoryError:
        display.insert("end", f"{path} Is A Directory!")
    except FileNotFoundError:
        display.insert("end", f"File {path} Not Found!")
    except UnicodeDecodeError as e:
        display.insert("end", e)
    try:
        for line in file:
            display.insert("end", line)
    except UnboundLocalError:
        pass
    