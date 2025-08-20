# Windows 8.0 and up
from pypresence import Presence
import time

client_id = "1399410639134523405"
RPC = Presence(client_id)
RPC.connect()

RPC.update(
    state="SCNAV test"
)

while True:
    time.sleep(60)