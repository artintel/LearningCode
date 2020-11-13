# CMC_rank

在 `CMC.py` 中通过 `from CMC_rank.CMC_data_file import CMC.py` 进行内部的计算

每当要加入新的数据时。

1. 初始化 test_cmcno = []
2. test_cmcno = CMC(label_root, list_root, class_num)
3. test_cmcno = np.array(test_cmcno)
4. ...
5. plt.plot(...)

# insightface_pytorch_datasets_make

Insightface_pytorch版本的自定义数据准备过程，之后再更新具体流程