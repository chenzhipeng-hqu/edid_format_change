#!/usr/bin/env python    
#encoding: utf-8

import os, sys, time

#SrcFilename = r'C:\Users\cvter\Desktop\edid.txt'
#DstFilename = r'C:\Users\cvter\Desktop\edid.bin'
SrcFilename = r'EDID_Tool\edid.txt'
DstFilename = r'EDID_Tool\edid.bin'

__author__ = 'chenzhipeng3472'
import struct
if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    print (time)
    print("SrcFilename =",SrcFilename)
    print("DstFilename =",DstFilename)
    #print ("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))  # 获取当前文件__file__的路径
    #print ("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__))) # 获取当前文件__file__的所在目录
    #print ("sys.path[0]=%s" % sys.path[0])  #sys.path[0]或sys.argv[0] “D:\python_test”，取的是被初始执行的脚本的所在目录
    if os.path.isfile(DstFilename):
       os.remove(DstFilename)
       print ("remove current DstFile")
       
    srcfp = open(SrcFilename).readlines()
    list = []
    
    for line in srcfp:
        line = line[5:]
        line = line.replace("  ","")
        line = line.lstrip().rstrip()      
        for i in range(0, len(line), 2):
            hexItem = line[i] + line[i+1]
            list.append(int(hexItem, 16))
            
    with open(DstFilename, 'wb') as dstfp:
        for byte in list:
            dstfp.write(struct.pack('B', byte))
    dstfp.close()
    print ("edid has created") 
