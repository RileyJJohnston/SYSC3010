import requests
import json

def writeToChannel():
    writeKey = "54CDA6FJF4RCJ92C"
    header = "&field1={}&field2={}&field3={}".format("RileyJohnston@cmail.carleton.ca","L2-M-12","a")
    path = "https://api.thingspeak.com/update?api_key=" + writeKey + header
    return requests.post(path)

response = writeToChannel()
