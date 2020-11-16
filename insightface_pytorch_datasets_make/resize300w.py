'''
Project: LearningProject
@author: Mayc
Create time: 2020-11-16 14:54
IDE: PyCharm
Introduction:
'''
import os
from PIL import Image
#resize图片
def resize300w(rootpath):
    '''

    Args:
        root_path: D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\EAR_Probe
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
    list = os.listdir(rootpath) #列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootpath, list[i])
        #print('path',path)
        earpath=os.listdir(path)
        #print('earpath',earpath)
        for j in range(0, len(earpath)):
            orinpath=path+'/'+earpath[j]
            #print('orinpath',orinpath)
            im = Image.open(orinpath)
            (x, y) = im.size
            # print x
            # print y
            if y >= x:
                w_divide_h =112.0/y
            if y < x:
                w_divide_h = 112.0 /x
                #print 666
            # print w_divide_h
            x_s = int(x * w_divide_h)
            # y_s = int(y * w_divide_h)
            y_s = int(112)
            out = im.resize((x_s, y_s), Image.ANTIALIAS)
            if not os.path.exists(rootpath + '/' + list[i]):
                os.makedirs(rootpath + '/' + list[i])
            out.save(rootpath + '/' + list[i] + '/' +earpath[j][:-4]+'.bmp')

if __name__ == '__main__':
    resize300w(r'D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\EAR_Probe')
