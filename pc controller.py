import os
input=input(str("What would you like to open:"))
if "sublime" in input:
    sublime_dir="C:\Program Files\Sublime Text 3\sublime_text.exe"
    os.startfile(os.path.join(sublime_dir))
if "zoom" in input:
    zoom_dir="C:\\Users\\KHALID\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    os.startfile(os.path.join(zoom_dir))
if "shareit" in input:
    shareit_dir="C:\\Program Files\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
    os.startfile(os.path.join(shareit_dir))
if "notepad++" in input:
    notepad_dir="C:\\Program Files\\Notepad++\\notepad++.exe"
    os.startfile(os.path.join(notepad_dir))
if "cmd" in input:
    cmd_dir="C:\\Windows\\System32\\cmd.exe"
    os.startfile(os.path.join(cmd_dir))
if "vs code" in input:
    vscode_dir="C:\\Users\\KHALID\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(os.joinpath(vscode_dir))