from random import randint, choice
import asyncio
import requests
import aiohttp
import time
from datetime import datetime
import json
import threading

def getData():
    f = open('endpoints.json')
    data = json.load(f)
    f.close()
    return data

def request_task(url, headers):
    try:
        session = requests.Session()
        session.trust_env = False
        requests.get(url, verify=False, timeout=60)
    except Exception as e:
        print(e)

def fire_and_forget(url, headers=None):
    threading.Thread(target=request_task, args=(url, headers)).start()

def randomCall(type_):
    data=getData()
    return randint(1,data[type_])

def randomSleepTime():
    data=getData()
    return randint(data["minTimeSleep"],data["maxTimeSleep"])

async def req(data, traffic,type_, callType):
    try:
        timeout = aiohttp.ClientTimeout(total=60)
        calls=int(randomCall(callType)+int(randomCall(callType)*traffic))
        for x in range(0,calls):
            endpoint=choice(data[type_])
            request_task(endpoint, headers=None)
            # print(f"Type {type_}  endpoint {endpoint}", flush=True)
        print(f"Calls {calls}  type {type_}", flush=True)
    except Exception as e: 
        print(f"Err {e}", flush=True)

async def reqConst(data):
    try:
        for x in data["Const"]:
            if "id" in x:
                endpoint=str(x["url"]).replace("$$id$$",choice(x["id"]))
            else:
                endpoint=str(x["url"])
            request_task(endpoint, headers=None)
    except Exception as e: 
        print(f"Err {e}", flush=True)


async def callfn(data):
    
    if datetime.now().hour in data["increasedTrafficHours"]:
        print(f"Traffic houer on", flush=True)
        await req(data, 1,"endpoints","callCount")
        await req(data, 1.5,"longEndpoints", "callCountLong")
        await reqConst(data)
    else:
        print(f"Normal houer on", flush=True)
        await req(data, 0,"endpoints","callCount")
        await req(data, 0,"longEndpoints","callCountLong")
        await reqConst(data)

async def main():
    lognStopIt=0
    while True:
        data=getData()
        await callfn(data)
        sleepTime=randomSleepTime()
        print(f"Wait {sleepTime} s", flush=True)
        if lognStopIt==10:
            sleepTime=sleepTime+90
            lognStopIt=0
        else:
            lognStopIt=lognStopIt+1
        time.sleep(sleepTime)

asyncio.run(main()) 