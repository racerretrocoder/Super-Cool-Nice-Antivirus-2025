# "Real time protection" For SCNAV
print("")
print("Super Cool Nice Antivirus 2025 Edition")
print("Copyright (c) 2025 Backdoor Interactive!\n")
print("scnavrealtime.exe -- Real Time Protection")
print("")
scantime = 100 # overwritten with settings file
checktime = 3
scanspeed = 0

import os, time, hashlib, sys, subprocess
import os.path
userpf = os.environ['USERPROFILE']

customdirs = []
exclusions = []
filesAndFolders1 = []
filesAndFolders2 = []
removeables = ["E:\\","F:\\","G:\\"]
commondirs = [f"{userpf}\\Downloads",f"{userpf}\\Appdata",f"{userpf}\\Documents",f"{userpf}\\Desktop",f"{userpf}\\Music"]
debug = 0
canscantimely = 0
ranOnce = 0
changer = 0

def resetcheckfiles():
    global filesAndFolders1
    global filesAndFolders2
    global ranOnce
    filesAndFolders2 = []
    filesAndFolders1 = []
    ranOnce = 0
    print("files and folders reset!")


def requestscan(directory):
    print(f"requestscan(): {directory}")
    print("Checking exclusions:")
    notexcluded = 1
    for i in range(len(exclusions)):
        print(f"Checking exclusions: {i}: {exclusions[i]}")
        print(directory)
        if f"{exclusions[i]}" in directory:
            print("its in there!")
            notexcluded = 0

        else:
            print("string not in there")

    if notexcluded == 1:  
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call(f"sscan.exe {directory} activescan", creationflags=CREATE_NO_WINDOW)
        print("scan finish, delaying")
        global scantime
        time.sleep(scantime)




def checkfiles():
    # Goals of this function:
    #  |--- Have the ability to rapidly detect changes in filecount in folders, whilist hopefully being easy on resources
    #  |--- If the file count has changed we will run a scan on that folder  
    #  |--- Speed Control
    scanreq1 = 0
    scanreq2 = 0
    global ranOnce
    times = len(commondirs)
    if ranOnce == 0:
        print("checkfiles(): First run")
    for i in range(len(commondirs)):
        print(f"len() of commondirs: {len(commondirs)}")
        print(f"in checkfiles(): i: {i}")
        print(f"counting files in {commondirs[i]}")
        lst = os.listdir(commondirs[i]) # your directory path
        number_files = len(lst)
        #print(f"Number of files in {commondirs[i]}: {number_files} using listdir()")
        for root, dirs, files in os.walk(commondirs[i]):
            #print(f"{len(root)}")
            #print(f"{len(dirs)}")
            #print(f"{len(files)}")
            num1 = len(root)
            num2 = len(dirs)
            num3 = len(files)
            nummain = num1 + num2 + num3
        print(f"\n{commondirs[i]} : {nummain}")
        global filesAndFolders1
        global filesAndFolders2
        cpt = sum([len(files) for root, dirs, files in os.walk(commondirs[i])])
        if ranOnce == 0:
            print(f"----- in append! i: {i} -----")
            filesAndFolders1.append(f'{commondirs[i]} : {nummain}')
            print(filesAndFolders1)
            
            print(f"Number of files in {commondirs[i]}: {cpt} using cpt\n")
            filesAndFolders2.append(f'{commondirs[i]} : {cpt}')
            print(filesAndFolders2)
        if ranOnce == 1:
            print("---------------------- checking for changes ----------------------")
            global scanspeed
            if scanspeed == 0:
                time.sleep(5)
            elif scanspeed == 1:
                time.sleep(3)
            elif scanspeed == 2:
                time.sleep(2)
            elif scanspeed == 3:
                time.sleep(1)
            elif scanspeed == 4:
                time.sleep(0.5)
            elif scanspeed == 5:
                fastest = 1 # Do somthing other than sleep
            print(f"Expecting: {commondirs[i]} : {nummain}")
            print(f"FilesAndF: {filesAndFolders1[i]}")
            folder1String = f"{commondirs[i]} : {nummain}"
            if folder1String != filesAndFolders1[i]:
                print(f"---------- A: Change detected at commondirs: {i} ----------")
                scanreq1 = 1
                time.sleep(5) # for debug
                print("updating list 1")
                filesAndFolders1[i] = folder1String
            print("---------------------- checking for changes (2) ----------------------")
            #time.sleep(1)
            print(f"2  -- Expecting: {commondirs[i]} : {cpt}")
            print(f"2  -- FilesAndF: {filesAndFolders2[i]}")
            folder2String = f"{commondirs[i]} : {cpt}"
            if folder2String != filesAndFolders2[i]:
                print(f"---------- B: Change detected at commondirs: {i} ----------")
                scanreq2 = 1
                time.sleep(5) # for debug 
                print("updating list 2")
                filesAndFolders2[i] = folder2String

            print("Scan requests:")
            print(scanreq1)
            print(scanreq2)
            if scanreq1 == 1 or scanreq2 == 1:
                print(f"Will run a scan at: {commondirs[i]}")
                # scan that dir:
                scanner = requestscan(commondirs[i])
            if scanreq1 == 1:
                scanreq1 = 0
            if scanreq2 == 1:
                scanreq2 = 0

    # End the commondirs[] loop
    if ranOnce == 0:
        print("first run complete!")
        ranOnce = 1
    checkfiles()

