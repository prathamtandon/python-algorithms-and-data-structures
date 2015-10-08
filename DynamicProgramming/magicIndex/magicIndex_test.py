from magicIndex import magicIndex
from magicIndex import magicIndex_Repition

def test_magicIndex_pass():
	arr = [-10,-5,2,4,6]
	assert(magicIndex(arr) == 2)

def test_magicIndex_fail():
	arr = [-10,-5,3,4,6]
	assert(magicIndex(arr) == -1)

def test_magicIndex_Repition_pass():
	arr = [-10,-5,1,3,3,3,4,6,8,9,12,13]
	assert(magicIndex_Repition(arr) == 3)
	arr = [-10,-5,1,1,1,4,5,7,9,12,13]
	assert(magicIndex_Repition(arr) == 7)

def test_magicIndex_Repition_fail():
	arr = [-10,-5,1,1,1,4,5,9,9,12,13]
	assert(magicIndex_Repition(arr) == -1)
