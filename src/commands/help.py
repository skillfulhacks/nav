#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Displays Help - Req man - Usage: help"""

def func(root, display, *args, **kwargs):
    print(root["imported_commands"].keys())
    for command in list(root["imported_commands"].keys()):
        try:
            if root["imported_commands"][command].INTERNAL:
                continue
        except AttributeError:
            pass
        print(command)
        display.insert("end", f"{command}: ")
        root["imported_commands"]["man"].func(root, display, command)