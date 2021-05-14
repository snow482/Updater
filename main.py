
if __name__ == "__main__":
    import Part_1
    import killer
    
    fileVersionFromJson = Part_1.gettingJson()

    currentFileVersion = Part_1.getFileProperties(r'C:\Scada2\\tsetup.2.4.2.exe')['FileVersion']

    

    if fileVersionFromJson != currentFileVersion:
        try:
            Part_1.saveFileFromServer()

    print(currentFileVersion)



    #
    #killer.savingArchive()
    '''if Part_1.versionCheck() != True:
       pass
    else:
        print('don\'t need to update')'''