import os
import psutil

# убитие процессов
def processKilling(): 
    for processName in psutil.process_iter():
        if processName.name() == "App.exe":
            os.system("taskkill /PID " + str(processName.pid) + " /F")

processKilling()




