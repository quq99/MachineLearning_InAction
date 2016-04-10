#caculate the entropy of the given dataset

from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)#number of the samples
	labelCounts = {}#key: the name of different categories;
			# value:number of each category.
	
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0#add new and set the value to 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt


def createDataSet():
	dataSet = [[1, 1, 'yes'],
			[1, 1, 'yes'],
			[1, 0, 'no'],
			[0, 1, 'no'],
			[0, 1, 'no']]

	labels = ['no surfacing', 'flippers']
	return dataSet, labels


#splitDataSet

def splitDataSet(dataSet, axis, value):
	#axis:features; value:feature need to return
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
