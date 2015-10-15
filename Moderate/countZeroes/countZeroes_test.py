from countZeroes import countZeroes
import pytest

def test_countZeroes():
    assert(countZeroes(3) == 0)
    assert(countZeroes(10) == 2)
    assert(countZeroes(14) == 2)
