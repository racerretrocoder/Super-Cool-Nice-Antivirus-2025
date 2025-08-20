import hashlib
import os
import datetime
import sys
import time
import ctypes
threatcount = 0
activescan = 0
# SCNAV File Scanner
#  _________                           _______________   ________   .________
# /   _____/ ____   ____ _____ ___  __ \_____  \   _  \  \_____  \  |   ____/
# \_____  \_/ ___\ /    \\__  \\  \/ /  /  ____/  /_\  \  /  ____/  |____  \ 
# /        \  \___|   |  \/ __ \\   /  /       \  \_/   \/       \  /       \
#/_______  /\___  >___|  (____  /\_/   \_______ \_____  /\_______ \/______  /
#        \/     \/     \/     \/               \/     \/         \/       \/ 

# Made by the BACKDOOR INTERACTIVE TEAM!!
# Phoenix, Adko5558, Theprebeta, Hinata, Gamma_games, and a few more who inspired me with ideas thank you :D




print("")
print("Super Cool Nice Antivirus 2025 Edition")
print("Copyright (c) 2025 Backdoor Interactive!\n")
print("scan.exe | sscan.exe -- SCNAV File Scanner")


# better md5 scanner lol
# def md5Checksum(filePath):
#     with open(filePath, 'rb') as filetohash:
#         m = hashlib.md5()
#         while True:
#             data = filetohash.read(8192)
#             if not data:
#                 break
#             m.update(data)
#         return m.hexdigest()

#print('The MD5 checksum of text.txt is', md5Checksum('test.txt'))



try: 
    import vt
except:
    print("error could not import virus total")

# please dont abuse my api key for virus total :(
# d41d8cd98f00b204e9800998ecf8427e  zero byte test file
debug = 0
sound = 'C:\\Program Files\\SCNAV2025\\threat.mp3'
try:
    import simpleaudio as sa
    #threatsound = pyglet.media.load('threat.mp3')
    #wave_obj = sa.WaveObject.from_wave_file("threat.wav")
    #play_obj = wave_obj.play()
    #play_obj.wait_done()
    # 
except:
    print("Error on loading audio system")
    time.sleep(3)


