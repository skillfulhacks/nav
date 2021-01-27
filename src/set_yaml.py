#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UpdateYaml:
    def __init__(self, file):
        import yaml
        import os
        
        
        ### Set Programs Root Dir Defaults to cwd ###
        root_dir = input(f"Root Dir ({os.getcwd()}): ")
        root_dir = root_dir if root_dir != "" else f"{os.getcwd()}"
        print(f"Root Dir Set To: {root_dir}" if root_dir != "" else f"Root Dir Set To: {os.getcwd()}")
    
        ### Load and Yaml file and Merges it With the Defualt File
        print("!!! Advanced Leave Blank if Unsure !!!")
        spec_file = input("Spec File (None): ")
        if spec_file != "":
    
            with open(spec_file) as file:
                spec_file = yaml.load(file, Loader=yaml.FullLoader)
    
            if spec_file == None:
                spec_file = {}
        else:
            spec_file = {}
    
        print(f"Spec File Set To: {spec_file}")
    
    
        ### Config File ###
        raw_cfg = {**{
            'gen_config':
                {
                'rootdir': root_dir,
                'os': os.name
                },
                
            'internal':
                {
                'cfg_file_built': 1
                },
                
            'commands':
                {
                'paths': 
                    [
                    f"{root_dir}/.commands"
                    ],
                'files':
                    [
                    ],
                },
            }, **spec_file}    
            
    
    
        with open(root_dir + "/xvrc.yaml", 'w') as file:
            dump = yaml.dump(raw_cfg, file)
            
        print("made config file")