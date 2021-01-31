#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:19:32 2021

@author: clarence
"""

class Console():
    def __init__(self):
        pass
    def print(self, text, level=1):
        if level == 1:
            level_text = "[  OK  ]"
        elif level == 2:
            level_text = "[ WARN ]"
        elif level == 3:
            level_text = "[ ERR  ]"
        print(f"{level_text} {text}")
        return f"{level_text} {text}"