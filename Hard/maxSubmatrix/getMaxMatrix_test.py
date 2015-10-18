from getMaxMatrix import getMaxMatrix
import pytest

def test_getMaxMatrix():
    matrix = [[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
    res = getMaxMatrix(matrix)

    assert(res.getSum() == 33)
