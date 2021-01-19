# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import sys

# Set up PLATFORM.ini
with open("PLATFORM.ini","w+") as file:
    if os.name == "nt":
        file.write("Win")
    else:
        file.write("Posix")
    file.close()
 
# Set up SETDIR.ini       
with open("SETDIR.ini","w+") as file:
    os.chdir("..")
    file.write(os.getcwd())
    file.close()
