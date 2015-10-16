from allLengths import getAllLengths
import pytest

def test_getAllLengths():
    k = 2
    shorter = 5
    longer = 10

    lengths = getAllLengths(k, shorter, longer)
    assert(len(lengths) == 3)
    assert(10 in lengths)
    assert(15 in lengths)
    assert(20 in lengths)
