import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0,1.1], [1.0, 1.0], [0,0], [0, 0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX, dataSet, labels, k):
	#how many examples
	dataSetSize = dataSet.shape[0]
	#calculate the distance between inX and all dataset
	diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
	sqdiffMat = diffMat ** 2
	distance = sqdiffMat.sum(axis=1) ** 0.5
	#sort
	sortedDictIndex = distance.argsort()

	classCount = {}
	for i in range(k):
		#get the i'st close's label
		voteLabel = labels[sortedDictIndex[i]]
		#calculate each labels
		classCount[voteLabel] = classCount.get(voteLabel,0) + 1

	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
	
	return sortedClassCount[0][0]


#main

group, labels=createDataSet()
print ">group:\n",group

print ">labels:\n",labels

print ">input label:\n[0, 0]" 
a = classify0([0,0], group, labels, 3)
print ">label:\n", a
