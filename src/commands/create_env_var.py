#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Create a Envirorment Var - Usage: create_env_var <name> <value>"""
imports = ("ast")
reqcoms = ()

def func(root, display, *args, **kwargs):
    import ast
    try:
        root["env_vars"].update({args[0]: ast.literal_eval(
            f'"{args[1]}"')})
        display.insert("end", f"Added ENV Var: {args[0]} - {args[1]}")
    except SyntaxError:
        display.insert("end", f"Invalid Syntax: {args[1]}")