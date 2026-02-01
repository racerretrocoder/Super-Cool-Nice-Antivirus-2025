@echo off
rem Super Cool Nice Antivirus 2025 v1.07
rem scan.exe arguments:
rem mode (must be 1)
set arg1= %*
echo %arg1%

start py32\python.exe shred.pyc 1 %arg1%