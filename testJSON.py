import os
import json
import requests
import hmac
import hashlib 
from shutil import copyfile






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