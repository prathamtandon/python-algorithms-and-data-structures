from maxProduct import maxProduct
import pytest

def test_maxProduct():
    arr = [6,-10,-3,0,2]
    assert(maxProduct(arr) == 180)

    arr = [-1,-3,-10,0,60]
    assert(maxProduct(arr) == 60)
