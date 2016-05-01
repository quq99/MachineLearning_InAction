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
	#axis:which features; value:feature need to return
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

#choose the way to divide dataset
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1

	for i in range(numFeatures):
		#all i'st feature create a list
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)#no duplicate
		
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)

		infoGain = baseEntropy - newEntropy
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature


#main function
myData, labels = createDataSet()
print myData
a = calcShannonEnt(myData)
print a
b = chooseBestFeatureToSplit(myData)
print b
