from longestIncreasingSeq import longestIncreasingSeq
import pytest

def test_longestIncreasingSeq():
	arr = [13,14,10,11,12]
	res = longestIncreasingSeq(arr)
	
	assert(res == [10,11,12])
