#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Displays Help - Req man - Usage: help"""

def func(root, *args, **kwargs):
    print(root["imported_commands"].keys())
    for command in list(root["imported_commands"].keys()):
        try:
            if root["imported_commands"][command].INTERNAL:
                continue
        except AttributeError:
            pass
        print(command)
        root["tkconsole"].insert("end", f"{command}: ")
        root["imported_commands"]["man"].func(root, command)
