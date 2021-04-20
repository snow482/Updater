import os
import subprocess
import glob
import json
import requests
import hmac
import hashlib 
from shutil import copyfile


# убитие процессов
"""def scriptStart():
    
    for processName in psutil.process_iter():
        if processName.name() == "explorer.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

scriptStart()"""

cmd = "dwarf.png"
os.system(cmd)
#subprocess.run('DiscordSetup.exe')


'''import glob
os.chdir("c:\git")
for file in glob.glob("*.txt"):
    print(file)'''


"""def find_files(filename, search_path):
   result = []
# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

print(find_files("*txt","C:\git"))"""



'''#path = r"C:\\Downloads"
for root, dirs, files in os.walk("/Downloads"):
    for file in files:
        if file.endswith('.exe'):
            path_file = os.path.join(root, file)
            print(path_file)'''





'''#чек версии программы
def versionCheck():
    fileForHash = hashlib.md5()
    with open('TrajectoryConverter.exe', 'rb') as fileType: 
        buf = fileType.read()
        fileForHash.update(buf)
    print(fileForHash.hexdigest())

versionCheck()'''



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