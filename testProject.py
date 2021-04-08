import os
import zipfile
import shutil

myFile = open("file.txt", "w")
myFile.write("madmefed")
myFile.close()

print(os.getcwd())

#shutil.copyfile("./file.txt", "./file1.txt") - копирование файла (./ - тукущая дирректория)

#создаем zip файл
with zipfile.ZipFile('files1.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZipFile:   # сжимаем файл в zip с именем "files1.zip", флаг "w (запись)", тип сжатия, 
                                                                                          # переменная с именем myZipFile 
    myZipFile.write('file.txt')                         # добавляем в архив первый файл
    myZipFile.write('file1.txt')                        # добавляем в архив второй файл

# https://www.youtube.com/watch?v=z0gguhEmWiY
