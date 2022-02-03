import requests
import time
while True:
    for x in range(0,100):
        requests.get("http://168.63.19.214:6018/errors/error_URI")
    time.sleep(900)
