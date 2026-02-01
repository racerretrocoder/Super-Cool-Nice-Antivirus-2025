import os, time, urllib.request

scnavupdate = 0
basesupdate = 0

print("Super Cool Nice Antivirus 2025")
print("Copyright (C) Backdoor Interactive! 2026")
print("SCNAV Updater Version 2.0")
server = "http://ilovetech0629.epizy.com/SCNAV/update.txt"
time.sleep(1)
print("Checking for Updates... ")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0',
}
    #r = requests.get("http://ilovetech0629.epizy.com/SCNAV/update.txt", headers=headers)
r = urllib.request.urlopen('http://ilovetech0629.epizy.com/SCNAV/update.txt')

# print("Failed to check for updates")
time.sleep(5)
#print(r.text)
updatebyt = r.read()
updatereq = updatebyt.decode("utf-8")

update = updatereq.split("\n")
updatepost = update[0]
prefirstline = updatepost.replace("\r","")
firstline = prefirstline.replace("\n","")

# SCNAV

scnavpost = update[1]
prescnavsvr = scnavpost.replace("\r","")
scnavsvr = prescnavsvr.replace("\n","")

# DATABASE

dbpost = update[2]
predbsvr = dbpost.replace("\r","")
dbsvr = predbsvr.replace("\n","")

# Check update syntax
# print(f"a{firstline}b")
if firstline == "SCNAVUPDATE":
    # Check our current version
    try:
        with open("ver.txt", 'r') as file:
            ver = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print("Could not detect SCNAV Version file: ver.txt\nYou may have to reinstall SCNAV Manually")
        data = set()
    print("Connected to SCNAV Update Server Successfully!\n")
    print("Your current version of SCNAV is: "+ver[0])
    print("Your current version of the MD5 Database (bases.txt) is: "+ver[1]+"\n")
    time.sleep(2)
    print("Most recent SCNAV Version (From updateserver): "+scnavsvr)
    print("Most recent Threat Database Version (From updateserver): "+dbsvr)
    print("\n")
    if ver[0] != scnavsvr:
        print("-----------------   New SCNAV Version Available!   -----------------")
        scnavupdate = 1
    if ver[1] != dbsvr:
        print("-----------------   New Threat Database Version Available!   -----------------")
        basesupdate = 1
    
    # User interaction
    if scnavupdate == 1:
        answer = input("Would you like to upgrade to a newer version of SCNAV?\n (y/n) > ")
        if answer == "y":
            print("Downloading Newer Version Please wait...")
            preup = update[3]
            preup1 = preup.replace("\r","")
            upgradeurl1 = preup1.replace("\n","")
            spreup = update[4]
            spreup1 = spreup.replace("\r","")
            upgradeurl2 = spreup1.replace("\n","")
            # attempt to download the upgrade
            print("Creating Temp Directory... (C:\SCNAVUPDATE)")
            os.system("mkdir C:\SCNAVUPDATE")
            try:
                os.system("taskkill /f /im SCNAV.exe")
                os.system("taskkill /f /im scnavrealtime.exe")
                print("Downloading SCNAV Updates... (Using UpdateServer1) To C:\\SCNAVUPDATE\\upgrade.exe")
                urllib.request.urlretrieve(upgradeurl1, "C:\\SCNAVUPDATE\\upgrade.exe") # Download upgrader
                print("Download complete! Upgrading SCNAV. Please dont close this window!")
                os.system("C:\\SCNAVUPDATE\\upgrade.exe")
                time.sleep(1)
            except:
                print("Update server 1 failed!")
                print("Attempting to download on backup server")
                print("Getting latest SCNAV from UpdateServer2 to C:\\SCNAVUPDATE\\upgrade.exe")
                try:
                    urllib.request.urlretrieve(upgradeurl2, "C:\\SCNAVUPDATE\\upgrade.exe") # Download upgrader
                    print("Download complete! Upgrading SCNAV")
                    os.system("C:\\SCNAVUPDATE\\upgrade.exe")
                    time.sleep(1)
                except:
                    print("Failed twice at trying to download the upgrade file!")
                    print("Deleted temporary directory: C:\\SCNAVUPDATE")

            print("")
            time.sleep(5)
            print("Finished.")
            os.system("del C:\\SCNAVUPDATE\\upgrade.exe")
            os.system("rmdir C:\\SCNAVUPDATE")
            print("Deleted temporary directory: C:\\SCNAVUPDATE")
            print("")
            time.sleep(3)
        if answer != "y":
            print("Ok SCNAV will not be upgraded")
    if scnavupdate == 0:
        print("Your current SCNAV Version is already up to date! Check back later :)")
        time.sleep(1)
    if basesupdate == 1:
        answer = input("Would you like to update SCNAV's Threat Database?\n (y/n) > ")
        if answer == "y":
            print("Updating Threat Database. Downloading Please wait...")
            print("This may take a while!")
            preup = update[5]
            preup1 = preup.replace("\r","")
            upgradeurl1 = preup1.replace("\n","")
            spreup = update[6]
            spreup1 = spreup.replace("\r","")
            upgradeurl2 = spreup1.replace("\n","")
            try:

                os.system("taskkill /f /im SCNAV.exe")
                os.system("taskkill /f /im scnavrealtime.exe")
                print("Downloading bases.txt to: C:\\Program Files\\SCNAV2025\\bases.txt")
                urllib.request.urlretrieve(upgradeurl1, "C:\\Program Files\\SCNAV2025\\bases.txt") # Download upgrader
                print("Download complete!")
                time.sleep(1)
            except:
                print("Update server 1 failed!")
                print("Attempting to download on backup server")
                print("Downloading bases.txt to: C:\\Program Files\\SCNAV2025\\bases.txt")
                try:
                    urllib.request.urlretrieve(upgradeurl2, "C:\\Program Files\\SCNAV2025\\bases.txt") # Download upgrader
                    print("Download complete! Upgrading SCNAV")
                    time.sleep(1)
                except:
                    print("Failed twice at trying to download the upgrade file!")        
        if answer != "y":
            print("Ok Threat database will not be updated")


else:
    print("SCNAVUPDATE not found")
print("Program finished. You may now close this window.")
print("Thank you for using Super Cool Nice Antivirus 2025")
time.sleep(5)