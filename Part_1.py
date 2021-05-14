#назначить интерпретатор???

#import main
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
import win32api


checkHash = 'httpbin.org'
jsonHashValue = ''


# POST запрос по ссылке на скачку архива по URL
def gettingJson():
    
    responce = requests.get('https://httpbin.org/get').content
    tmp = json.loads(responce)
    #newJson = json.dumps(tmp, indent=4) # для отображения удобного, indent=4 - 4 отступа
    #print(newJson)
    jsonHashValue = tmp['headers']['Host']
    
    return jsonHashValue

#if checkHash == jsonHashValue:
#    print('true') 


# GET запрос по ссылке на скачку архива по URL
def saveFileFromServer():
    a = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg')
    with open('image.png', 'wb') as i:
        i.write(a.content)
    with zipfile.ZipFile('test.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile:
        myZipFile.write('image.png', 'version.txt')    

#saveFileFromServer()


def archiveSaving():
    responce = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg')
    if os.path.exists(r'C:\Scada2\Downloads'):
        with open(r'C:\Scada2\Downloads\App.png', 'wb') as way:
            way.write(responce.content)




def getFileProperties(fname):

    """
    Read all properties of the given file return them as a dictionary.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            ## print str_info
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        pass

    return props





# поиск файлов с расширением .exe, добавление в массив и поиск в массиве конкретного
def findFile():
    name = "App.exe"
    neededFile = []
    os.chdir(r'c:\\users\\snow-pc\\downloads')
    for file in glob.glob("*.exe"):
        neededFile.append(file)
    if name in neededFile:
        print("yes")

#findFile()



# чек хеша программы
def versionCheck():
    fileForHash = hashlib.md5()
    with open('test.zip', 'rb') as fileType: 
        buf = fileType.read()
        fileForHash.update(buf)
        checkSum = str(fileForHash.hexdigest())
    return checkSum
    #print(checkSum)

#fileHash = versionCheck()


'''if checkHash == jsonHashValue:
    print('true')
else: 
    print('something wrong')
print(fileHash)'''

# берем hash с json и с функции versionCheck() и сравниваем их
# если ок, то значит все скачалось, идем дальше, если нет, попробовать сначала???


# распакует архив в папку с именем 'Tempfolder'
def fileExtraction():
    path = 'cd' + ' ' + 'c:\\git\\Updater'
    os.system(path)
    with zipfile.ZipFile('test.zip', 'r') as myZipFile:
        myZipFile.extractall('TempFolder')

#fileExtraction()


# зайти в файл version.txt, проверить версию программы
def versionCheck():
    os.chdir(r'c:\\users\\snow-pc\\downloads\\testFolder')
    with open('version.txt', 'r') as v:
        currentVersion = v.read()

    os.chdir(r'c:\\git\\Updater')
    with open('version.txt', 'r') as v_new:
        newVersion = v_new.read()
    if currentVersion == newVersion:
        print('good')




def imageRun():
    os.chdir(r'C:\\git\\Updater')
    path = 'start' + ' ' + 'mspaint.exe' + ' ' + 'image.png'
    os.system(path)
    
#imageRun()

#time.sleep(4)

# убить старую СКАДУ
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "mspaint.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

#processKilling()


# архивировать работавшую СКАДУ
def fileArchivation():
    with zipfile.ZipFile('BackupImage.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile: 
        myZipFile.write('image.png')                         # добавляем в архив первый файл

#fileArchivation()

# удалить прошлый EXE файл
#os.remove('./image.png') #удаление файла в текущей папке

# копирование нового EXE файла из временной папки

'''if (shutil.copyfile("./TempFolder/image.png", "././image1.png")):
    print('good')
'''

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
    
#removeTempFolder()


def image1Run():
    os.chdir(r'C:\\git\\Updater')
    path = 'start' + ' ' + 'mspaint.exe' + ' ' + 'image1.png'
    os.system(path)
#image1Run()


