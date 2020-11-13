#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from PIL import Image
#resize图片
import shutil
rootpath = 'D:\learning_data\datasets\\test\\'
# rootpath = 'C:\Users\Admin\Desktop\\arcface\\test'
list = os.listdir(rootpath) #列出文件夹下所有的目录与文件
for i in range(0, len(list)):
    path = os.path.join(rootpath, list[i])
    #print('path',path)
    earpath=os.listdir(path)
    #print('earpath',earpath)
    for j in range(0,len(earpath)):
        orinpath=path+'/'+earpath[j]
        #print('orinpath',orinpath)
        im = Image.open(orinpath)
        (x, y) = im.size
        # print x
        # print y
        if y>=x:
            w_divide_h =112.0/y
        if y<x:
            w_divide_h = 112.0 /x
            #print 666
        # print w_divide_h
        x_s = int(x * w_divide_h)
        # y_s = int(y * w_divide_h)
        y_s = int(112)
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        if not os.path.exists('D:\learning_data\datasets\\test\\new'+list[i]):
            os.makedirs('D:\learning_data\datasets\\test\\new'+list[i])
        out.save('D:\learning_data\datasets\\test\\new'+list[i]+'/'+earpath[j][:-4]+'.jpg')
