#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Removes a Envirorment Var - Usage: rm_env_var <key>"""
imports = ()
reqcoms = ()

def func(root, display, *args, **kwargs):
    try:
        del root["env_vars"][args[0]]
        display.insert("end", f"Removed {args[0]}")
    except KeyError:
        display.insert("end", f"Unknown Key {args[0]}")
    except IndexError:
        pass