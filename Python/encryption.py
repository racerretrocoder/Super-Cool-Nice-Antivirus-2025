# pip install pycrypto
# Compatible with Python 3.2

# Note this is just a general code basis! Must be changed to be implemented successfully
import sys
from Crypto.Cipher import AES

def tempwrite(data): # This is my idea to hopefully prevent overflowing.
    print("Tempwrite: ",data)
    with open("enc.tmp","ab+") as tempfile:
        tempfile.write(data)
        print("Temp Written out")
        tempfile.close()
def tempread():
    print("Tempread()")
    with open("enc.tmp","rb") as tempfile:
        ae = tempfile.read()
        return ae
def tempreset():
    os.system("del enc.tmp")
    print("tempfile reset!")


filepatharg = sys.argv[1:]
# as shown in sample code
encsys = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
#ciphertext = obj.encrypt(message)
with open(filepatharg,"rb") as filetoenc
    while True:
        data = filetoenc.read(8192) # 8kb
        if not data:
            break
        encdata = encsys.encrypt(data)
        tempwrite(encdata)
    print("Encryption complete")
# now write out to the actual file.
