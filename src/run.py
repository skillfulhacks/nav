#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:51:35 2021

@author: clarence
"""
import yaml
import <<<ADD YOU MODULE HERE>>>


CONFIGPATH = "xvrc.yaml"

with open("xvrc.yaml") as file:
    CFGFILE = yaml.load(file, Loader=yaml.FullLoader)
    
if CFGFILE["internal"]["cfg_file_built"] == 0:
    from set_yaml import UpdateYaml
    UpdateYaml("xvrc.yaml")
    
    
<<<YOU MODULE>>>(CFGFILE)
