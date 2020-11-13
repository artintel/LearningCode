# CMC曲线
# 需要提供predict_label和test_y这两个变量
# 需要安装numpy和matplotlib这两个包
import numpy as np
import matplotlib.pyplot as plt
from CMC_rank.CMC_data_file import CMC

test_cmc1 = []  #保存accuracy
test_cmc2 = []  #保存accuracy
test_cmc3 = []  #保存accuracy
test_cmc1 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79ear_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79ear_isre_pipeilist.txt', 79, 'min')
test_cmc2 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79face_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\\79face_isre_pipeilist.txt', 79, 'min')
test_cmc3 = CMC('D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\gtface_isre_pipeilabel.txt', 'D:\PycharmProjects\LearningProject\CMC_rank\\resualt_txt\gtface_isre_pipeilist.txt', 50, 'min')


test_cmc1 = np.array(test_cmc1) * 100.0
test_cmc2 = np.array(test_cmc2) * 100.0
test_cmc3 = np.array(test_cmc3) * 100.0


#创建绘图对象
plt.figure(figsize=(13, 8))

x = np.arange(0, 20)
plt.xlim(0.9, 16.1)
fig_x_ticks = np.arange(1, 16, 1)
plt.xticks(fig_x_ticks)
plt.plot(x + 1, test_cmc1, color="red", linewidth=2, label='79ear', marker="o")
plt.plot(x + 1, test_cmc2, color="yellow", linewidth=2, label='79face', marker="^")
plt.plot(x + 1, test_cmc3, color="black", linewidth=2, label='GT50', marker="p")

plt.legend()
plt.xlabel("Rank")  
plt.ylabel("Recognition rate (%)")
plt.legend(loc='lower right', fontsize='xx-large')
plt.title("CMC curves")
plt.grid(ls='--')
plt.show()