#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Prints a Internal Var - Usage: pinternal <var>"""

def func(root, *args, **kwargs):
    # Holy Crap This Got Out Of Hand
    def print_to_console(indent, text, prefix):
        try:
            root["tkconsole"].pprint(indent + text + f"{''.join([' ' for ch in range(60) if len(indent + text) + ch < 60])} ({prefix})")
        except TypeError:
            text = str(text)
            root["tkconsole"].pprint(indent + text + f"{''.join([' ' for ch in range(60) if len(indent + text) + ch < 60])} (class)")
  
    def list_recursion(lis, list_indent=""):
        for item in lis:
            if isinstance(item, dict):
                recursion(item.items(), list_indent + "  ")
            elif isinstance(item, list):                        
                print_to_console(list_indent, "-", "list")
                list_recursion(item, list_indent + "  ")
            else:
                print_to_console(list_indent, item, "str")
    
    def recursion(items, indent=""):            
        for key, value in items:
            if isinstance(value, dict):
                print_to_console(indent, key, "dict")
                recursion(value.items(), indent + "  ")
                
            elif isinstance(value, list):
                print_to_console(indent, key, "list")
                list_recursion(value, indent + "  ")
                
            else:
                print_to_console(indent, f"{key} - {value}", "k/v")
    try:
        if isinstance(root[args[0]], dict):
            recursion(root[args[0]].items())
        elif isinstance(root[args[0]], list):
            list_recursion(root[args[0]])
        else:
            print_to_console("", root[args[0]], "str")
    except KeyError:
        root["tkconsole"].pprint(f"Unknown Var: {args[0]}")
