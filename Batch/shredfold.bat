@echo off
rem Super Cool Nice Antivirus 2025 v1.07
rem scan.exe arguments:
rem mode (must be 1)
rem arg2 = file path
set arg1=%*

py32\python.exe shred.pyc 2 %arg1%