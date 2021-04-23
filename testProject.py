import os
import zipfile
import shutil
import requests

'''myFile = open("file.txt", "w")
myFile.write("madmefed")
myFile.close()'''

print(os.getcwd())

#copyfile("./file.txt", "./file2.txt") #- копирование файла (./ - текущая дирректория)
#os.remove('./file1.txt') - удаление файла
#os.makedirs('dir2') #- удаление дирректории
path = 'C:/git/Updater/dir2'
os.removedirs(path) #- удаление дирректории

#создаем zip файл
#with zipfile.ZipFile('files1.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile:   # сжимаем файл в zip с именем "files1.zip", флаг "w (запись)", тип сжатия, 
                                                                                          # переменная с именем myZipFile 
    #myZipFile.write('file.txt')                         # добавляем в архив первый файл
    #myZipFile.write('file1.txt')                        # добавляем в архив второй файл

# https://www.youtube.com/watch?v=z0gguhEmWiY

#with zipfile.ZipFile('file1.zip', 'r') as myZipFile:
    #print(myZipFile.namelist())                         # выведет, что имеется в архиве
    #myZipFile.extract('file1.txt')                      # распакует лишь один файл с именем file1.txt
    #myZipFile.extractall('folder')                      # распакует архив в папку с именем 'folder'


#shutil.make_archive('zipFile', 'zip', 'folderName')     # создать архив с именем zipFile, тип zip, из папки 'folderName'
#shutil.unpack_archive('zipFile.zip', 'nameOfFolder')    # распаковать архив с именем zipFile.zip в папку nameOfFolder


#r = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg')

#a = requests.get('https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe').content
#with open('dwarf.exe', 'wb') as i:
#    i.write(a.content)
#with open('pyzip1.zip', 'wb') as z:
#    z.write(a.content)

# https://www.youtube.com/watch?v=tb8gHvYlCFs