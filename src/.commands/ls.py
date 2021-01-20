#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(root, *args, **kwargs):
    import os
    for item in os.listdir(root["cwd"]):
        root["tkconsole"].insert("end", f"\n{item}")
    
doc = """Lists CWD"""
