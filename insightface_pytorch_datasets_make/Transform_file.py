'''
Project: LearningProject
@author: Mayc
Create time: 2020-11-13 21:29
IDE: PyCharm
Introduction:
'''
import os
import shutil
def move_file_own(rootdir):

    '''
    Args:
        rootdir: - imagefile
                    - 1-1.jpg
                    - 1-3.jpg
                    - 2-4.jpg
                    ...
                    - xxx.jpg

    Returns: no returns

    '''

    # 想要移动文件所在的根目录
    # 获取目录下文件名清单
    list = os.listdir(rootdir)

    # 移动图片到指定文件夹
    for item in list:  # 遍历该文件夹中的所有文件 # item : 1-1.jpg
        if not os.path.exists(rootdir + '/' + item.split('-')[0]):
            os.makedirs(rootdir + '/' + item.split('-')[0])
        shutil.move(os.path.join(rootdir, item), rootdir + '/' + item.split('-')[0] + '/' + item)
def move_file_L_R(left_root, right_root, target_root):
    '''
    有两个文件夹，每个文件夹的格式和move_file_own是一样的格式，
        每一组每隔两个图片选一张出来，最后都放在 target_root 里

    Args:
        left_root: D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\EAR_L
                    - 1-1.jpg
                    - 1-2.jpg
                    - 1-3.jpg
                    - 1-4.jpg
                    - 2-4.jpg
                    ...
                    - xxx.jpg
        right_root: D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\EAR_R
                    - 1-1.jpg
                    - 1-2.jpg
                    - 1-3.jpg
                    - 1-4.jpg
                    - 2-4.jpg
                    ...
                    - xxx.jpg
        重新排序
        target_root: D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\USTB3\L+R
                    - 1-1.jpg
                    - 1-2.jpg
                    - 1-3.jpg
                    - 1-4.jpg
                    - 2-4.jpg
                    ...
                    - xxx.jpg

    Returns: No return
    '''

    list_left = os.listdir(left_root)
    list_right = os.listdir(right_root)
    # 移动图片到指定文件夹
    for item in list_left:  # 遍历该文件夹中的所有文件 # item : 1-1.jpg
        if not os.path.exists(target_root + '/' + item.split('-')[0]):
            os.makedirs(target_root + '/' + item.split('-')[0])
        num = item.split('-')[1]
        num = num[:-4]
        if((int(num) % 2 == 0) & (int(num) != 18)):
            shutil.move(os.path.join(left_root, item), target_root + '/' + item.split('-')[0] + '/' + item.split('-')[0] + '-' + str(len(os.listdir(target_root + '/' + item.split('-')[0])) + 1) + '.bmp')

    for item in list_right:  # 遍历该文件夹中的所有文件 # item : 1-1.jpg
        if not os.path.exists(target_root + '/' + item.split('-')[0]):
            os.makedirs(target_root + '/' + item.split('-')[0])
        num = item.split('-')[1]
        num = num[:-4]
        if((int(num) % 2 == 0) & (int(num) != 22)):
            shutil.move(os.path.join(right_root, item), target_root + '/' + item.split('-')[0] + '/' + item.split('-')[0] + '-' + str(len(os.listdir(target_root + '/' + item.split('-')[0])) + 1) + '.bmp')

if __name__ == '__main__':
    move_file_own('D:/PycharmProjects/LearningProject/insightface_pytorch_datasets_make/USTB3/EAR_Gallery')
    move_file_L_R('D:/PycharmProjects/LearningProject/insightface_pytorch_datasets_make/USTB3/EAR_L', 'D:/PycharmProjects/LearningProject/insightface_pytorch_datasets_make/USTB3/EAR_R', 'D:/PycharmProjects/LearningProject/insightface_pytorch_datasets_make/USTB3/L+R')
