#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:51:35 2021

@author: clarence
"""
import yaml
from <<<ADD YOU MODULE HERE>>> import <<ADD YOUR FUNCTION HERE>>>

### Load Config File ###
CONFIGPATH = "xvrc.yaml"

with open("xvrc.yaml") as file:
    CFGFILE = yaml.load(file, Loader=yaml.FullLoader)

### If Program Has Never Been Run Before Update the onfig File ###
if CFGFILE["internal"]["cfg_file_built"] == 0:
    from set_yaml import UpdateYaml
    UpdateYaml("xvrc.yaml")
    
    
<<<YOUR FUNCTION>>>(CFGFILE)
