import os
import psutil
import time


def processKilling(): 
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
    main()


