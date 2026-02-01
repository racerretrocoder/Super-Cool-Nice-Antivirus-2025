# SCNAV Custom Fileshredder
# Copyright (C) Backdoor Interactive! | 2026

import os, sys, time, random
print("Super Cool Nice Antivirus 2025")
print("Copyright (c) Backdoor Interactive! 2026")
print("SCNAV's File Shredder")
print("")
candelete = 1
# Random Byte generator
# Similar to secrets.token_bytes()
def garbagedata(number=None):
    if number == None:
        number = 1
    return bytearray(random.getrandbits(8) for _ in range(number))

def shredfile(path):
    global candelete
    print("Shredding: "+path)
    mega_size = os.path.getsize(path)
    with open(path,"wb+") as f:
        f.seek(mega_size-1)
        f.write(bytearray(1)) # Zero out all the data in the file
    #   ae = input("Press any key to continue")
        f.seek(0)
	#	print(b"\x00" + secrets.token_bytes(mega_size-1) + b"\x00")
        f.write(bytearray(b'SCNAV           FILE SHREDDER                   COPYRIGHT (C) BACKDOOR INTERACTIVE | 2026' + garbagedata(mega_size-1)))
    #	ae = input("Press any key to continue")
        f.close() # Give access back
    if candelete == 1:
        os.system('del /f /q "'+path+'"') # Delete the final file
    print(path + " Shredded!")

def shreddirectory(directory):
    print("Shredding directory: " + directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            shredfile(filepath)	
	
def ae():
    print("Shredder!!!")
    if 1 == 1:
      mode = int(sys.argv[1]) # int, 1 for individual file or 2 for folder (and included subdirectories)
      file = " ".join(sys.argv[2:])
      message = input("Would you like the files to be deleted after the shred? [y/n] (y)\n > ")
      if message == "n":
        candelete = 0;
        print("Wont delete files after shredding!")
        time.sleep(2)
        print("Begin!")
      
      if mode == 1:
          shredfile(file)
          print("Complete!")
          time.sleep(5)
          return 1
      if mode == 2:
          shreddirectory(file)
          print("Complete!")
          time.sleep(5)
      else:
          print("Arguments:  shred.exe int(mode) str(path)   <-- Put path in quotes if it contains a space!")
          print("Mode: 1 | Shred only 1 file")
          print("Mode: 2 | Shred a folder including all subfolders and files within it")
          time.sleep(5)
ae()