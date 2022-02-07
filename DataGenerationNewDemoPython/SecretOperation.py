from time import sleep
import random
import revdebug


@revdebug.norecord
def randomTime(scanAmount,increasedTraffic,minimalArea):
    result=random.randint(int(minimalArea),int(scanAmount))
    result=result+int(increasedTraffic)
    if 3==random.randint(0,10):
        result=result+750
    
    return int(result)
@revdebug.norecord
def saveData(self):
    # ms
    try:
        time=randomTime(self.get_query_argument("scan_amount"),self.get_query_argument("increased_traffic"),self.get_query_argument("minimal_area"))
        sleep(time/1000)
    except Exception as e:
        print(e, flush=True)
        pass

    if int(self.get_query_argument("CountActiveArea"))>1000:
        if 3==random.randint(0,5):
            a=[]
            a[1000]="err"



