from maxMinutes import maxSum,maxSum3,maxSum4
import pytest

def test_maxMinutes():
    arr = [30,15,60,75,45,15,15,45]

    assert(maxSum(arr) == 180)
    assert(maxSum3(arr) == 180)
    assert(maxSum4(arr) == 180)
