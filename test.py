# coding : utf-8

from numpy import *
import operator 
import KNN

group, labels = KNN.createDataSet()

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        numOflabel = labels[sortedDistances[i]]
        classCount[numOflabel] = classCount.get(numOflabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

my = classify([0,0], group, labels, 3)
print (my)