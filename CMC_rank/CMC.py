# CMC曲线
# 需要提供predict_label和test_y这两个变量
# 需要安装numpy和matplotlib这两个包
import numpy as np
import matplotlib.pyplot as plt
from CMC_rank.CMC_data_file import CMC

test_cmc1 = []  #保存accuracy
test_cmc2 = []  #保存accuracy
test_cmc3 = []  #保存accuracy
test_cmc4 = []  #保存accuracy
test_cmc5 = []  #保存accuracy
test_cmc6 = []  #保存accuracy
# test_cmc1 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79ear_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79ear_isre_pipeilist.txt', 79, 'min')
# test_cmc2 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79face_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79face_isre_pipeilist.txt', 79, 'min')
# test_cmc3 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\gtface_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\gtface_isre_pipeilist.txt', 50, 'min')

test_cmc1 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ar79_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ar79_pipeilist.txt', 79, 'min')
# test_cmc2 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_pipeilist.txt', 50, 'min')
test_cmc3 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\gtface_isre_pipeilabel_3399.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\gtface_isre_pipeilist_3399.txt', 50, 'min')
test_cmc4 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pp_isre_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pp_isre_pipeilist.txt', 100, 'min')
test_cmc5 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_0.05_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_0.05_pipeilist.txt', 50, 'min')
test_cmc6 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER79_0.05_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER79_0.05_pipeilist.txt', 79, 'min')


test_cmc1 = np.array(test_cmc1) * 100.0
test_cmc3 = np.array(test_cmc3) * 100.0
test_cmc4 = np.array(test_cmc4) * 100.0
test_cmc5 = np.array(test_cmc5) * 100.0
test_cmc6 = np.array(test_cmc6) * 100.0




#创建绘图对象
plt.figure(figsize=(13, 8))

x = np.arange(0, 20)
plt.xlim(0.9, 16.1)
fig_x_ticks = np.arange(1, 16, 1)
plt.xticks(fig_x_ticks)
plt.plot(x + 1, test_cmc1, color="red", linewidth=2, label='AR', marker="o")
plt.plot(x + 1, test_cmc3, color="black", linewidth=2, label='GT', marker="p")
plt.plot(x + 1, test_cmc4, color="green", linewidth=2, label='PALM', marker="x")
plt.plot(x + 1, test_cmc5, color="cyan", linewidth=2, label='EAR', marker=">")
plt.plot(x + 1, test_cmc6, color="darkblue", linewidth=2, label='ER_79', marker="<")

plt.legend()
plt.xlabel("Rank")  
plt.ylabel("Recognition rate (%)")
plt.legend(loc='lower right', fontsize='xx-large')
plt.title("CMC curves")
plt.grid(ls='--')
plt.show()