def fileoperation(mode,filename,buffer="data",line=0):
    # Filename can be eaither local directory name or full featured file path
    if debug != 0:
        print("file operation in progress")
    if mode == 1:
        try:
        # Append Mode
            if debug != 0:
                print("APPEND MODE")
                print(f"APPEND: {filename} <-- {buffer}")
            with open(filename, 'a') as appended:
                appended.write(buffer)
                appended.close()
        except:
            print("unknown error")
    if mode == 2:
        # Read Mode
        if debug != 0:
            print("READ MODE")
            print(f"READ: {filename}")
        try:
            with open(filename, 'r') as file:
                return {line.strip() for line in file if line.strip()}
        except Exception as e:
            print(f"Error loading the file: {filename} {e} make sure everything is updated")
            return set()
    if mode == 3:
        # Hash Mode
        try:
            # Old way: Bugs with old way! If you scanned a file that bigger than ur ram. pc freeze xd
            # with open(filename, 'rb') as file:
            #     file_data = file.read()
            #     file_hash = hashlib.md5(file_data).hexdigest()
            #     return file_hash
            #     file.close()
            with open(filename, 'rb') as filetohash:
                m = hashlib.md5()
                while True:
                    data = filetohash.read(8192) # 8kb
                    if not data:
                        break
                    m.update(data)
                return m.hexdigest()
        except:
            return "none"
    if mode == 4:
        # List Read Mode
        if debug != 0:
            print("READ MODE")
            print(f"READ: {filename}")
        try:
            with open(filename, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error loading the file: {filename} {e} make sure everything is updated")
            return set()

def isadmin():
    return True


def scan():
    print('argument list', sys.argv)
    try:
        scanpath = sys.argv[1]

    except:
        print("Super Cool Nice Antivirus - SCAN.exe TO USE:")
        print('scan.exe "C:\\The\\Directory\\To\\Scan" -- Scan a directory for threats! Then log them to the quarentine')
        sys.exit()
    if scanpath == "C:\\Program":
        scanpath = sys.argv[3]
    # try:
    #     os.remove("threatsexe.txt")
    #     os.remove("threats.txt")
    # except:
    #     print("Threat history files are not found. No need to reset them")
    
    try: 
        if sys.argv[2] == "activescan":
            print("launched from realtime protectionscanner")
            global activescan
            activescan = 1
    except:
        print("SCAN Mode: Regular")
    # determine scan settings
    lowrammode = 0

    try:
        settings = fileoperation(4,"scansettings.txt",)
        print(settings[0])
        if settings[0] == "LOWRAM:0" or settings[0] == "LOWRAM:0\n":
            lowrammode = 0
        else:
            lowrammode = 1
    except:
        print("Could not load scansettings.txt - Using default settings, Low ram mode (Slow scaninng)")
        lowrammode = 1
    if scanpath == "web": # VT Mode
        client = vt.Client("ae")
        filepathvt = sys.argv[2]
        if isadmin():
            
            filehashvt = fileoperation(3,filepathvt)
            #file = client.get_object(filehashvt) # Upload to vt
            #size = file.size
            with open(filepathvt, "rb") as file:
                print("Uploading file to VirusTotal please wait...")
                analysis = client.scan_file(file,)
            while True:
                analysis = client.get_object("/analyses/{}", analysis.id)
                try:
                    file = client.get_object(filehashvt) # Upload to vt
                    size = file.size
                    print("Got it!!")
                except:
                    print("File proccessing please wait")
                print(analysis.status)
                if analysis.status == "completed":
                    file = client.get_object(f"/files/{filehashvt}") # Upload to vt
                    size = file.size
                    #print(file.last_analysis_stats)
                    print("File upload complete! Heres the info!")
                    print(f"File: {filepathvt}")
                    print(f"File Size: {size}")
                    print(f"File hash (MD5): {filehashvt}")

                    print("")
                    print("Virstotal Detections:")
                    max = int(file.last_analysis_stats['malicious']) + int(file.last_analysis_stats['suspicious']) + int(file.last_analysis_stats['undetected'])
                    print(f"Malicious: {file.last_analysis_stats['malicious']} / {max}")
                    print(f"Suspicious: {file.last_analysis_stats['suspicious']} / {max}")
                    print(f"Undetected:  {file.last_analysis_stats['undetected']} / {max}")
                    print("")
                    print("Done!")
                    print("Delaying for 20 seconds...")
                    client.close()
                    time.sleep(20)
                    exit()
                    break
                time.sleep(30)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    
    # scan history
    if isadmin():
    
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history = f"[{timestamp}] Scanned in {scanpath}\n"
        fileoperation(1,"scanhistory.txt",history)
        
        basesoutdated = 0
        if basesoutdated == 1:
            print("Bases are outdated!")
            time.sleep(2)
    
        
        print("Scanning! please wait. All detected threats will show below")
        print("This does not remove the threats!")
        print("Check the results of the scan when it is finsished")
        
        def load_malware_hashes(filename):
            """Loads malware hashes from a text file"""
            return fileoperation(2,filename) # should return right? or do i just call it
    
        def scan_file(filepath, malware_hashes, filename, lowrammode):
            """Scans a file and checks if its hash is in the malware list"""
            try:
                print(f"Scanning {filename}")
                fileoperation(1,"scanneddirs.txt",filepath)   
                file_hash = fileoperation(3,filepath)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                global threatsound
                global threatcount
                if lowrammode == 1: # Use low ram when loading the database
                    with open(malware_hashes) as mdb:
                        for line in mdb:
                            if file_hash in line:
                                print("threat detected!")
                #if file_hash in malware_hashes:
                                if debug != 0:
                                    fileoperation(1,"debug.txt",f"[{timestamp}] Threat detected: {filename} Location: {filepath} (Hash: {file_hash})")
                                print(f"[{timestamp}] Threat detected: {filename} Location: {filepath} (Hash: {file_hash})")
                                
                                threatcount = threatcount + 1
                                
                                try:
                                    if sys.argv[2] == "activescan":
                                        print("SCAN in stealth mode")
                                    else:
                                        #threatsound.play()
                                        wave_obj = sa.WaveObject.from_wave_file("threat.wav")
                                        play_obj = wave_obj.play()
                                        play_obj.wait_done()
                                except:
                                    try:
                                        wave_obj = sa.WaveObject.from_wave_file("threat.wav")
                                        play_obj = wave_obj.play()
                                        play_obj.wait_done()
                                    except:
                                        print("Error on playing error sound file")

                                time.sleep(1) # delay 1 second!
                                fileoperation(1,"threats.txt",filepath + "\n") # Store threat location in quarentine!
                                fileoperation(1,"threatsexe.txt",filename + "\n") # Store threat location in quarentine!
                            else: 
                                clean = 1
                elif lowrammode == 0: # Fast scanning

                            if file_hash in malware_hashes:
                                if debug != 0:
                                    fileoperation(1,"debug.txt",f"[{timestamp}] Threat detected: {filename} Location: {filepath} (Hash: {file_hash})")
                                print(f"[{timestamp}] Threat detected: {filename} Location: {filepath} (Hash: {file_hash})")
                                threatcount = threatcount + 1
                                try:
                                    if sys.argv[2] == "activescan":
                                        print("SCAN in stealth mode")
                                    else:
                                        wave_obj = sa.WaveObject.from_wave_file("threat.wav")
                                        play_obj = wave_obj.play()
                                        play_obj.wait_done()
                                except:
                                    try:
                                        wave_obj = sa.WaveObject.from_wave_file("threat.wav")
                                        play_obj = wave_obj.play()
                                        play_obj.wait_done()
                                    except:
                                        print("Error on playing threat.wav sound file")

                                time.sleep(1) # delay 1 second!
                                fileoperation(1,"threats.txt",filepath + "\n") # Store threat location in quarentine!
                                fileoperation(1,"threatsexe.txt",filename + "\n") # Store threat location in quarentine!
                            else: 
                                clean = 1
            except Exception as e:
                print(f"Error scanning: {e} at: {filepath}")
        
        def scan_directory(directory, malware_hashes, lowrammode):

            """Scans all files in a directory"""
            for root, dirs, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    scan_file(filepath, malware_hashes, file, lowrammode)
        
        hash_file = "bases.txt" 
        # OK FIRST Determine if we are in low ram mode
        if lowrammode == 0:
            # low ram disabled! lets use 4gb to store the database
            print("Low RAM Moded is disabled! Allocating 4GB's of RAM to load the threat database for the fastest Scanning")
            malware_hashes = load_malware_hashes(hash_file)
        else:
            print("Low RAM Mode: Enabled - Scans may be slow! But little to no RAM will be used")
            malware_hashes = hash_file # just give the filename instead
        directory_to_scan = scanpath
        scan_directory(directory_to_scan, malware_hashes, lowrammode)
        try:
            if sys.argv[2] == "activescan":
                print("launched from realtime protectionscanner")
                global threatcount
                print("making message box")
                title = 'Super Cool Nice Antivirus 2025'
                if threatcount == 0 or threatcount < 0:
                    print("lol")
                    sys.exit()
                    return 0

                text =f'WARNING! SCNAV Real Time Protection has detected {threatcount} threats! Location: {directory_to_scan}'
                style = 16
                ctypes.windll.user32.MessageBoxW(0, text, title, style)
                return 0
                time.sleep(5)
        except:
            print("Not showing MSG Box")

        print("Scan finished")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
scan()
