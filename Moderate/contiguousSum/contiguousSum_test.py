from contiguousSum import contiguousSum
import pytest

def test_contiguousSum():
    arr = [2,-8,3,-2,4,-10]
    assert(contiguousSum(arr) == 5)
