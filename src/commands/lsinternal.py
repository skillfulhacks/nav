#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lists All Internal Vars - Usage: lsinternal"""
# Not in Use atm
DEPS = ("pinternal")

def func(root, display, *args, **kwargs):
    for key in root.keys():
        display.pprint(f"[{key}]")
        root["imported_commands"]["pinternal"].func(root, display, key)
        display.pprint("")