from findLongestSubarray import findLongestSubarray
import pytest

def test_findLongestSubarray():
    arr = ['1','2','w','e','5','6','f','8']
    res = findLongestSubarray(arr)

    assert(res == ['w','e','5','6','f','8'])