# old unused
def mainloop():
    print("active scan main loop")
    print("Begin cycle scanning!")
    global scantime
    time.sleep(scantime)
    print("RTP About to scan")
    print("checking if threat")
    print(os.path.isfile("threats.txt"))

    CREATE_NO_WINDOW = 0x08000000
    if os.path.isfile("threats.txt") == True: # threat o noee!!
        mainloop() # restart and wait till threats are all gone okie?
    subprocess.call(f"sscan.exe {commondirs[0]} activescan", creationflags=CREATE_NO_WINDOW)
    print("scan finish, delaying")
    time.sleep(scantime + 14)
    print("checking if threat")
    print(os.path.isfile("threats.txt"))

    if os.path.isfile("threats.txt") == True: # threat o noee!!
        mainloop() # restart and wait till threats are all gone okie?
    subprocess.call(f"sscan.exe {commondirs[1]} activescan", creationflags=CREATE_NO_WINDOW)
    print("scan finish, delaying")
    time.sleep(scantime + 14)
    print("checking if threat")
    print(os.path.isfile("threats.txt"))

    if os.path.isfile("threats.txt") == True: # threat o noee!!
        mainloop() # restart and wait till threats are all gone okie?
    subprocess.call(f"sscan.exe {commondirs[2]} activescan", creationflags=CREATE_NO_WINDOW)
    print("scan finish, delaying")
    time.sleep(scantime + 14)
    print("checking if threat")
    print(os.path.isfile("threats.txt"))
    if os.path.isfile("threats.txt") == True: # threat o noee!!
        mainloop() # restart and wait till threats are all gone okie?
    subprocess.call(f"sscan.exe {commondirs[3]} activescan", creationflags=CREATE_NO_WINDOW)
    mainloop()
    

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
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error loading the file: {filename} {e} make sure everything is updated")
            return set()
    if mode == 4:
        # Gimme lines Mode
            if debug != 0:
                print("Gimme lines MODE")
                print(f"Getting Lines: {filename}")
            try:
                num_lines = sum(1 for _ in open(filename))
                return num_lines
            except Exception as e:
                print(f"Error loading the file: {filename} {e} make sure everything is updated")
                return set()

try:
    # First load the RTP settings
    settings = fileoperation(2,"scansettings.txt",)
    scantime = int(settings[1])
    scanspeed = int(settings[2])
    # i starts at 3
    numlines = fileoperation(4,"scansettings.txt") # number of lines in the file - 3
    print(f"Number of lines!: {numlines}")
    for i in range(3,numlines,1):

        if settings[i] == "endscandirs\n" or settings[i] == "endscandirs":  # ae
            print("done!")
            print(settings[i])
            # now check for exclusions thislist.remove("banana")
            # if the next line down is "EXCLUDE"
            try:
                if settings[i + 1] == "EXCLUDE" or settings[i + 1] == "EXCLUDE\n":
                    end = 0
                    ae = 2
                    while end == 0:
                        print("in exclusion loop")
                        print(f"{settings[i + ae]}")
                        if settings[i + ae] == "endexclude" or settings[i + ae] == "endexclude\n":
                            print("Exclusions done")
                            end = 1
                        else:
                            print(f"line {i+ae} is an exclusion adding")
                            if settings[i + ae] == "EXCLUDE" or settings[i + ae] == "EXCLUDE\n":
                                print("ae double exclude")
                            else:
                                exclusions.append(f"{settings[i + ae]}")
                            print(exclusions)
                            ae = ae + 1
            except:
                print("ae error in exclusions")
            print("Exclusions finished")
            if exclusions != []:
                print("There are exclusions! removing from common dirs (if they exist)")
                for i in range(len(exclusions)):
                    try:
                        commondirs.remove(exclusions[i])
                    except:
                        print(exclusions[i])
                print("done~")
            else:
                print("There are no exclusions")

        else:
            print(settings[i]) # Custom RTP Directory found!
            if settings[i] == "EXCLUDE" or settings[i] == "EXCLUDE\n":
                print("Settings loading finished. Breaking")
                break
            commondirs.append(settings[i])
    print(f"Common dirs: {commondirs}")
    print(f"Exclusions: {exclusions}")
except:
    print("Real Time Protection: Error!")
checkfiles()