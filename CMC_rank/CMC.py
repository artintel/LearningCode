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

test_cmc1 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ar79_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ar79_pipeilist.txt', 79, 'min')
# test_cmc2 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_pipeilist.txt', 50, 'min')
test_cmc2 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\gtface_isre_pipeilabel_3399.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\gtface_isre_pipeilist_3399.txt', 50, 'min')
test_cmc3 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pp_isre_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pp_isre_pipeilist.txt', 100, 'min')
test_cmc4 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_0.05_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\ER50_0.05_pipeilist.txt', 50, 'min')
test_cmc5 = CMC(r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pre\79ear_isre_pipeilabel.txt', r'D:\PycharmProjects\LearningProject\CMC_rank\resualt_txt\pre\ER79_0.05_pipeilist.txt', 79, 'min')

score = []

test_cmc1 = np.array(test_cmc1) * 100.0
test_cmc2 = np.array(test_cmc2) * 100.0
test_cmc3 = np.array(test_cmc3) * 100.0
test_cmc4 = np.array(test_cmc4) * 100.0
test_cmc5 = np.array(test_cmc5) * 100.0
score.append('AR:       ' + str(list(test_cmc1[:16])) + '\n')
score.append('GT:       ' + str(list(test_cmc2[:16])) + '\n')
score.append('Palam:    ' + str(list(test_cmc3[:16])) + '\n')
score.append('ER:       ' + str(list(test_cmc4[:16])) + '\n')


score_cmc = []
f = open('D:\PycharmProjects\LearningProject\CMC_rank\\test_cmc.txt', 'a')
for scores in score:
    f.write(scores)

# test_cmc = []

# for i in range(4):
#     f = open('D:\PycharmProjects\LearningProject\CMC_rank\\test_cmc.txt', 'a')
#     for scope in range(16):
#         test_cmc.append(test_cmc + str(i + 1))
#         pass

# f1 = open('D:\PycharmProjects\LearningProject\CMC_rank\\test_cmc.txt', 'a')
# test_cmc = test_cmc1[:16]
# f1.write(str(test_cmc1))


#创建绘图对象
plt.figure(figsize=(13, 8))

x = np.arange(0, 20)
plt.xlim(0.9, 16.1)
fig_x_ticks = np.arange(1, 16, 1)
plt.xticks(fig_x_ticks)
plt.plot(x + 1, test_cmc1, color="red", linewidth=2, label='AR', marker="o")
plt.plot(x + 1, test_cmc2, color="black", linewidth=2, label='GT', marker="p")
plt.plot(x + 1, test_cmc3, color="green", linewidth=2, label='PALM', marker="x")
plt.plot(x + 1, test_cmc4, color="cyan", linewidth=2, label='EAR', marker=">")
plt.plot(x + 1, test_cmc5, color="black", linewidth=2, label='EAR79', marker=">")

plt.legend()
plt.xlabel("Rank")  
plt.ylabel("Recognition rate (%)")
plt.legend(loc='lower right', fontsize='xx-large')
plt.title("CMC curves")
plt.grid(ls='--')
plt.show()