'''
Project: LearningProject
@author: Mayc
Create time: 2020-11-16 16:06
IDE: PyCharm
Introduction:
'''
import os
import random
import argparse


class PairGenerator:
    def __init__(self, data_dir, pairs_filepath, img_ext):
        """
        Parameter data_dir, is your data directory.
        Parameter pairs_filepath, where is the pairs.txt that belongs to.
        Parameter img_ext, is the image data extension for all of your image data.
        """
        self.data_dir = data_dir
        self.pairs_filepath = pairs_filepath
        self.img_ext = img_ext

    def write_item_label_abc(self):
        cnt = 0
        names = []
        for name in os.listdir(self.data_dir):
            names.append(name)

        names = sorted(names)

        for name in names:
            print(name)
            a = []
            f = open(self.pairs_filepath, 'a+')
            for file in os.listdir(self.data_dir + '/' + name):
                if file == ".DS_Store":
                    continue
                a.append(data_dir + '/' + name + '/' + file)
                f.write(str(1) + '\t' + data_dir + '/' + name + '/' + file + '\t' + str(name) + '\n')
            cnt = cnt + 1




if __name__ == '__main__':

    # arguments to pass in command line
    parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
    parser.add_argument('--dataset-dir', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
    parser.add_argument('--list-file', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
    parser.add_argument('--img-ext', default='', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
    # reading the passed arguments
    args = parser.parse_args()
    data_dir = args.dataset_dir
    lst = args.list_file
    img_ext = args.img_ext
    # generatePairs = PairGenerator(data_dir, pairs_filepath, img_ext)
    # generatePairs.write_item_label()
    # generatePairs = PairGenerator(data_dir, pairs_filepath, img_ext)
    generatePairs = PairGenerator(data_dir, lst, img_ext)
    generatePairs.write_item_label_abc() # looping through our dataset and creating 1 ITEM_PATH LABEL lst file
    # generatePairs.generate_pairs() # to use, please uncomment this line
    # generatePairs.generate_non_pairs() # to use, please uncomment this line

    # generatePairs = PairGenerator(dataset_dir, test_txt, img_ext)
    # generatePairs.split_to_10()
