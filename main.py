from pypresence import Presence
import time
import json
import datetime

with open('../DiscordRichPresence-master/Settings.json', mode='r', encoding='utf8') as sfile:
    sdata = json.load(sfile)

state = sdata["STATE"]
detail = sdata["APP"]
large_text = sdata["LARGE_TEXT"]
small_text = sdata["SMALL_TEXT"]
ntime = datetime.datetime.now()
timestamp = ntime.strftime("%s")

rpc = Presence(751373482817749062)  # Initialize the client class
rpc.connect()  # Start the handshake loop

# Set the presence
rpc.update(state=f"{state}", details=f"{detail}",
           large_image="",
           large_text=f"{large_text}",
           small_image="",
           small_text=f"{small_text}",
           party_size=[int(sdata["SIZE"]), 30],
           start=timestamp)

print("Connected to Discord")

while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
