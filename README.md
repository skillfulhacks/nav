XV File Manager
====
---
3.0.0a 01-31-2021   
-----------------  
@SkillfulHacks 
* Changes  
• Added XVScript; A Basic Way to Write Script Files  
• Added ENV Vars Use $VARNAME to Replace a Arg With the Selected var  
• Added Internal Vars Use #VARNAME to Replace a Arg With the Selected var  
• Added Command "cp"; Copies a File  
• Added Command "mv"; Cuts a File  
• Added Command "create_env_var"; Creates a ENV Var  
• Added Command "rm_env_var"; Removes a ENV Var  
• Added Command "echo"; Prints Lines to Console  
• Added Command "run_xvs"; Run a Script File  

* Updated Files:  
• XV_File_Manager.py (Req),  
• commands/run_command.py (Req),  

* New Files:  
• commands/cp.py (Opt),  
• commands/mv.py (Opt),  
• commands/create_env_var.py (Opt),  
• commands/remove_env_var.py (Opt),  
• commands/echo.py (Opt),  
• commands/run_xvs.py (Opt),  

---
2.01a 01-27-2021   
---  
@SkillfulHacks 
* Changes  
• Minor Changes/Bug Fixes in gui_tabs/file_system.py

* Updated Files:  
• gui_tabs/file_system.py (Opt)  

---
2.0.0a 01-27-2021   
---  
@SkillfulHacks 
* Changes  
• Renamed .commands to commands  
• Overhauled the Way Tabs Were Loaded  

* Updated Files:  
• XV_File_Manager.py (Req),  
• tk_custum_widgets.py (Req),  
• gui_tabs/command_ls.py (Req),  
• gui_tabs/term_emul.py (Req)  
• !!! ALL FILES IN commands !!! (Req)  

* New Files:  
• gui_tabs/file_system.py (Opt)  
• gui_tabs/cmdout_console.py (Req)  
• commands/cat.py (Opt),  

---
1.1.0a 01-26-2021   
---  
@SkillfulHacks 
* Changes  
• Added a Update Function to Tab Files, Allowing for Updates After Startup  
• Added Configs >> xvrc.yaml  
• Added the Command "pinternal"; Prints a Internal Var  
• Added the Command "lsinternal"; Lists All Internal Vars  
• Added the Command "cd"; Changes Dir  
• Update the Command "ls"  

* Updated Files:  
• XV_File_Manager.py (Req),  
• tk_custum_widgets.py (Req),  
• xvrc.yaml (Req),  
• .commands/ls.py (Opt),  
• gui_tabs/command_ls.py (Req),  
• gui_tabs/term_emul.py (Opt)  

* New Files:  
• .commands/pinternal.py (Opt),  
• .commands/lsinternal.py (Opt),  
• .commands/cd.py (Opt),  

---
1.0.1a 01-22-2021   
---  
@SkillfulHacks 
* Changes  
• Cleaned Up XV_File_Manager Code  
• Minor Changes to "man" and "ls"

* Updated Files:  
• XV_File_Manager.py (Req),  
• .commands/ls.py (Opt),  
• .commands/man.py (Opt),  

---
1.0.0a 01-22-2021   
---  
@SkillfulHacks 
* Changes  
• Tabs are Now in Seperate Files in the gui_tabs Folder.  
• Changed tk_custum_widgets Internally.  
• Added the Tab "command_ls"; Displays a list of all Non Internal Commands.  
• Added the Tab "term_emul"; Displays a CLI Interface For Running Commands.  
• Added the INTERNAL Attribute to Command Files.  
• Added the Command "help"; Runs the "man" Command on all Non-Internal Commands.  
• Added the Command "run_command"; A Internal Command Use to Run Other Command.  

* New Files:  
• .commands/help.py (Opt),  
• .commands/run_command.py (Req),  
• gui_tabs/command_ls.py (Opt),  
• gui_tabs/term_emul.py (Opt)  

* Updated Files:  
• XV_File_Manager.py (Req),  
• tk_custum_widgets.py (Req)  

---
0.2.3a 01-22-2021  
---  
@Pybit   
• Added the 'sysinfo' command.  
• Changed 'doc' to '\_\_doc\_\_' in command files.  
• Added the 'runfile' command.  

---
0.2.2a 01-21-2021   
---  
@Pybit   
• Stoped window resizability in the main file.   
• The ls command will now give more information when run.  

---
0.2.1a 01-20-2021  
---  
@Skillfulhacks  
• Updated Console Internally.  
• Fixed an Typo Making it so it Could Display Only 1 Command.  
• Added the Command "man"; Displays Help for a Selected Command.  

---
0.2.0a 01-20-2021  
---  
@Skillfulhacks  
• Added the Ability to Update Commands.  
• Added a Basic Tkinter Console With the Ablity to Insert Text.  
• Added the Command "ls"; Lists CWD.  

---
0.1.0a 01-20-2021  
---  
@Pybit  
• Added SETUP_CONSOLE. 


  

