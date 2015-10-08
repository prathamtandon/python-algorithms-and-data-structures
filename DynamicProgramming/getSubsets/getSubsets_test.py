from getSubsets import getSubsets
import pytest

def test_getSubsets():
    assert(getSubsets([]) == [[]])
    subsets_1 = getSubsets([1])
    assert(len(subsets_1) == 2)
    assert([] in subsets_1)
    assert([1] in subsets_1)
    subsets_2 = getSubsets([1,2])
    assert(len(subsets_2) == 4)
    assert([] in subsets_2)
    assert([1] in subsets_2)
    assert([2] in subsets_2)
    assert([1,2] in subsets_2)
