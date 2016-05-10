import cPickle as pickle
def storeTree(inputTree, filename):
	fw = open(filename, 'w')
	pickle.dump(inputTree, fw)
	fw.close()

def grabTree(filename):
	fr = open(filename)
	return pickle.load(fr)

mytree = {'no surfacing' :{0:'no', 1:{'flippers':{0:'no', 1:'yes'}}}}

storeTree(mytree,'classifierStore.txt')
print grabTree('classifierStore.txt')
