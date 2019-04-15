#!c:\python27\python.exe
# -- coding: utf-8 --
import os
import subprocess

def vaAdd(vPath,aPath):
    outPath=vPath[:-4]+'.mp4'
    task=["ffmpeg","-i",vPath,"-i",aPath,"-strict","-2","-f","mp4",outPath]
    subprocess.check_call(task, shell = True)

tempDirPath='D:\\Download\\Temp'
for dirpath, dirnames, filenames in os.walk(tempDirPath):
    for filepath in filenames:
        tempPath = os.path.join(dirpath, filepath)
        if filepath[-4:]=='.avi' or filepath[-4:]=='.AVI':
            vaAdd(tempPath,tempPath[:-4]+'.mp3')
            if os.path.exists(tempPath):
                os.remove(tempPath)
            if os.path.exists(tempPath[:-4]+'.mp3'):
                os.remove(tempPath[:-4]+'.mp3')