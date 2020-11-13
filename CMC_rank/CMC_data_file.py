import numpy as np

def change_method(root, label, class_num):
    with open(root, 'r') as file:
        lines = file.read()
        lines = lines.split(']], [[')
        for i in range(len(lines)):
            lines[i] = lines[i].replace('[[[', '')
            lines[i] = lines[i].replace(']]]', '')
            n = lines[i].split(', ')
            label += n
        label = np.array(label).reshape((-1, class_num))
        label = label.astype(np.float32)
    return label

def change(label_root, predict_root, class_num):
    ground_truth_label = []
    predict_label = []
    ground_truth_label = change_method(label_root, ground_truth_label, class_num)
    predict_label = change_method(predict_root, predict_label, class_num)
    return ground_truth_label, predict_label

def CMC(label_root, predict_root, class_num, maxOrmin):
    test_cmc = []  # 保存accuracy，记录rank1到rank48的准确率
    test_y, predict_label = change(label_root, predict_root, class_num)
    # sort_index = np.argsort(predict_label, axis=1)  # predict_label为模型预测得到的匹配分数矩阵；降序排序，返回匹配分数值从大到小的索引值
    if maxOrmin == 'max':
        sort_index = np.argsort(-predict_label, axis=1)
        actual_index = np.argmax(test_y, 1)  # test_y为测试样本的真实标签矩阵；返回一列真实标签相对应的最大值的索引值
        predict_index = np.argmax(predict_label, 1)  # 返回一列预测标签相对应的最大值的索引值
    else:
        sort_index = np.argsort(predict_label, axis=1) # predict_label为模型预测得到的匹配分数矩阵；降序排序，返回匹配分数值从小到大的索引值
        actual_index = np.argmax(test_y, 1)  # test_y为测试样本的真实标签矩阵；返回一列真实标签相对应的最大值的索引值
        predict_index = np.argmin(predict_label, 1)  # 返回一列预测标签相对应的最大值的索引值
    temp = np.cast['float32'](np.equal(actual_index, predict_index))  # 一列相似值，1代表相同，0代表不同
    test_cmc.append(np.mean(temp))  # rank1
    # rank2到rank15
    for i in range(19):
        for j in range(len(temp)):
            if temp[j] == 0:
                predict_index[j] = sort_index[j][i + 1]
        temp = np.cast['float32'](np.equal(actual_index, predict_index))
        test_cmc.append(np.mean(temp))
    return test_cmc