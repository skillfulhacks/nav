import yaml
import os
from XV_File_Manager import MainFunc

BACE_PATH = os.getcwd()
if os.name == "nt":
    PLATFORM = "Windows"
    SLASH = "\\"
else:
    PLATFORM = "Posix"
    SLASH = "/"
CFG_PATH= f"{BACE_PATH}{SLASH}.config{SLASH}xvrc.yaml"
os.chdir(f"{BACE_PATH}{SLASH}.config")
with open("xvrc.yaml") as file:
    CFG_FILE = yaml.load(file, Loader=yaml.FullLoader)
    
if CFG_FILE["internal"]["cfg_file_built"] == 0:
    os.chdir(BACE_PATH)
    from set_yaml import UpdateYaml
    os.chdir(f"{BACE_PATH}{SLASH}.config")
    UpdateYaml("xvrc.yaml")
    
    
MainFunc(CFG_FILE)