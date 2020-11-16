'''
Project: LearningProject
@author: Mayc
Create time: 2020-11-16 15:47
IDE: PyCharm
Introduction:
'''
#给图片添加padding
import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc
import os
def resize112(rootpath):
    '''

    Args:
        root_path: D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\L+R
                    - 1-1.jpg
                    - 1-2.jpg
                    - 1-3.jpg
                    - 1-4.jpg
                    - 2-4.jpg
                    ...
                    - xxx.jpg

    Returns:
        No returns

    '''
    BLUE=[255,255,255]
    list = os.listdir(rootpath) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        filepath = os.path.join(rootpath, list[i])
        imagepaths =os.path.join(rootpath, list[i])
        fns = os.listdir(filepath)
        fns.sort()
        for fn in fns:
            filename=os.path.join(filepath,fn)
            imagepath =os.path.join(imagepaths,fn)
            imagepath =imagepath[:-4]+'.bmp'
            img1=cv2.imread(filename)
            width =float(img1.shape[1])
            height = float(img1.shape[0])
            # print width
            if height == width:
                cv2.imwrite(imagepath, img1)
            if height>width:
                pad = (112.0-width)/2
                if pad%1==0.5:
                    addpad =pad+1.0
                    # constant = cv2.copyMakeBorder(img1, 0, 0, int(128.0-width),0, cv2.BORDER_CONSTANT, value=BLUE)
                    constant = cv2.copyMakeBorder(img1, 0, 0, int(addpad), int(pad), cv2.BORDER_CONSTANT, value=BLUE)
                    cv2.imwrite(imagepath, constant)
                if pad%1==0:
                    # constant = cv2.copyMakeBorder(img1, 0, 0, int(128.0-width),0 , cv2.BORDER_CONSTANT, value=BLUE)
                    constant = cv2.copyMakeBorder(img1, 0, 0, int(pad), int(pad), cv2.BORDER_CONSTANT, value=BLUE)
                    cv2.imwrite(imagepath,constant)
            if height < width:
                pad = (112.0 - height) / 2
                if pad % 1 == 0.5:
                    addpad = pad + 1.0
                    print(addpad)
                    # constant = cv2.copyMakeBorder(img1,  int(128.0 - height), 0,0,0 , cv2.BORDER_CONSTANT,value=BLUE)
                    constant = cv2.copyMakeBorder(img1, int(addpad), int(pad),0,0,cv2.BORDER_CONSTANT, value=BLUE)
                    cv2.imwrite(imagepath, constant)
                if pad % 1 == 0:
                    # constant = cv2.copyMakeBorder(img1,  int(128.0 - height), 0, 0,0,cv2.BORDER_CONSTANT, value=BLUE)
                    constant = cv2.copyMakeBorder(img1, int(pad), int(pad),0,0, cv2.BORDER_CONSTANT, value=BLUE)
                    cv2.imwrite(imagepath, constant)

if __name__ == '__main__':
    resize112(r'D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\EAR_Probe')