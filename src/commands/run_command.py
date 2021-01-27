#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INTERNAL RUNS A COMMAND - Usage: run_command <arg 1> ... <arg n>"""
INTERNAL=True

def func(root, display, *args, **kwargs):
    # command name
    command = args[0]
    try:
        args = args[1]
    except IndexError:
        args = ()
    print(args)
    if isinstance(args, str):
        args = [args]
    
    # Checks if the Command is Valid
    display.insert("end", f"IN: run_command {command} - ARGS: {' '.join(list(args))} \nOUT:")
    for key, value in root["cfg"]["commands"]["atlases"].items():
        if command == key:
            command = value
            break
        
    if command not in list(root["imported_commands"].keys()):
        display.insert("end", f"[ Error ] Unknown Command {command}")
        return
    
    root["imported_commands"][command].func(root, display, *args)
    display.insert("end", "")
        
    
    # Updates Tabs
    for item in root["loaded_tabs"].values():
        item.update()