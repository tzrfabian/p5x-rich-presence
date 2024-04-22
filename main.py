from pypresence import Presence
import time

client_id = "1231839039254953994"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state = "I'm Thou, Thou Art I",
    large_image='p5x-icon',
    start= int(time.time()),
    buttons=[{"label": "Download Link!", "url":"https://p5x.perfectworld.com/kr/index.html"}]
)

while True:
    time.sleep(60)


## This code if you want to use "discordrp" library ##
# with Presence(client_id) as RPC:
#     print("Connected")
#     RPC.set(
#         {
#             "state": "In Game",
#             # "icon": "p5x-icon",
#             "details": "Currently in Mementos",
#             "timestamps": {"start": int(time.time())}
#         }
#     )
#     print("Presence updated")
#     while True:
#         time.sleep(60)    