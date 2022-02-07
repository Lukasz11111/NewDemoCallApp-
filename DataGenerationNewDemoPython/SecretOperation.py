from time import sleep
import yaml
import random
import revdebug
@revdebug.norecord
def yanlOpen():
    with open("option.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

@revdebug.norecord
def randomTime(scanAmount,increasedTraffic,minimalArea):
    yaml_=yanlOpen()
    
    result=random.randint(int(minimalArea),int(scanAmount))
    result=result+int(increasedTraffic)
    
    return int(result)
@revdebug.norecord
def saveData(scanAmount=100,increasedTraffic=0, minimalArea=0):
    # ms
    try:
        sleep(randomTime(scanAmount,increasedTraffic,minimalArea)/1000)
    except:
        pass
