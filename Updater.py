import os
import shutil
import psutil
import json
import zipfile
import requests
import hmac
import hashlib 

# уточнение текущей дирректории
print(os.getcwd())

# чек версии программы
def versionCheck():
    fileForHash = hashlib.md5()
    with open('TrajectoryConverter.exe', 'rb') as fileType: 
        buf = fileType.read()
        fileForHash.update(buf)
        checkSum = str(fileForHash.hexdigest())
    print(checkSum)

versionCheck()

# GET/POST запросы
'''def myjson(): 
    responce = requests.get('https://httpbin.org/get', params={'a':'b'})

    if responce.status_code == 200: 
        print('all ok')

    print(responce.text)

#myjson()

def myjson_1():
    r = requests.post('https://httpbin.org/post', params={'key':'value'}, json={'username':'melou'})
    with open('log.json', 'w') as log:
        log.write(r.text)
    print(r.text)

myjson_1()'''



# убитие процессов
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "explorer.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")
