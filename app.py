from random import randint, choice
import requests
import time

import json

def getData():
    f = open('endpoints.json')
    data = json.load(f)
    f.close()
    return data

def randomCall():
    data=getData()
    return randint(1,data["callCount"])

def randomSleepTime():
    data=getData()
    return randint(data["minTimeSleep"],data["maxTimeSleep"])

def main():
    while True:
        data=getData()
        for x in range(0,randomCall()):
            endpoint=choice(data["endpoints"])
            requests.get(endpoint, verify=False, timeout=30)
            print(endpoint)
        sleepTime=randomSleepTime()
        print(f"Wait {sleepTime} s")
        time.sleep(sleepTime)

main()