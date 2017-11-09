# encoding=utf-8
import Classification_KNN  # 导入Knn模块
from numpy import *

# group,labels=Classification_KNN.createDataSet()  # 创建了变量
# Classification_KNN.classfy0([0,0],group,labels,3)
# reload(Classification_KNN)
datingDataMat,datingLabels = Classification_KNN.file2matrix('datingTestSet2.txt')