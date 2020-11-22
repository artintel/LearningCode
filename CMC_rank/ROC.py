'''
Project: LearningProject
@author: Mayc
Create time: 2020-11-20 14:47
IDE: PyCharm
Introduction:
'''

import numpy as np
import matplotlib.pyplot as plt

def farfrr(path):
    farlist = []
    with open(path, 'r') as fd:
        pairs = fd.readlines()
        # print (pairs)
        far = pairs[0][1:-1].split(', ')
        for f in far:
            farlist.append(float(f) * 100)
    return farlist


def hua():

    farlist = np.loadtxt(r'D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\far_MDII_jizhun_fusion.txt')
    frrlist = np.loadtxt(r'D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\frr_MDII_jizhun_fusion.txt')
    farlist = farlist * 100
    frrlist = frrlist * 100

    farlist111 = []
    frrlist111 = []
    count = 0;
    for a, b in zip(farlist, frrlist):
        if a == b:
            x = a;
        if (a == b) | (count % 1000 == 0) :
            farlist111.append(a)
            frrlist111.append(b)
        count+=1
    farlist111 = np.array(farlist111)
    frrlist111 = np.array(frrlist111)
    print((farlist111 - frrlist111).any() == 0)


    farlist1 = np.loadtxt('D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\far_MDII_isre_fusion.txt')
    frrlist1 = np.loadtxt('D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\frr_MDII_isre_fusion.txt')
    farlist1 = farlist1 * 100
    frrlist1 = frrlist1 * 100

    farlist2 = np.loadtxt('D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\far_MDII_scr_fusion.txt', delimiter=',')
    frrlist2 = np.loadtxt('D:\PycharmProjects\LearningProject\CMC_rank\ROC\MD2\\frr_MDII_scr_fusion.txt', delimiter=',')
    farlist2 = farlist2 * 100
    frrlist2 = frrlist2 * 100

    plt.figure(figsize=(10, 6))
    line1, = plt.plot(farlist, frrlist, color='green', lw=2)

    plt.plot(farlist1, frrlist1, color='red', lw=3)
    plt.plot(farlist1, frrlist1, color='red', lw=3)
    line2, = plt.plot(farlist1, frrlist1, color='red', lw=2)
    line3, = plt.plot(farlist2, frrlist2, color='blue', lw=2)

    plt.xlim(0.0, 0.10)
    fig_x_ticks = np.arange(0.0, 0.01, 0.001)
    plt.xticks(fig_x_ticks)

    plt.tick_params(labelsize=19)
    plt.xlim(0, 0.01)
    plt.ylim(0, 0.01)
    plt.xlabel('FAR(%)', size=19)
    plt.ylabel('FRR(%)', size=19)
    plt.title('MD II', size=19)
    plt.grid(linestyle='dotted')
    plt.legend([line1, line2, line3], ('Sum rule', 'SRC-sce', 'SRC-scr'), loc="upper right", prop={'size': 19})
    plt.show()


if __name__ == '__main__':
    hua()
