import os
import psutil
import time
import win32api

#==============================================================================
def getFileProperties(fname):
#==============================================================================
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

print(type(getFileProperties('C:\Scada2\CLion-2020.2.3.exe')))


tmpr = getFileProperties('C:\Scada2\CLion-2020.2.3.exe')

'''
tm = json.loads(tmpr)
newJson = json.dumps(tmp, indent=4) # для отображения удобного, indent=4 - 4 отступа
print(newJson)
'''


#print(tmpr.get("FixedFileInfo"))



'''try: 
    def versionCheck():
        currentVersion = 0
        newVersion = 0
        #os.chdir(r'c:\\users\\snow-pc\\downloads\\testFolder')
        with open(r'c:\\users\\snow-pc\\downloads\\testFolder\\version.txt', 'r') as v:
            currentVersion = v.read()

        #os.chdir(r'c:\\git\\Updater')
        with open(r'c:\\git\\Updater\\version.txt', 'r') as v_new:
            newVersion = v_new.read()
        print(currentVersion)
        print(newVersion)

        if currentVersion != newVersion:
            print('current version is - ' + currentVersion +
                'new version - ' + newVersion + ', need to update')
        else:
            print('need update')
            
except ValueError:
    print('error')
#finally: 
    print('all good')'''








'''def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "explorer.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")


def ExplorerRun():
    path = 'start' + ' ' + 'explorer.exe'
    os.system(path)


def main():
    processKilling()
    time.sleep(10)
    ExplorerRun()


if __name__ == '__main__':
    main()'''


