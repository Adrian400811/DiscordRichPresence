from pypresence import Presence
import time
import json

with open('../DiscordRichPresence/Settings.json', mode='r', encoding='utf8') as sfile:
    sdata = json.load(sfile)

state = sdata["STATE"]
detail = sdata["DETAIL"]
client_id = sdata["CLIENT"]  # Put your real client ID in Settings.json
small_image = sdata["SMALL_IMAGE"]
large_image = sdata["LARGE_IMAGE"]
large_text = sdata["LARGE_TEXT"]
small_text = sdata["SMALL_TEXT"]

RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop


# Set the presence
RPC.update(state=f"{state}", details=f"{detail}",
           large_image=f"{large_image}",
           large_text=f"{large_text}",
           small_image=f"{small_image}",
           small_text=f"{small_text}")

print(RPC.update(state=f"{state}", details=f"{detail}"))  

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
