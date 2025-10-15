# Malware sandbox server implementation
import sys,os,time,requests,urllib,urllib3
from random import randint
filename = sys.argv[1] # path to upload to server
print("Super Cool Nice Antivirus 2025 Edition")
print("Copyright (c) 2025 Backdoor Interactive!\n")
print("sand.exe -- SCNAV Sandbox Client\n")

stage = 1

print("Enter the Servers URL or IP Address (and port if needed): ")
server = input("> ")

def statusOnFile(uid):
    global server
    global stage
    # Get status on the file from a 16 digit number
    print("Server check!")
    #print(f'{server}/index.php?getinfo=1&uid={str(uid)}')
    #r = requests.get(f'{server}/ae.php',timeout=3)
    #return r.text
    try:
        with urllib.request.urlopen(f'{server}/index.php?getinfo=1&stage={stage}&uid={str(uid)}') as response:
            html = response.read().decode('utf-8')
            rec = html.split("?")
            print(rec)
            print(html)
            if rec[0] == "Stage 1 Testing (VT)":
                print("First stage complete!")
                print(f"Malware Percent: {rec[1]}")
                print(f"Stealth / Clean Percent: {rec[3]}")
                print(f"Sus: {rec[2]}")
                stage = stage + 1
    #        print(html)  # Print the first 200 characters of the HTML
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    


print("Preparing to upload the file")
files = {'file': open(filename, 'rb')}
print(f"Uploading to server: {sys.argv[1]}")
# how we keep track of the file: generate a 16 digit unique id to refer to file on the server
s = ''
for i in range(16):
    s = s + str(randint(0,9))
uid = s
try:
    thestring = f"{server}/index.php?uid={uid}"
    requests.post(thestring, files=files, timeout=8) # send the file and the uid
except:
    print("File sent!")
time.sleep(2)
while True:
    chck = statusOnFile(uid)
    time.sleep(10)