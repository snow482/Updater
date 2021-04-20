import os
import glob
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

#versionCheck()

# поиск файлов с расширением .exe, добавление в массив и поиск в массеве конкретного
def findFiles():
    name = "DiscordSetup.exe"
    neededFile = []
    os.chdir(r'c:\users\snow-pc\downloads')
    for file in glob.glob("*.exe"):
        neededFile.append(file)
    if name in neededFile:
        print("yes")

#findFiles()

def fileRun(fileType):
    #cmd = "DiscordSetup.exe"
    os.chdir(r'c:\users\snow-pc\downloads')
    os.system(fileType)

fileRun('200115300109_488395.jpg')

# GET/POST запросы
def myjson(): 
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

#myjson_1()



# убитие процессов
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "explorer.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

#processKilling()

def build_libs(Nthreads,LibCfg):  # Nthreads is int,LibCfg as string
      

if __name__=='__main__':
    numthreads = sys.argv[1] # first argument to script - 4
    libconfig = sys.argv[2] # second argument
    # call build_libs however you planned
    build_libs(numthreads, libconfig)