from checkDuplicates import checkDuplicates
import pytest

def test_checkDuplicates():
	arr = [12,3,5,17,3,3,22,12,17]
	result = checkDuplicates(arr, 17)
	assert(len(result) == 3)
	assert(3 in result)
	assert(12 in result)
	assert(17 in result)
