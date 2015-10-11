from merge import merge
import pytest

def test_merge():
	A = [1,2,4,None,None]
	B = [3,6]
	
	merge(A,B)
	
	assert(A == [1,2,3,4,6])
	
	A = [12,14,15,None,None]
	B = [1,2]
	
	merge(A,B)
	
	assert(A == [1,2,12,14,15])
