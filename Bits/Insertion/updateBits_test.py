from updateBits import updateBits
import pytest

def test_updateBits():
    n = 1024
    m = 19
    i = 2
    j = 6
    assert(updateBits(n,m,i,j) == 1100)
