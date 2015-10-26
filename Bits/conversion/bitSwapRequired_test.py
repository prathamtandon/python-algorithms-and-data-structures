from bitSwapRequired import bitSwapRequired
import pytest

def test_bitSwapRequired():
    a = 29
    b = 15
    assert(bitSwapRequired(a,b) == 2)
