@echo off
rem Super Cool Nice Antivirus 2025 v1.07
rem scan.exe arguments:

set arg1=%1
set arg2=%2

start py32\pythonw.exe scan.pyc "%arg1%" %arg2%