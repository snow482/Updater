import os
from multiprocessing import Process

# запуск программы
def fileRun():
    os.chdir(r'C:\git\proxygnss\cmake-build-debug\App')
    path = 'start' + ' ' + 'App.exe' + ' ' + 'span6' + ' ' + '20000'
    os.system(path)
    
fileRun()