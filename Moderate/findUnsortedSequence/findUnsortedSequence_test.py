from findUnsortedSequence import findUnsortedSequence
import pytest

def test_findUnsortedSequence():
	arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
	res = findUnsortedSequence(arr)
	assert(res[0] == 3)
	assert(res[1] == 9)
