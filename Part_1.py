#назначить интерпретатор???

import os, sys
import glob
import time
import shutil
import psutil
import json
import zipfile
import requests
import hmac
import hashlib 

checkHash = '6c9c373f59631e76b7f237db7e2c4938'

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
    a = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg')
    with open('image.png', 'wb') as i:
        i.write(a.content)
    with zipfile.ZipFile('test.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile:
        myZipFile.write('image.png')    

saveFileFromServer()

# чек версии программы
def versionCheck():
    fileForHash = hashlib.md5()
    with open('test.zip', 'rb') as fileType: 
        buf = fileType.read()
        fileForHash.update(buf)
        checkSum = str(fileForHash.hexdigest())
    return checkSum
    #print(checkSum)

fileHash = versionCheck()

if fileHash == checkHash:
    print('true')
else: 
    print('something wrong')
print(fileHash)

# берем hash с json и с функции versionCheck() и сравниваем их
# если ок, то значит все скачалось, идем дальше, если нет, попробовать сначала???


# распакует архив в папку с именем 'Tempfolder'
def fileExtraction():
    path = 'cd' + ' ' + 'c:\\git\\Updater'
    os.system(path)
    with zipfile.ZipFile('test.zip', 'r') as myZipFile:
        myZipFile.extractall('TempFolder')

fileExtraction()

def imageRun():
    os.chdir(r'C:\\git\\Updater')
    path = 'start' + ' ' + 'mspaint.exe' + ' ' + 'image.png'
    os.system(path)
imageRun()
time.sleep(4)
# убить старую СКАДУ
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "mspaint.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

processKilling()


# архивировать работавшую СКАДУ
def fileArchivation():
    with zipfile.ZipFile('BackupImage.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile: 
        myZipFile.write('image.png')                         # добавляем в архив первый файл

fileArchivation()

# удалить прошлый EXE файл
os.remove('./image.png') #удаление файла в текущей папке

# копирование нового EXE файла из временной папки

if (shutil.copyfile("./TempFolder/image.png", "././image1.png")):
    print('good')


# запустить новый EXE с аргументами
def fileRun():
    os.chdir(r'C:\\git\\proxygnss\\cmake-build-debug\\App')
    path = 'start' + ' ' + 'App.exe' + ' ' + 'span6' + ' ' + '20000'
    os.system(path)

#fileRun()

#удаление временной папки
def removeTempFolder():
    shutil.rmtree('c:\\git\\Updater\\TempFolder')
    os.remove('./test.zip')
    
removeTempFolder()


def image1Run():
    os.chdir(r'C:\\git\\Updater')
    path = 'start' + ' ' + 'mspaint.exe' + ' ' + 'image1.png'
    os.system(path)
image1Run()



