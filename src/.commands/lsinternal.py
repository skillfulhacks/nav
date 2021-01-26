#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lists All Internal Vars - Usage: lsinternal"""
# Not in Use atm
DEPS = ("pinternal")

def func(root, *args, **kwargs):
    for key in root.keys():
        root["tkconsole"].pprint(f"[{key}]")
        root["imported_commands"]["pinternal"].func(root, key)
        root["tkconsole"].pprint("")
