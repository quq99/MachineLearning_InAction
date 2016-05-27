import numpy as np


def loadDataSet():
	postingList = [['my', 'dog', 'has', 'flea', \
			'problems', 'help','please'],\
			 ['maybe', 'not', 'take', 'him',\
			'to', 'dog', 'park', 'stupid'],\
			['my', 'dalmation', 'is', 'so', \
			'cute', 'I', 'love', 'him'],\
			['stop', 'posting', 'stupid', 'worthless',\
			'garbage'],
			['mr', 'licks', 'ate', 'my', 'steak', 'how',\
			'to', 'stop', 'him'],
			['quit', 'buying', 'worthless', 'dog', \
			'food', 'stupid']]
	classVec = [0,1,0,1,0,1]
	return postingList, classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for doc in dataSet:
		vocabSet = vocabSet | set(doc)
	return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in the vocabulary!" % word
	return returnVec

def trainNB0(trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numwords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)#p(c1)
	p0Num = np.zeros(numwords)
	p1Num = np.zeros(numwords)
	p0Denom = 0.0
	p1Denom = 0.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = p1Num/p1Denom
	p0Vect = p0Num/p0Denom
	return p0Vect, p1Vect, pAbusive
#main
listOposts, listClasses = loadDataSet()
myvocablist = createVocabList(listOposts)
print myvocablist
returnvec = setOfWords2Vec(myvocablist, listOposts[0])
print returnvec
returnvec2 = setOfWords2Vec(myvocablist, listOposts[3])
print returnvec2

trainMat = []
for p in listOposts:
	trainMat.append(setOfWords2Vec(myvocablist, p))

p0V,p1V,pAb = trainNB0(trainMat, listClasses)
print p0V
print p1V
print pAb

