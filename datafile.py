#using utf-8
'''
数据集说明:
Caltech-UCSD Birds-200-2011
官方网站:http://www.vision.caltech.edu/visipedia/CUB-200-2011.html
（1）类别数目: 200
（2）图像总数目: 11,788
（3）每张图片的标注信息: 15 Part Locations, 312 Binary Attributes, 1 Bounding Box

'''
imort unzp
!wget http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz

'''
备用数据集:AI研习社鸟类分类

https://dwz.cn/ijPVPQhz

本数据集一共分为三部分训练集、验证集、测试集、。

训练集包含8251张图片以及该图片所对应的200个classes索引文件train_pname_to_index.csv，可与classes.txt对照找到图片所对应的真实标签。

验证集包含1768张图片以及该图片所对应的200个classes索引文件val_pname_to_index.csv，可与classes.txt对照找到图片所对应的真实标签。

测试集包含1768张图片，需参赛者预测生成与训练集、验证集类似的csv索引文件用于组委会评判。
'''
