#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTERNAL RUNS A COMMAND - Usage: run_command <arg 1> ... <arg n>"""
INTERNAL=True

def func(root, *args, **kwargs):
    command = args[0]
    try:
        args = args[1]
    except IndexError:
        args = ()
    print(args)
    if isinstance(args, str):
        args = [args]
        
    if command not in list(root["imported_commands"].keys()):
        root["tkconsole"].insert("end", f"\n Unknown Command {command}\n")
        
    try:
        root["tkconsole"].insert("end", f"\nIN: run_command {command} - ARGS: {' '.join(list(args))} \nOUT:\n")
        root["imported_commands"][command].func(root, *args)
    except KeyError:
        root["pyconsole"].print(f"Invailed Command {command}", level=2)
