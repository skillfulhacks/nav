#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Echos A Input - Usage: Echo <text>"""
imports = ()
reqcoms = ()

def func(root, display, *args, **kwargs):
    display.insert("end", "")
    for arg in args:
        if arg == "\\n":
            
            display.insert("end", "")
        else:
            display.insert("end", arg, sep="")
