import os, sys
import glob
import shutil
import psutil
import json
import zipfile
import requests
import hmac
import hashlib 

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


# поиск файлов с расширением .exe, добавление в массив и поиск в массеве конкретного
def findFile():
    name = "App.exe"
    neededFile = []
    os.chdir(r'c:\users\snow-pc\downloads')
    for file in glob.glob("*.exe"):
        neededFile.append(file)
    if name in neededFile:
        print("yes")

#findFile()


# GET запрос по ссылке на скачку архива по URL
def saveFileFromServer():
a = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg').content
with open('testFile.zip', 'wb') as i:
    i.write(a.content)


# чек версии программы
def versionCheck():
    fileForHash = hashlib.md5()
    with open('TrajectoryConverter.exe', 'rb') as fileType: 
        buf = fileType.read()
        fileForHash.update(buf)
        checkSum = str(fileForHash.hexdigest())
    print(checkSum)

#versionCheck()


# распакует архив в папку с именем 'Tempfolder'
def fileExtraction():
    path = 'C:/git/Updater/'
    os.system(path)
    with zipfile.ZipFile('file.zip', 'r') as myZipFile:
        myZipFile.extractall('TempFolder')                      






# убить старую СКАДУ
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "App.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

#processKilling()


# архивировать работавшую СКАДУ
def fileArchivation():
    with zipfile.ZipFile('BackupScada.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile: 
        myZipFile.write('App.exe')                         # добавляем в архив первый файл


# удалить прошлый EXE файл
os.remove('./App.exe') #удаление файла в текущей папке


# запустить новый EXE с аргументами
def fileRun():
    os.chdir(r'C:\git\proxygnss\cmake-build-debug\App')
    path = 'start' + ' ' + 'App.exe' + ' ' + 'span6' + ' ' + '20000'
    os.system(path)

#fileRun()





