# Super Cool Nice Antivirus 2025
# Copyright (c) 2025 - Backdoor Interactive!
# SCNAVs Settings Control Panel

import os, time, ctypes
debug = 0


def fileoperation(mode,filename,buffer=None,line=0):
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
    if mode == 5:
        with open(filename, 'w') as file:
            file.writelines(buffer)
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

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def lowramoff():
    try:
        replace_line("scansettings.txt",0,"LOWRAM:0\n")
        print("Settings Updated")
    except:
        print("Error!")

def lowramon():
    try:
        replace_line("scansettings.txt",0,"LOWRAM:1\n")
        print("Settings Updated")
    except:
        print("Error!")


def scanner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("SCAN.exe Settings")
    print("")
    print("What would you like to change?")
    print("Enter a number and press enter")
    print("")
    print('1: Enable Low RAM mode')
    print("2: Disable Low RAM mode")
    print("3: Enable scan.exe Debug Mode")
    print("4: ")
    print("5: ")   

def realtimeprotection():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Real Time Protection | Scan.exe Settings")
    print("")
    print("What would you like to change?")
    print("Enter a number and press enter")
    print("")
    print('1: Enable Real time Protection')
    print("2: Add Extra Custom directories to use with Real Time Protection")
    print("3: Add Exclusions for Real Time Protection (Exclude default directories for RTP)")
    print("4: Change the activity of Real Time Protection (in seconds)")
    print("5: Disable Real Time Protection")
    print("6: Enable scan.exe Low RAM Mode")
    print("7: Disable scan.exe Low RAM Mode")
    print("8: Back to Main Menu")
    try:
        ans = int(input("> "))
        if ans == 1:
            os.system("start scnavrealtime.exe")
            time.sleep(3)
            print("Real Time Protection is now enabled!")
            print("The background proccess is: scnavrealtime.exe Check taskmanager if you want!")
            print("Would you like to auto start Real Time Protection when you log into Windows? (y/n)")
            ans = input("> ")
            if ans == "y":
                print("This feature will be available in a later update!")
                print("Done!")
                time.sleep(3)
                main()
            if ans == "n":
                print("Ok! Thats fine. Just be aware that you have to enable Real Time Protection again everytime you logout from your computer!")
                print("If you want to use it")
                time.sleep(3)
                main()
        elif ans == 2:
            directoriestoadd = []
            while True:
                print('Type "done" to finish adding directories')

                ans = input("Enter a directory to include with Real Time Protection > ")
                if ans == "done":
                    print("ae")
                    print(str(directoriestoadd))
                    lines = "".join(directoriestoadd)
                    print(lines)
                    replace_line("scansettings.txt",3,f"{lines}endscandirs\n")
                    print("Settings Updated!")
                    time.sleep(3)
                    raise Exception
                directoriestoadd.append(f"{ans}\n")
                

        elif ans == 3:
            directoriestoadd = []
            while True:
                print('Type "done" to finish adding directories')

                ans = input("Enter a directory to exclude with Real Time Protection > ")
                if ans == "done":
                    print("Saving settings...")
                    print(str(directoriestoadd))
                    lines = "".join(directoriestoadd)
                    print(lines)
                    print("Finding endscandirs...")
                    linesofsettings = fileoperation(4,"scansettings.txt")
                    print(linesofsettings)
                    replace_line("scansettings.txt",linesofsettings-1,f"endscandirs\nEXCLUDE\n{lines}endexclude\n")
                    print("Settings Updated!")
                    time.sleep(10)
                    raise Exception
                directoriestoadd.append(f"{ans}\n")
        elif ans == 4:
            print("Time: Real time protection uses time to determine how 'active' it can be!")
            print("You dont really want to set this number too low! it will scan too much")
            print("The default Activity time is 60 seconds Per action")
            print("The lower the number, the more activity, the higher the number\nThe less activity, But You get more bandwidth to the OS")
            ans = int(input("Enter the time in seconds for: Real Time Protection Activity > "))
            replace_line("scansettings.txt",1,f"{ans}")
            print("Settings Updated!")
            time.sleep(3)
            raise Exception

        elif ans == 5:
            print("Disabling Real Time Protection...")
            os.system("taskkill /f /im scnavrealtime.exe")
            print("Real Time Protection Disabled")
            time.sleep(3)
            raise Exception
        elif ans == 6:
            print("Enabling Low RAM Mode...")
            print("SCNAV can now be used with 1gb of ram!")
            print("WARNING: Very harddrive intensive")
            lowramon()
            time.sleep(3)
            raise Exception
        elif ans == 7:
            print("Disabling Low RAM Mode...")
            print("SCNAV Will scan at its fastest")
            lowramoff()
            time.sleep(3)
            raise Exception
        elif ans == 8:
            print('"ae" -- Phoenix')
            time.sleep(1)
            main()
    except:
        realtimeprotection()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Super Cool Nice Antivirus 2025 -- Settings")
    print("Copyright (c) 2025 - Backdoor Interactive!")
    print("Version 1.0")
    print("")
    print("For help: Check out the SCNAV Userguide at: http://server1.phoenixproliant.42web.io:4556/SCNAV/help.html")
    print("What would you like to change?")
    print("Enter a number and press enter")
    print("")
    print("1: Real Time Protection | Scan.exe Settings")
    print("2: General SCNAV Settings")
    print("3: Advanced Settings")
    print("4: Open the settings.txt config file to view current settings")
    try:
        ans = int(input("> "))
        if ans == 1:
            realtimeprotection()
        elif ans == 2:
            raise Exception
        elif ans == 3:
            raise Exception
        elif ans == 4:
            os.system("start notepad.exe scansettings.txt")
            raise Exception
    except:
        # lol
        print("ae Error!")
        time.sleep(3)
        main()
main()