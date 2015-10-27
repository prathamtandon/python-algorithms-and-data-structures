from countSetBits import countSetBits
import pytest

def test_countSetBits():
    n = 5
    count = 2
    assert(countSetBits(n) == count)
