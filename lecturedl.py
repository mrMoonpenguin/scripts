import requests, time, youtube_dl, sys

## Short python script to download ku leuven lecture streams
## example use: 'python lecturedl.py [pin]'

try:
    pin = sys.argv[1]
except IndexError:
    print("Please enter a valid pin.")
    quit()
link = "https://icts-p-toledo-streaming-video-live-backend.cloud.icts.kuleuven.be/api/viewers/" + pin

raw = requests.get(link)
data = raw.json()

while "status" in data and data["status"] == "NOT_FOUND":
    time.sleep(30)

    raw = requests.get(link)
    data = raw.json()

    print("Retrying.")

print("Found stream.")

streamlink = data["streamUrl"]

opts = {}

print("Starting download.")
with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download([streamlink])

print("Download finished.")
