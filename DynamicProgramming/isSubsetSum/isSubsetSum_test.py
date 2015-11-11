from isSubsetSum import isSubsetSum
import pytest

def test_isSubsetSum():
        arr = [3,34,4,12,5,2]
        sum_val = 9
        output = True
        
        assert(isSubsetSum(arr,len(arr),sum_val) == output)
