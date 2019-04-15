#!c:\python27\python.exe
# -- coding: utf-8 --
import cv2
import subprocess
import sys
import io
import os
import argparse

def v2a(vPath,outPath):
    outPath=outPath[:-4]+'.mp3'
    task=["ffmpeg","-i",vPath,"-f","mp3",outPath]
    subprocess.check_call(task, shell = True)
    return outPath

def vaAdd(vPath,aPath):
    outPath=vPath[:-4]+'.mp4'
    task=["ffmpeg","-i",vPath,"-i",aPath,"-strict","-2","-f","mp4",outPath]
    subprocess.check_call(task, shell = True)

def oneFix(srcPath):
    outDir='D:\\Download\\Temp\\'
    outPath=outDir+srcPath.split('\\')[-1][:-4]+'.avi'

    srcVideo = cv2.VideoCapture(srcPath)
    fps = srcVideo.get(cv2.CAP_PROP_FPS) 
    size = (int(srcVideo.get(cv2.CAP_PROP_FRAME_WIDTH)),int(srcVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
    outVideo = cv2.VideoWriter(outPath,cv2.cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps, size)

    srcImg = cv2.imread('D:\\Download\\testPic.jpg')
    srcRet,srcBinary =cv2.threshold(cv2.cvtColor(srcImg,cv2.COLOR_RGB2GRAY),245,255,cv2.THRESH_BINARY)

    num = -2
    success, frame = srcVideo.read()
    while success :
        num = num+1
        ret,binary =cv2.threshold(cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY),245,255,cv2.THRESH_BINARY)
        hist = srcBinary-binary
        if hist.sum()<50000:
            print num
            outVideo.write(tmpFrame)
        else:
            outVideo.write(frame)
            tmpFrame = frame
        sys.stdout.write(str(int((num*1.0)/srcVideo.get(cv2.CAP_PROP_FRAME_COUNT)*10000)/100.0)+'%'+"\r")
        success, frame = srcVideo.read()
    srcVideo.release()

    auPath=v2a(srcPath,outPath)
    #vaAdd(outPath,auPath)

def oneCheck(srcPath):
    tempPath=srcPath[:-4]+'.txt'

    srcVideo = cv2.VideoCapture(srcPath)
    srcImg = cv2.imread('testPic.jpg')
    srcRet,srcBinary =cv2.threshold(cv2.cvtColor(srcImg,cv2.COLOR_RGB2GRAY),245,255,cv2.THRESH_BINARY)

    num = -2
    success, frame = srcVideo.read()
    while success :
        num = num+1
        ret,binary =cv2.threshold(cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY),245,255,cv2.THRESH_BINARY)
        hist = srcBinary-binary
        if hist.sum()<50000:
            context=str(num).encode('utf-8')
            tempFile = io.open(tempPath,mode='wb+')
            tempFile.write(context+'\r\n')
            tempFile.close()
            break
        sys.stdout.write(str(int((num*1.0)/srcVideo.get(cv2.CAP_PROP_FRAME_COUNT)*10000)/100.0)+'%'+"\r")
        success, frame = srcVideo.read()

#参数输入
parser=argparse.ArgumentParser()
parser.add_argument('-p',help='Path to the MP4 Folder')
args = parser.parse_args()
if args.p:
    tempDirPath=args.p
    for dirpath, dirnames, filenames in os.walk(tempDirPath):
        for filepath in filenames:
            tempPath = os.path.join(dirpath, filepath)
            if filepath[-4:]=='.mp4' or filepath[-4:]=='.MP4':
                oneFix(tempPath)