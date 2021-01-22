#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Displays Help For Selected Command; Usage - man <command>"""

def func(root, *args, **kwargs):
    root["tkconsole"].insert("end", root["imported_commands"][args[0]].__doc__, sep="")
    
