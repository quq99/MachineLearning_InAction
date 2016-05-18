import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0,1.1], [1.0, 1.0], [0,0], [0, 0.1]])
	labels = ['A','A','B','B']
	return group,labels

def file2matrix(filename):
	featureNum = 3
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = np.zeros((numberOfLines,featureNum))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		listFromLine = line.strip().split('\t')
		returnMat[index,:] = listFromLine[0:featureNum]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = ( dataSet - np.tile(minVals, (m,1)) )/np.tile(ranges, (m,1))
	return normDataSet, ranges, minVals
	

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
