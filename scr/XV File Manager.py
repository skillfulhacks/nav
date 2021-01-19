# import Modules
import tkinter as tk
import os

"""
THIS CODE IS TEMPORARY AND MOSTLIKLY WILL BE CHANGED AT SOME POINT
"""

BACE_DIR = os.getcwd()

# Get SLASH and PLATFORM
if os.name == "nt":
    PLATFORM = "Windows"
    SLASH = "\\"
else:
    PLATFORM = "Posix"
    SLASH = "/"

# Get CWD
os.chdir(f"{os.getcwd()}{SLASH}.config")
try:
    with open("Setdir.ini","r") as file:
        CWD = file.read()
        file.close()
except FileNotFoundError:
    with open("Setdir.ini","w+") as file:
        CWD = BACE_DIR
        file.write(BACE_DIR)
        file.close()

# COMMANDS_DIR AND LIST_OF_COMMANDS
COMMANDS_DIR = f"{BACE_DIR}{SLASH}.commands"
os.chdir(COMMANDS_DIR)
LIST_OF_COMMANDS = os.listdir(COMMANDS_DIR)

# Create a tkinter screen named gui
gui = tk.Tk()
gui.geometry('500x400')
gui.title("XV File Manager")
gui.iconbitmap(f'{BACE_DIR}{SLASH}.images{SLASH}XVimg.ico')

# Create a Entrybox with CWD inserted
set_dir_label = tk.Label(gui,text="set directory: ",font="monospace 8").grid(row=0,column=0)
set_dir_entry = tk.Entry(gui,bd=1,font="monospace 8",width=12)
set_dir_entry.grid(row=0,column=1,sticky="nswe")
set_dir_entry.insert(0,CWD)

# Create list of commands
ROW_NUM = 2
COLUMN_NUM = 0
times_run = 0

for command in LIST_OF_COMMANDS:
    command_name = tk.Label(gui,text=command,font="monospace 10",fg="darkblue").grid(row=ROW_NUM,column=COLUMN_NUM,sticky="nswe")
    command_button = tk.Button(gui,text=f"Run {command}",font="monospace 9").grid(row=ROW_NUM,column=COLUMN_NUM+1+times_run,sticky="nswe")
    os.chdir(f"{COMMANDS_DIR}\{command}")
    with open("Description","r") as file:
        Description = file.read()
        file.close()
    command_description = tk.Label(gui,text=f"Description:\n{Description}",font="monospace 8",fg="gray").grid(row=ROW_NUM+1,column=COLUMN_NUM,sticky="nswe")
    COLUMN_NUM += 3
    times_run +=1

# gui mainloop
gui.mainloop()
