#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Displays Help For Selected Command; Usage - man <command>"""

def func(root, display, *args, **kwargs):
    display.insert("end", root["imported_commands"][args[0]].__doc__, sep="")
    
    