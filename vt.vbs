web="web "
param=InputBox("Enter the path to the file you want to upload to VT with quotes","Directory")

Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run("""scan.exe """ & web & param)
Set objShell = Nothing