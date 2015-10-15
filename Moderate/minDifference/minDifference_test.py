from minDifference import minDifference
import pytest

def test_minDifference():
    arr1 = [1,3,15,11,2]
    arr2 = [23,127,235,19,8]

    assert(minDifference(arr1,arr2) == 3)
