import ctypes, sys, os, time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        print("Error on determining admin permissions!")
        return False
try:
    print("Init")
except:
    print("Could not load some file(s)! Please check to make sure that SCNAV is installed and not damaged")


if is_admin():
    with open("threatsexe.txt", 'r') as threatsexe:
        for line in threatsexe:
            print(f'Killing {line}')
            os.system(f'taskkill /f /im {line}')

    with open("threats.txt", 'r') as threats:
        for line in threats:
            print(f'Deleting {line}')
            print(line)
            try:
                os.remove(f'{line}')
                print(f"Threat {line} has been deleted successfully in attempt 1")
            except:

                try:
                    print(f"Attempt 2 of deleteing: {line}")
                    print(line[1])
                    if line[1] == ":":
                        # Not a blank space. delete it
                        os.system(f'del /f /q "{line}"')
                        print(f"Threat {line} has been deleted successfully in attempt 2!")
                except:
                    print("Attempts failed too delete the threat!")
                    print(f"Find {line} and delete it manually!")
                    time.sleep(1)
    print("Threat Removeal: Complete")
    print("Removing quarentine")
    os.remove("threatsexe.txt")
    os.remove("threats.txt")

    

else:
    # Didnt run as admin, Ask for admin and rerun
    print("Requesting administrator to remove threats")
    time.sleep(3)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)