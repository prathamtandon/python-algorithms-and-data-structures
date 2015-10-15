from sumPairs import sumPairs
import pytest

def test_sumPairs():
    arr = [12,9,-2,6,5,4,1,2]
    target = 7


    pairs = sumPairs(arr, target)
    assert(len(pairs) == 3)
    assert((-2,9) in pairs)
    assert((1,6) in pairs)
    assert((2,5) in pairs)

