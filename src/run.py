#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
from XV_File_Manager import MainFunc

### Load Config File ###
CONFIGPATH = ".config/xvrc.yaml"

with open(CONFIGPATH) as file:
    CFGFILE = yaml.load(file, Loader=yaml.FullLoader)

### If Program Has Never Been Run Before Update the onfig File ###
if CFGFILE["internal"]["cfg_file_built"] == 0:
    from setcfg import UpdateYaml
    UpdateYaml("xvrc.yaml")
    
    
MainFunc(CFGFILE)
