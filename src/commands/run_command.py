#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""INTERNAL RUNS A COMMAND - Usage: run_command <arg 1> ... <arg n> [do_run_info=1]"""

INTERNAL = True

def func(root, display, *args, **kwargs):
    # command name
    command = args[0]
    consoleout = []
    try:
        # Test For Index Air
        args = args[1]
    # If no Args A Selected Set args to a Empty Tuple
    except IndexError:
        args = []
        
    out_args = []
    out_kwargs = {}
    
    # Procces Raw Command
    for arg in args:
        if arg == '':
            continue
        
        if "=" in arg:
            out_kwargs.update({arg.split("=")[0]: arg.split("=")[1]})
            continue
        if arg[0] == "$":
            try:
                arg = root["env_vars"][arg[1:]]
            except KeyError:
                consoleout.append(root["pyconsole"].print(f"Unknown ENV Var {arg[1:]}!", level=2))
                continue
            
        elif arg[0] == "#":
            try:
                arg = root[arg[1:]]
            except KeyError:
                consoleout.append(root["pyconsole"].print(f"Unknown Internal Var {arg[1:]}!", level=2))
                continue
            
        out_args.append(arg)
    
    # Checks if the Command is Valid
    sep = "\n"
    try:
        if kwargs["do_run_info"]:
            display.insert("end", f"IN: run_command {command} - ARGS: {' '.join(out_args)}{sep.join(consoleout)} \nOUT:")
        else:
            pass
    except KeyError:
        display.insert("end", f"IN: run_command {command} - ARGS: {' '.join(out_args)}{sep.join(consoleout)} \nOUT:")
        
    for key, value in root["cfg"]["commands"]["atlases"].items():
        if command == key:
            command = value
            break
        
    if command not in list(root["imported_commands"].keys()):
        display.insert("end", f"[ Error ] Unknown Command {command}")
        return
    
    root["imported_commands"][command].func(root, display, *out_args)
            
    
    # Updates Tabs
    for item in root["loaded_tabs"].values():
        item.update()