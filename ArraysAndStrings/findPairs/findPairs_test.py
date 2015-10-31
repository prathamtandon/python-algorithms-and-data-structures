from findPairs import findPairs
import pytest

def test_findPairs():
    array = [3,4,7,1,2,9,8]

    result = findPairs(array)

    assert((3,8) in result)
    assert((4,7) in result)

    array = [65, 30, 7, 90, 1, 9, 8]

    result = findPairs(array)

    assert(result is None)
