import os
import shutil
import tkinter
import tkinter.filedialog

#Define format and directoryoutput
definitions=[['doc',['.docx','.doc','.xls','.xlsx','.xps','.oxps']],['Music',['.mp3']],['Videos',['.mp4','.mvi','.avi']],['pdf',['.pdf']],['compressed',['.zip','.7z','.rar','.xz','.bz2','.tgz']],['images',['.jpg','.JPG','.tif','.jpeg','.png','.gif']],['textfiles',['.txt','.json','.py']],['programs',['.msi','.exe','.EXE']]]
cur_dir='C:\\Users\\Zombie\\Downloads'

cur_dir = tkinter.filedialog.askdirectory(initialdir="/",title='Please select a directory')

print(cur_dir)


def CreateDir(items_dir):
    try:
        if not os.path.isdir(str(items_dir)):
            os.makedirs(items_dir)
    except OSError as e:
        if not os.path.isdir(str(items_dir)):
            raise

def MoveItems(item,originalpath,destpath):
    items_dir = cur_dir + '\\' + destpath
    try:
        shutil.move(originalpath + '\\' + item,items_dir)
    except shutil.Error as e:
        print(e)



#loop through each definition
for definition in definitions:
    items = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1]  in definition[1]]
    if len(items) > 0:
            CreateDir(cur_dir +'\\'+str(definition[0]))
            for i in items:
                MoveItems(i,cur_dir,str(definition[0]))
            print (definition[0]+' found -',len(items))
    
for item in os.listdir(cur_dir):
    if not os.path.isdir(cur_dir+'\\'+item):
        curext=os.path.splitext(item)[1]
        CreateDir(cur_dir +'\\Other\\'+curext)
        MoveItems(item,cur_dir,'\\Other\\'+curext)
        print (curext+' found -')

