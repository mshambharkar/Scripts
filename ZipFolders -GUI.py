import os
import shutil
import send2trash
import tkinter
import tkinter.filedialog

definitions=['.zip','.tar','.rar']
cur_dir='C:\\Users\\Zombie\\Downloads'

#processedobjects
compressedlist=list()
extractedfolders=list()

cur_dir = tkinter.filedialog.askdirectory(initialdir="/",title='Please select a directory')

print(cur_dir)

def ValidateFile(fileItem):
    if os.path.splitext(fileItem)[1].lower() in definitions:
        name=('.').join(os.path.basename(fileItem).split('.')[:-1])
        compressedlist.append(name)
def ValidateFolder(folderName):
    if folderName in compressedlist:
        return True
    else:
        return False

def IterateChildZip(folder):
    for fitem in os.listdir(folder):
        if os.path.isdir(folder+'\\'+fitem):
            IterateChildZip(folder+'\\'+fitem)
        else:
            ValidateFile(folder+'\\'+fitem)
def IterateChildFolder(folder):
    for fitem in os.listdir(folder):
        if os.path.isdir(folder+'\\'+fitem):
            if ValidateFolder(fitem):
                extractedfolders.append(folder+'\\'+fitem)
            else:
                IterateChildFolder(folder+'\\'+fitem)


#loop through each definition
IterateChildZip(cur_dir)
IterateChildFolder(cur_dir)
print(compressedlist)
print(extractedfolders)
print('Do you want to proceed with delete ? Y/N')
proceed=input()
if proceed.lower() == 'y':
    for folder in extractedfolders:
        try:
            send2trash.send2trash(folder)
            print('Moved to recycle bin-'+folder)
        except Exception as e:
            print(e)
print('done enter any key to exit')
input()
