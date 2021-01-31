#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copies a File - Usage: cp <src> <dst>"""
imports = ("shutil", "os")
reqcoms = ()

def func(root, display, *args, **kwargs):
    import shutil
    import os
    def copytree(src, dst, symlinks=False, ignore=None):
        # Source:
        # https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth @ Mital Vora
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copytree(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)
    try:
        src = os.path.join(root["cwd"], args[0])
        dst = os.path.join(root["cwd"], args[1])
    except IndexError:
        display.insert("end", "Invalid Arg Usage; cp, <src> <dst>")
        return 0
    try:
        
        if os.path.isfile(src):
            shutil.copy2(src, dst)
        elif os.path.isdir(src):
            copytree(src, dst)
            
        display.insert("end", f"Copyed {src} -> {dst}")
        
    except IOError as e:
        display.insert("end", e)
