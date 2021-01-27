#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Lists CWD - Usage: ls"""

def func(root, display, *args, **kwargs):
    import os
    
    for item in os.listdir(root["cwd"]):
        file_stats = os.stat(f'{root["cwd"]}{root["slash"]}{item}')
        # File Permissons
        perms = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        for i, sec in enumerate(str(oct(file_stats.st_mode)[-3:])):
            if int(sec) == 7 or int(sec) == 5 or int(sec) == 3 or int(sec) == 1:
                perms[i][2] = "e"
            if int(sec) == 7 or int(sec) == 6 or int(sec) == 3 or int(sec) == 2:
                perms[i][1] = "w"
            if int(sec) == 7 or int(sec) == 6 or int(sec) == 5 or int(sec) == 4:
                perms[i][0] = "r" 
            perms[i] = ''.join(perms[i])
        perms = ''.join(perms)
        
        display.insert("end", f"{perms} {file_stats.st_size}{''.join([' ' for ch in range(15) if len(str(file_stats.st_size)) + ch < 15])} {item}") 
        
        if os.path.isdir(f"{root['cwd']}{root['slash']}{item}"):
            display.insert("end", f"{''.join([' ' for ch in range(35) if len(item) + ch < 35])}(dir)", sep="")
            
        else:
            display.insert("end", f"{''.join([' ' for ch in range(35) if len(item) + ch < 35])}(file)", sep="")