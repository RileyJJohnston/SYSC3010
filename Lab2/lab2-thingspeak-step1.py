import requests
import json

def writeToChannel(value):
    writeKey = "QMWMKPPPKVF2CO9B"
    header = "&field1={}".format(value)
    path = "https://api.thingspeak.com/update?api_key=" + writeKey + header
    return requests.post(path)

number = input("input number to write to ThingSpeak channel:  ")
response = writeToChannel(number)

