# 制作 .lst : 注意路径问题

```bash
python make_lst.py --dataset-dir D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\EAR_train --list-file D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\lst\train.lst --img-ext '.bmp'
```

# 创建property文件，注意不要有后缀

在文件中输入：class_num,112,112

class_num 代表类别个数

112，112 代表图片尺寸

# 生成rec & idx 文件

运行`face2rec.py` (同时注意：需要 face_image.py 和 face_preprocess.py文件)
也可以通过：

```bash
python face2rec.py --prefix D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\dataset_file\lst --root D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\dataset_file\EAR_train 
```
的方式进行。

# 生成 pairs.txt 文件

```bash
python generate_image_pairs.py --data-dir D:\PycharmProjects\LearningProject\
insightface_pytorch_datasets_make\dataset_file\EAR_train --outputtxt D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\dataset_file\lst\pairs.txt

```

# 生成 .bin 文件

`--data-dir`: .lst 文件路径

```bash
python lfw2pack.py --data-dir D:\PycharmProjects\LearningProject\insightface_pytorch_datasets_make\dataset_file\lst --output D:\PycharmProjects\
LearningProject\insightface_pytorch_datasets_make\dataset_file\lst\EAR.bin --num-samepairs 11000

```