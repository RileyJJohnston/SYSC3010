import requests
import json
from pprint import pprint

def readFromChannelFeed(channelID):
    readKey = "2D5PMX1Z2S8JKLQE"
    path = "https://api.thingspeak.com/channels/" + str(channelID) + "/feeds.json?api_key=" + readKey + "&results=2"
    return requests.get(path)

def readFromChannelField(channelID, channelFieldNumber):
    readKey = "2D5PMX1Z2S8JKLQE"
    path = "https://api.thingspeak.com/channels/" + str(channelID) + "/fields/" + str(channelFieldNumber) + ".json?api_key=" + readKey + "&results=2"
    return requests.get(path)

response = readFromChannelFeed(1156891)
#response = readFromChannelField(1156891, 1)
print(response)

json_val = json.loads(response.content)
pprint(json_val)
