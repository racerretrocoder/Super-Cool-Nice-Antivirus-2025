import ctypes, sys, os, time

def is_admin():
    try:
        #return ctypes.windll.shell32.IsUserAnAdmin()
        return True
    except:
        print("Error on determining admin permissions!")
        return False
try:
    print("Super Cool Nice Antivirus 2025")
    print("Copyright (c) Backdoor Interactive! 2026")
    print("remove.exe -- SCNAV's Virus Remover")
    print("This program will automatically remove any files listed in threats.txt")
except:
    print("Could not load some file(s)! Please check to make sure that SCNAV is installed and not damaged")


if is_admin():
    with open("threatsexe.txt", 'r') as threatsexe:
        for line in threatsexe:
            os.system('taskkill /f /im ' + line) # NT 6 and up
            exe1 = line.replace("\r","")
            exe2 = exe1.replace("\n","")
            exe3 = exe2.replace(".exe","")
            os.system('tskill ' + exe3 + ' /A')

    with open("threats.txt", 'r') as threats:
        for line in threats:
            try:
                os.remove(line)
                print("Threat has been deleted successfully in attempt 1")
            except:

                try:
                    print("Attempting to delete: " + line)
                    #print(line)
                    if line == ":" or line == "*.*" or line == " " or line == "":   
                        # Not a blank space. delete it
                        #os.system('del /f /q ' + line)
                        print("Unable to delete: " + line)
                    else:
                        data1 = line.replace("\r","")
                        data2 = data1.replace("\n","")
                        #print("1"+data2+"2")
                        os.system('del /f /q ' + '"' + data2 + '"')
                        print("\nSuccessfully deleted " + data2 + "\n")
                except:
                    print("Attempts failed too delete the threat!")
                    print("Find " + line +" and delete it manually!")
                    time.sleep(2)
    print("Threat Removeal: Complete")
    print("Reseting quarentine")
    os.remove("threatsexe.txt")
    os.remove("threats.txt")

    

else:
    # Didnt run as admin, Ask for admin and rerun
    print("Requesting administrator to remove threats")
    time.sleep(3)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)