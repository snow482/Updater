import os, sys
import glob
import shutil
import psutil
import json
import zipfile
import requests
import hmac
import hashlib 



# уточнение текущей дирректории
#print(os.getcwd())

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

# запуск программы
def fileRun():
    os.chdir(r'C:\git\proxygnss\cmake-build-debug\App')
    path = 'start' + ' ' + 'App.exe' + ' ' + 'span6' + ' ' + '20000'
    os.system(path)

    #cmd = "DiscordSetup.exe"
    #os.chdir(r'C:\git\Updater')
    #os.chdir(r'c:\users\snow-pc\downloads')
    #path = 'cmdWithArgs.py'
    #os.system('start')
    #os.system(path)

fileRun()

#fileRun()
#os.chdir(r'c:\git\proxygnss\cmake-build-debug\App')
#os.system('App.exe', 'span6', '20000')
#argum = 'App.exe' + ' ' + 'span6' + ' ' + '20000'
#os.system(argum)
#sys.exit()
# запуск программы с агрументами
#firstArgument = "Scada6.exe"
#secondArgument =  "anonimous.json"


'''def funcWithArgs(f1, f2, f3):
       
    if len(sys.argv) == 3:
        f1 = sys.argv[0]
        secondArgument = sys.argv[1]
        firdArgument = sys.argv[2]
        f1 = firstArgument
        f2 = secondArgument
        f3 = firdArgument
        argument = {firstArgument, secondArgument}
    return argument  '''   
      

#fileRun(funcWithArgs('App.exe', 'span6', '20000'))


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
        if processName.name() == "App.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

#processKilling()




